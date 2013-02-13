from django.http import Http404
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Pair, Env, Project
from .serializers import PairSerializer, EnvSerializer, ProjectSerializer


class SlugFieldMixin(object):
    slug_field = 'name'
    slug_url_kwarg = 'name'


class PairList(ListAPIView):
    model = Pair
    serializer_class = PairSerializer

    def get_object(self):
        kwargs = {
            'deployment__project__name': self.kwargs['name'],
            'deployment__env__name': self.kwargs['env_name'],
        }
        try:
            return self.model.objects.get(**kwargs)
        except self.model.DoesNotExist:
            raise Http404


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

