from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    """ Extends default registration form by adding required email address """
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        """ What fields I use and in what order """
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    """ For users to update their model """
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        """ What fields I use and in what order """
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

