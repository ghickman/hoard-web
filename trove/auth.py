import re

from django import forms
from django.contrib.auth import authenticate
from djangorestframework.authentication import BaseAuthentication
from djangorestframework.response import ErrorResponse
from djangorestframework.status import HTTP_400_BAD_REQUEST
from djangorestframework.views import View

from .models import Access


class UserForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)


class APIKeyAuthentication(BaseAuthentication):
    """This is for application-level access.

    Similarly to the access token auth, we expect an Authorization header, but
    in the form token <application_key>.
    """
    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header:
            return None

        m = re.match(r'Token ([a-f0-9]{32})', auth_header, re.I)
        if not m:
            return None

        try:
            access = Access.objects.get(token=m.group(1).lower())
        except Access.DoesNotExist:
            return None
        return access


class GetAccessToken(View):
    authentication = [APIKeyAuthentication]
    form = UserForm

    def post(self, request, *args, **kwargs):
        user = authenticate(username=self.CONTENT['username'], password=self.CONTENT['password'])
        if not user:
            raise ErrorResponse(HTTP_400_BAD_REQUEST, {'detail': 'invalid username or password'})
        access, created = Access.objects.get_or_create(user=user)
        response_data = {'access_token': access.token}
        return response_data

