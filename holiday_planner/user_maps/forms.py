from django import forms
from .models import PlacesVisited

'''
CountriesUpdateForm class displays and retrieves information from the multiple choice menus, in order specified below.
'''


class CountriesUpdateForm(forms.ModelForm):
    class Meta:
        model = PlacesVisited
        fields = ['asian_countries', 'european_countries', 'oceania_countries', 'african_countries',
                  'south_american_countries', 'north_american_countries', 'antarctic_countries']
