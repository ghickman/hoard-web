from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Deployment, Env, Pair, Project


class EnvSerializer(ModelSerializer):
    projects = SerializerMethodField('get_projects')

    class Meta:
        fields = ('name', 'projects')
        model = Env

    def get_projects(self, obj):
        return obj.projects


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


class ProjectSerializer(ModelSerializer):
    envs = SerializerMethodField('get_envs')

    class Meta:
        fields = ('name', 'envs')
        model = Project

    def get_envs(self, obj):
        return obj.envs

