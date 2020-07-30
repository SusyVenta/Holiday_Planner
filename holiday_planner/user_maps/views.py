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
from .select_countries_and_cities import select_cities_options
from multiselectfield import MultiSelectField

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
        europe2 = request.user.placesvisited.european_countries
        asia2 = request.user.placesvisited.asian_countries
        africa2 = request.user.placesvisited.african_countries
        oceania2 = request.user.placesvisited.oceania_countries
        antarctica2 = request.user.placesvisited.antarctic_countries
        north_america2 = request.user.placesvisited.north_american_countries
        south_america2 = request.user.placesvisited.south_american_countries
        countries_list2 = europe2 + africa2 + oceania2 + antarctica2 + north_america2 + south_america2 + asia2




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
        """ Refreshes map, highlighting countries visited """
        MapCreation().create_base_map(cleaned_list)
        countries_visited_drop_down = []
        for country in cleaned_list:
            countries_visited_drop_down.append((country, country))
        form = CountriesUpdateForm(instance=request.user.placesvisited)
        """ Need to pass cities available for countries visited """
        print(f"countries visited: {cleaned_list}\n")
        visited = MultiSelectField(choices=countries_visited_drop_down, default="-", blank=True)
        # print(request.user.placesvisited.filter(antarctica))
        all_cities = select_cities_options()

        return render(request, self.template_name, {'form': form, 'countries_visited': cleaned_list,
                                                    'countries_and_cities': all_cities, "visited": countries_visited_drop_down})

