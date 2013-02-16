from django import forms

from .models import Pair


class PairForm(forms.ModelForm):
    class Meta:
        model = Pair

    def clean_key(self):
        return self.cleaned_data['key'].upper()


class UserForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

