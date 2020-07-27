from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .select_countries import select_options

'''
CountriesChoice class is using a select_options() function to create a form.
It creates a multiple choice fields with checkbox inside.
As an options it takes a values (names of the countries) from the json file sorted by continent.
'''


class CountriesChoice(forms.Form):

    Europe = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple(),
                                       choices=select_options('Europe'))
    Asia = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple(),
                                       choices=select_options('Asia'))
    Africa = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple(),
                                       choices=select_options('Africa'))
    Antarctica = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple(),
                                       choices=select_options('Antarctica'))

    Oceania = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple(),
                                       choices=select_options('Oceania'))

    South_America = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple(),
                                       choices=select_options('South America'))

    North_America = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple(),
                                       choices=select_options('North America'))


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

