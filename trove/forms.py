from django import forms

from .models import Project


class DictField(object): pass

class ProjectForm(forms.ModelForm):
    secrets = DictField()

    class Meta:
        model = Project


class UserForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

