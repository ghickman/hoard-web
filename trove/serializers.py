from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, SerializerMethodField

from .models import Env, Pair, Project


class EnvSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(slug_field='name')
    # TODO: List projects, w/ urls

    class Meta:
        fields = ('url', 'name')
        model = Env


class PairSerializer(ModelSerializer):
    class Meta:
        fields = ('key', 'value')
        model = Pair

    def convert_object(self, obj):
        return {obj.key: obj.value}


class ProjectSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(slug_field='name')
    envs = SerializerMethodField('get_envs')

    class Meta:
        fields = ('url', 'name', 'envs')
        model = Project

    def get_envs(self, obj):
        return Env.objects.filter(deployment__project=obj).values_list('name', flat=True)

