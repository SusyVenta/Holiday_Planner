from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import ListView, UpdateView
from .models import PlacesVisited
from .forms import CountriesUpdateForm
from .maps_creation import MapCreation
import json
from django.shortcuts import render,get_object_or_404,redirect
try:
    from django.contrib.auth import get_user_model

    user_model = get_user_model()
except ImportError:
    from django.contrib.auth.models import User

    user_model = User


# from django.db import connection
# tables = connection.introspection.table_names()
# print(f"existing tables: {tables}")
# seen_models = connection.introspection.installed_models(tables)
# print(f"seen_models: {seen_models}")


class VisitedCountriesView(LoginRequiredMixin, ListView):
    template_name = 'user_maps/visited_places.html'

    def post(self, request, *args, **kwargs):
        """
        - form is the html template updated with the choices marked in the drop-down menus
        - to see countries visited by user: print(request.user.placesvisited.european_countries)
        """
        form = CountriesUpdateForm(request.POST, instance=request.user.placesvisited)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/places_visited")
        else:
            return render(request, self.template_name, {'form': form})

    def get(self, request, *args):
        """ Passing placesvisited also in get request so that update does not replace existing choices, but builds
        upon it """

        """ Get countries visited in the form of a list"""
        europe = str(request.user.placesvisited.european_countries).split(",")
        asia = str(request.user.placesvisited.asian_countries).split(",")
        africa = str(request.user.placesvisited.african_countries).split(",")
        oceania = str(request.user.placesvisited.oceania_countries).split(",")
        antarctica = str(request.user.placesvisited.antarctic_countries).split(",")
        north_america = str(request.user.placesvisited.north_american_countries).split(",")
        south_america = str(request.user.placesvisited.south_american_countries).split(",")
        countries_list = europe+africa+oceania+antarctica+north_america+south_america+asia
        cleaned_list = []
        for element in countries_list:
            cleaned_item = element.strip()
            if cleaned_item != "":
                cleaned_list.append(cleaned_item)
        print(f"countries visited: {cleaned_list}")
        """ Refreshes map, highlighting countries visited """
        MapCreation().create_base_map(cleaned_list)
        form = CountriesUpdateForm(instance=request.user.placesvisited)
        return render(request, self.template_name, {'form': form})

