from django.http import HttpResponseNotFound
from djangorestframework.mixins import CreateModelMixin, ListModelMixin
from djangorestframework.resources import ModelResource

from .auth import AuthMixin
from .forms import ProjectForm
from .models import Env, Project


class EnvResource(ModelResource):
    model = Env

    fields = ['id', 'name']


class ProjectResource(ModelResource):
    # form_class = ProjectForm
    model = Project

    # fields = ['secrets']

    # def secrets(self, instance):
    #     return instance.secrets


class EnvView(AuthMixin, CreateModelMixin, ListModelMixin):
    resource = EnvResource


class ProjectView(AuthMixin, CreateModelMixin, ListModelMixin):
    resource = ProjectResource

    def get(self, request, *args, **kwargs):
        if not 'env' in request.GET:
            return super(ProjectView, self).get(request, *args, **kwargs)

        filter_kwargs = {'name': kwargs['name'], 'env__name': request.GET['env']}
        try:
            return self.resource.model.objects.get(**filter_kwargs)
        except self.resource.model.DoesNotExist:
            return HttpResponseNotFound()

