import uuid

from django.db import models
from django.utils import timezone

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


class Access(models.Model):
    """
    When a user authenticates with the site (by whatever method) they obtain
    an access token, which is modelled by this table.
    """
    user = models.ForeignKey('auth.User')
    token = models.CharField(max_length=32, blank=True)

    active = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        verbose_name_plural = 'accesses'

    def __unicode__(self):
        return self.token

    def save(self, *args, **kwargs):
        new = not self.token  # new ones (should) never specify a token
        if new:
            self.token = uuid.uuid4().hex
        return super(Access, self).save(*args, **kwargs)

    def is_authenticated(self):
        """Access objects can mock as a user for djangorestframework."""
        return True

