from tastypie import fields
from tastypie.api import Api
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource

from .models import Project


class ProjectResource(ModelResource):
    secrets = fields.DictField(attribute='secrets')

    class Meta:
        allowed_methods = ('get',)
        fields = ('name', 'environment', 'secrets')
        filtering = {
            'environment': ('exact',),
            'name': ('exact',)
        }
        # authentication = BasicAuthentication()
        # authorization = DjangoAuthorization()
        queryset = Project.objects.all()

    def dehydrate_secrets(self, bundle):
        return [{k: v} for k, v in bundle.data['secrets'].items()]

