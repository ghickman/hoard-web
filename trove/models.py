from django.db import models

from .fields import AESPickledObjectField


class Env(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    env = models.ForeignKey('Env')
    secrets = AESPickledObjectField()

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

