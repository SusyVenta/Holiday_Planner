from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    """ Extends default registration form by adding required email address """
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        """ What fields I use and in what order """
        fields = ['username', 'email', 'password1', 'password2']

