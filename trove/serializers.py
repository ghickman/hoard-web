from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, SerializerMethodField

from .models import Deployment, Env, Pair, Project


class EnvSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(slug_field='name')
    # TODO: List projects, w/ urls

    class Meta:
        fields = ('url', 'name')
        model = Env


class PairSerializer(ModelSerializer):
    class Meta:
        model = Deployment

    def convert_object(self, obj):
        return {pair.key: pair.value for pair in obj.pairs.all()}

    def from_native(self, data, files):
        for k, v in data.items():
            pair, created = Pair.objects.get_or_create(
                deployment=self.object,
                key=k.upper(),
                defaults={'value': v},
            )
            if created:
                self.object.pairs.add(pair)
            else:
                pair.value = v
                pair.save()
        return self.object


class ProjectSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(slug_field='name')
    envs = SerializerMethodField('get_envs')

    class Meta:
        fields = ('url', 'name', 'envs')
        model = Project

    def get_envs(self, obj):
        return Env.objects.filter(deployment__project=obj).values_list('name', flat=True)

