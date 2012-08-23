from djangorestframework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin
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


class ProjectView(AuthMixin, CreateModelMixin, UpdateModelMixin, ListModelMixin):
    resource = ProjectResource

    def get_query_kwargs(self, *args, **kwargs):
        query_kwargs = super(ProjectView, self).get_query_kwargs(*args, **kwargs)
        if 'env' in self.request.GET:
            query_kwargs['env__name'] = self.request.GET['env']
        return query_kwargs

