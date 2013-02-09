from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer

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
    # TODO: List envs, w/ urls
    # envs = ManyHyperlinkedRelatedField(view_name='env-detail')

    class Meta:
        fields = ('url', 'name')#, 'envs')
        model = Project

