from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView, TemplateView

from . import views


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^login/?', 'rest_framework.authtoken.views.obtain_auth_token'),

    url(r'^envs/?$', views.EnvList.as_view(), name='env-list'),
    url(r'^envs/(?P<name>[\w-]+)/?$', views.EnvDetail.as_view(), name='env-detail'),

    url(r'^projects/?$', views.ProjectList.as_view(), name='project-list'),
    url(r'^projects/(?P<name>[\w-]+)/?$', views.ProjectDetail.as_view(), name='project-detail'),
    url(r'^projects/(?P<name>[\w-]+)/envs/(?P<env_name>[\w-]+)/?$', views.DeploymentDetail.as_view(), name='deployment-detail'),
    url(r'^projects/(?P<project>[\w-]+)/envs/(?P<env>[\w-]+)/keys/(?P<key>[\w-]+)/?$', views.PairDelete.as_view(), name='pair-delete'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^favicon.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'favicon.ico')),
)

urlpatterns += staticfiles_urlpatterns()

