from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer, SerializerMethodField

from .fields import DeploymentURLField, PairsField, SlugHyperlinkedRelatedField
from .models import Deployment, Env, Project


class DeploymentSerializer(HyperlinkedModelSerializer):
    url = DeploymentURLField()
    env = SlugHyperlinkedRelatedField(view_name='env-detail')
    project = SlugHyperlinkedRelatedField(view_name='project-detail')
    pairs = PairsField()

    class Meta:
        fields = ('url', 'env', 'project', 'pairs')
        model = Deployment


class EnvSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(slug_field='name')
    # TODO: List projects, w/ urls

    class Meta:
        fields = ('url', 'name')
        model = Env


class ProjectSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(slug_field='name')
    envs = SerializerMethodField('get_envs')

    class Meta:
        fields = ('url', 'name', 'envs')
        model = Project

    def get_envs(self, obj):
        return Env.objects.filter(deployment__project=obj).values_list('name', flat=True)

