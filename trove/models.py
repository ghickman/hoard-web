from django.db import models

from .fields import AESPickledObjectField


class Deployment(models.Model):
    env = models.ForeignKey('Env')
    project = models.ForeignKey('Project')

    class Meta:
        unique_together = ('env', 'project')

    def __unicode__(self):
        return '{0}: {1}'.format(self.project, self.env)


class Env(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name


class Pair(models.Model):
    deployment = models.ForeignKey('Deployment', related_name='pairs')
    # TODO: encrypt these two at the db level
    key = models.CharField(max_length=511)
    value = models.CharField(max_length=511)

    class Meta:
        ordering = ('key',)
        unique_together = ('key', 'value', 'deployment')

    def __unicode__(self):
        return '{0}={1}'.format(self.key, self.value)


class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

