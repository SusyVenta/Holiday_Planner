from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import ListView, UpdateView
from .models import CitiesVisited, CitiesVisitedCountry
from .forms import CountriesUpdateForm, CitiesUpdateForm, SingleCountryUpdateForm
from .maps_creation import MapCreation
import json
from django.shortcuts import render, get_object_or_404, redirect

try:
    from django.contrib.auth import get_user_model

    user_model = get_user_model()
except ImportError:
    from django.contrib.auth.models import User

    user_model = User
from .select_countries_and_cities import select_cities_options, cities_variable_to_name_map
from multiselectfield import MultiSelectField

from django.db import connection


# tables = connection.introspection.table_names()
# print(f"existing tables: {tables}")
# seen_models = connection.introspection.installed_models(tables)
# print(f"seen_models: {seen_models}")
class ViewUtils:
    def countries_visited_list(self, request):
        europe = str(request.user.placesvisited.european_countries).split(",")
        asia = str(request.user.placesvisited.asian_countries).split(",")
        africa = str(request.user.placesvisited.african_countries).split(",")
        oceania = str(request.user.placesvisited.oceania_countries).split(",")
        antarctica = str(request.user.placesvisited.antarctic_countries).split(",")
        north_america = str(request.user.placesvisited.north_american_countries).split(",")
        south_america = str(request.user.placesvisited.south_american_countries).split(",")
        countries_list = europe + africa + oceania + antarctica + north_america + south_america + asia
        cleaned_list = []
        for element in countries_list:
            cleaned_item = element.strip()
            if cleaned_item != "":
                cleaned_list.append(cleaned_item)
        return cleaned_list


class VisitedCountriesView(LoginRequiredMixin, ListView):
    template_name = 'user_maps/visited_places.html'

    def post(self, request, *args, **kwargs):
        """
        - form is the html template updated with the choices marked in the drop-down menus
        - to see countries visited by user: print(request.user.placesvisited.european_countries)
        """
        form = CountriesUpdateForm(request.POST, instance=request.user.placesvisited)
        cities_form = CitiesUpdateForm(request.POST, instance=request.user.placesvisited)
        if form.is_valid() and cities_form.is_valid():
            print("### post form is valid")
            form.save()
            cities_form.save()
            return HttpResponseRedirect("/places_visited")
        else:
            return render(request, self.template_name, {'form': form})

    def get(self, request, *args):
        """ Passing placesvisited also in get request so that update does not replace existing choices, but builds
        upon it """
        countries_visited_list = ViewUtils().countries_visited_list(request)
        """ Refreshes map, highlighting countries visited """
        MapCreation().create_base_map(countries_visited_list)
        form = CountriesUpdateForm(instance=request.user.placesvisited)
        """ user needs to have a CitiesVisitedCountry object for each country visited currently selected in 
        any of the drop down menus """
        for visited_country in countries_visited_list:
            visited_country_object = CitiesVisitedCountry.objects.filter(
                user=request.user, country_name=visited_country).first()
            # print(f"existing visited country object: {visited_country_object}")
            if not visited_country_object:
                print(f"visited_country object {visited_country} not existing. creating it. ")
                visited_country_object = CitiesVisitedCountry(user=request.user, country_name=visited_country)
                visited_country_object.save()
        visited_country_objects = CitiesVisitedCountry.objects.filter(
            user=request.user)
        # print(f"countries visited: {countries_visited_list}\n")
        for item in visited_country_objects:
            print(f"item.country_name: {item.country_name}")
            print(f"countries_visited_list: {countries_visited_list}")
            if item.country_name not in countries_visited_list:
                print(f"removing {item.country_name}")
                item.delete()
        """ user CitiesVisited object """
        existing_visited_cities_object = CitiesVisited.objects.filter(user=request.user).first()
        cities_form = CitiesUpdateForm(instance=existing_visited_cities_object)
        # print(cities_form["Afghanistan_cities"])
        cities_variable_name_map = cities_variable_to_name_map()
        # print(cities_variable_name_map)

        return render(request, self.template_name, {'form': form,
                                                    'countries_visited': countries_visited_list,
                                                    "cities_visited_form": cities_form,
                                                    "country_names_map": cities_variable_name_map
                                                    })
