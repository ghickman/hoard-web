from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView, TemplateView

from core.api import ProjectResource


admin.autodiscover()
project_resource = ProjectResource()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='core/home.html'), name='home'),
    url(r'^api/', include(project_resource.urls)),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^favicon.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'favicon.ico'), name='favicon'),
)

urlpatterns += staticfiles_urlpatterns()

