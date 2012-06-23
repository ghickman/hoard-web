from django.db import models
from django_hstore import hstore


class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    environment = models.CharField(max_length=255)
    secrets = hstore.DictionaryField(db_index=True)

    objects = hstore.HStoreManager()

    def __unicode__(self):
        return self.name

