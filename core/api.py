from django.conf.urls.defaults import url
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
        filtering = {'environment': ('exact',)}
        # authentication = BasicAuthentication()
        # authorization = DjangoAuthorization()
        queryset = Project.objects.all()

    def dehydrate_secrets(self, bundle):
        return [{k: v} for k, v in bundle.data['secrets'].items()]

    def override_urls(self):
        """
        http://django-tastypie.rtfd.org/en/latest/cookbook.html#using-non-pk-data-for-your-urls
        """
        return [
            url(r'^(?P<resource_name>%s)/(?P<name>[\w\d_-]+)/$' % self._meta.resource_name,
                self.wrap_view('dispatch_detail'), name='api_dispatch_detail'),
        ]

