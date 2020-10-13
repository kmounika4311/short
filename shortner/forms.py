from django import forms
from .models import ShortUrl
from django.contrib.auth.models import User

class UrlForm(forms.ModelForm):
    class Meta:
        model = ShortUrl
        fields = ['url']

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']