from django.db import models


class Deployment(models.Model):
    env = models.ForeignKey('Env')
    project = models.ForeignKey('Project')

    class Meta:
        unique_together = ('env', 'project')

    def __str__(self):
        return '{0}: {1}'.format(self.project, self.env)


class Env(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    @property
    def projects(self):
        kwargs = {'deployment__env': self}
        return Project.objects.filter(**kwargs).values_list('name', flat=True)


class Pair(models.Model):
    deployment = models.ForeignKey('Deployment', related_name='pairs')
    # TODO: encrypt these two at the db level
    key = models.CharField(max_length=511)
    value = models.CharField(max_length=511)

    class Meta:
        ordering = ('key',)
        unique_together = ('key', 'value', 'deployment')

    def __str__(self):
        return '{0}={1}'.format(self.key, self.value)


class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    @property
    def envs(self):
        kwargs = {'deployment__project': self}
        return Env.objects.filter(**kwargs).values_list('name', flat=True)

