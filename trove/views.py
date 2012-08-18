from djangorestframework.mixins import CreateModelMixin, ReadModelMixin
from djangorestframework.resources import ModelResource

from .auth import AuthMixin
from .models import Project


# create project resource that doesn't let you change the project/env
class ProjectResource(ModelResource):
    model = Project

    # fields = ['secrets']

    # def secrets(self, instance):
    #     return instance.secrets


class ProjectView(AuthMixin, CreateModelMixin, ReadModelMixin):
    resource = ProjectResource

    def get_instance(self, **kwargs):
        return Project.objects.get(name=self.kwargs['project'], env=self.kwargs['env'])

