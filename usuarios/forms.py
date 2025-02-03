# usuarios/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2', 'telefone']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)