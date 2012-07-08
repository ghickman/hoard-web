from django.db import models
from django_hstore import hstore


class Project(models.Model):
    name = models.CharField(max_length=255)
    env = models.CharField(max_length=255)
    secrets = hstore.DictionaryField(db_index=True)

    objects = hstore.HStoreManager()

    class Meta:
        unique_together = ('name', 'env')

    def __unicode__(self):
        return self.name

