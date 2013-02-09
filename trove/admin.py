from django.contrib import admin

from .models import Deployment, Env, Pair, Project


class PairInline(admin.TabularInline):
    extra = 1
    model = Pair


class DeploymentAdmin(admin.ModelAdmin):
    inlines = [PairInline]
    list_filter = ('env', 'project')


admin.site.register(Deployment, DeploymentAdmin)
admin.site.register(Env)
admin.site.register(Project)
