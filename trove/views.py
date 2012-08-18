from djangorestframework.mixins import ReadModelMixin
from djangorestframework.resources import ModelResource

from .auth import AuthMixin
from .models import Project


class ProjectResource(ModelResource):
    model = Project

    fields = ['secrets']

    def secrets(self, instance):
        return instance.secrets


class Detail(AuthMixin, ReadModelMixin):
    resource = ProjectResource

    def get_instance(self, **kwargs):
        return Project.objects.get(name=self.kwargs['project'], env=self.kwargs['env'])

