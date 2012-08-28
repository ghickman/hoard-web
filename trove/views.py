import json

from djangorestframework.mixins import CreateModelMixin, ListModelMixin, ReadModelMixin, UpdateModelMixin
from djangorestframework.resources import ModelResource
from djangorestframework.response import ErrorResponse

from .auth import AuthMixin
from .models import Env, Project


class EnvResource(ModelResource):
    model = Env

    fields = ['id', 'name']


class ProjectResource(ModelResource):
    fields = [
        'name',
        'env',
        'secrets',
    ]
    model = Project


class EnvView(AuthMixin, CreateModelMixin, ListModelMixin):
    resource = EnvResource


class ProjectBase(AuthMixin):
    resource = ProjectResource

    def get_query_kwargs(self, *args, **kwargs):
        query_kwargs = super(ProjectBase, self).get_query_kwargs(*args, **kwargs)
        if 'env' in self.request.GET:
            query_kwargs['env__name'] = self.request.GET['env']
        return query_kwargs


class ProjectDetail(ProjectBase, ReadModelMixin):
    pass


class ProjectView(ProjectBase, CreateModelMixin, UpdateModelMixin, ListModelMixin):
    def get(self, request, *args, **kwargs):
        if 'env' in request.GET:
            return ProjectDetail.get(ProjectDetail(), request, *args, **kwargs)
        return super(ProjectView, self).get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        Couldn't work out how to make this method deal with the secrets dict
        being sent up so doing it myself instead.
        """
        def _error(msg):
            raise ErrorResponse(400, {'detail': msg})

        model = self.resource.model
        query_kwargs = self.get_query_kwargs(request, *args, **kwargs)
        try:
            data = json.loads(request.raw_post_data)
        except ValueError:
            # empty or not JSON
            _error('request data must be JSON encoded')

        try:
            secrets = data['secrets']
        except KeyError:
            _error('secrets field is required')

        try:
            self.model_instance = self.get_instance(**query_kwargs)
        except model.DoesNotExist:
            self.model_instance = model(**self.get_instance_data(model, secrets, *args, **kwargs))
        else:
            self.model_instance.secrets = secrets
            self.model_instance.save()

        return self.model_instance

