from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView, TemplateView

from .auth import GetAccessToken
from .views import EnvView, ProjectView


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^login/$', GetAccessToken.as_view()),
    url(r'^api/envs/$', EnvView.as_view()),
    url(r'^api/projects/$', ProjectView.as_view()),
    url(r'^api/projects/(?P<name>[\w-]+)/$', ProjectView.as_view()),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^favicon.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'favicon.ico')),
)

urlpatterns += staticfiles_urlpatterns()

