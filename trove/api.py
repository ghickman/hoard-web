from tastypie import fields
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource

from .models import Project


class ProjectResource(ModelResource):
    secrets = fields.DictField(attribute='secrets')

    class Meta:
        allowed_methods = ('get', 'post')
        fields = ('name', 'env', 'secrets')
        filtering = {
            'env': ('exact',),
            'name': ('exact',)
        }
        authentication = BasicAuthentication()
        authorization = Authorization()
        queryset = Project.objects.all()

    def dehydrate_secrets(self, bundle):
        return [{k: v} for k, v in bundle.data['secrets'].items()]

