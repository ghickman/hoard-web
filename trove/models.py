from django.db import models
from fields import AESPickledObjectField


class Project(models.Model):
    name = models.CharField(max_length=255)
    env = models.CharField(max_length=255)
    secrets = AESPickledObjectField()

    class Meta:
        unique_together = ('name', 'env')

    def __unicode__(self):
        return self.name

