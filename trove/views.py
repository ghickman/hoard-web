from django.http import Http404
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.mixins import UpdateModelMixin

from .models import Deployment, Env, Project
from .serializers import PairSerializer, EnvSerializer, ProjectSerializer


class SlugFieldMixin(object):
    slug_field = 'name'
    slug_url_kwarg = 'name'


class DeploymentDetail(UpdateModelMixin, RetrieveAPIView):
    model = Deployment
    serializer_class = PairSerializer

    def get_object(self):
        kwargs = {
            'project__name': self.kwargs['name'],
            'env__name': self.kwargs['env_name'],
        }
        try:
            return self.model.objects.get(**kwargs)
        except self.model.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class EnvDetail(SlugFieldMixin, RetrieveAPIView):
    model = Env
    serializer_class = EnvSerializer


class EnvList(ListAPIView):
    model = Env
    serializer_class = EnvSerializer


class ProjectDetail(SlugFieldMixin, RetrieveAPIView):
    model = Project
    serializer_class = ProjectSerializer


class ProjectList(ListAPIView):
    model = Project
    serializer_class = ProjectSerializer

