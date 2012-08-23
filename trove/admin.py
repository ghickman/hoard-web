from django.contrib import admin

from .models import Env, Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'env')
    list_filter = ('name', 'env')
    search_fields = ('name',)


admin.site.register(Env)
admin.site.register(Project, ProjectAdmin)
