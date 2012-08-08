from djangorestframework.mixins import ReadModelMixin
from djangorestframework.permissions import IsAuthenticated
from djangorestframework.resources import ModelResource
from djangorestframework.views import ModelView

from .auth import APIKeyAuthentication
from .models import Project


class ProjectResource(ModelResource):
    model = Project

    fields = ['secrets']

    def secrets(self, instance):
        return instance.secrets


class Detail(ModelView, ReadModelMixin):
    authentication = [APIKeyAuthentication]
    permissions = [IsAuthenticated]
    resource = ProjectResource

    def get_instance(self, **kwargs):
        return Project.objects.get(name=self.kwargs['project'], env=self.kwargs['env'])

