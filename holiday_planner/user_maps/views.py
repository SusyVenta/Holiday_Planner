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
from .select_countries_and_cities import select_cities_options
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
        if form.is_valid():
            """ Get selected country (value tag), if any from element with name tag == 'selected-country """
            selected_country = request.POST.get('selected-country', False)
            if selected_country:
                # country_related_object = CitiesVisitedCountry.objects.filter(
                #     user=request.user, country_name=selected_country).first()
                # city_form = CitiesUpdateForm(instance=country_related_object)
                # print(str(request.user.placesvisited.north_american_countries).split(","))
                return render(request, self.template_name, {'form': form})
                # self.get(request=request, city_form=city_form, form_in=form, selected_country=selected_country)
            else:
                form.save()
                return HttpResponseRedirect("/places_visited")
        else:
            return render(request, self.template_name, {'form': form})

    def get(self, request, selected_country=None, city_form=None, form_in=None, *args):
        """ Passing placesvisited also in get request so that update does not replace existing choices, but builds
        upon it """
        countries_visited_list = ViewUtils().countries_visited_list(request)
        """ Refreshes map, highlighting countries visited """
        MapCreation().create_base_map(countries_visited_list)
        if not form_in:
            form = CountriesUpdateForm(instance=request.user.placesvisited)
        else:
            form = form_in
        print(f"countries visited: {countries_visited_list}\n")

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
        for item in visited_country_objects:
            if item.country_name not in countries_visited_list:
                print(f"removing {item.country_name}")
                item.delete()
        """ user CitiesVisited object """
        existing_visited_cities_object = CitiesVisited.objects.filter(user=request.user).first()
        print(existing_visited_cities_object.Afghanistan_cities.choices)

        return render(request, self.template_name, {'form': form,
                                                    'countries_visited': visited_country_objects,
                                                    "cities_visited_form": CitiesUpdateForm(
                                                        instance=existing_visited_cities_object)
                                                    })


