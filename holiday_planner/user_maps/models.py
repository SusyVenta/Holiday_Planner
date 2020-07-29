from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from PIL import Image
from users.models import Profile
from .select_countries_and_cities import select_countries_options
import json
from multiselectfield import MultiSelectField


class PlacesVisited(models.Model):
    """
    Model to populate drop-down menus with places visited.
    to see places visited by user: request.user.placesvisited.countries
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    asian_countries_choices = select_countries_options("Asia")
    european_countries_choices = select_countries_options("Europe")
    african_countries_choices = select_countries_options("Africa")
    antarctic_countries_choices = select_countries_options("Antarctica")
    oceania_countries_choices = select_countries_options("Oceania")
    south_america_countries_choices = select_countries_options("South America")
    north_america_countries_choices = select_countries_options("North America")

    asian_countries = MultiSelectField(choices=asian_countries_choices, null=True, blank=True)
    european_countries = MultiSelectField(choices=european_countries_choices, null=True, blank=True)
    african_countries = MultiSelectField(choices=african_countries_choices, null=True, blank=True)
    antarctic_countries = MultiSelectField(choices=antarctic_countries_choices, null=True, blank=True)
    oceania_countries = MultiSelectField(choices=oceania_countries_choices, null=True, blank=True)
    south_american_countries = MultiSelectField(choices=south_america_countries_choices, null=True, blank=True)
    north_american_countries = MultiSelectField(choices=north_america_countries_choices, null=True, blank=True)

    def __str__(self):
        return f"{self.user} visited_places"


# class PlacesToVisit(models.Model):
#     """
#     Each user will have, associated to them:
#     - a json containing the countries they want to visit
#     - a json containing the cities they want to visit
#
#     to see places the user wants to visit: request.user.placestovisit.countries
#     """
#
#     user = models.OneToOneField(to=User, on_delete=models.CASCADE)
#     countries = models.TextField()
#     cities = models.TextField()
#
#     def set_countries_list_to_json(self, x):
#         self.foo = json.dumps(x)
#
#     def get_countries_list_from_json(self, x):
#         return json.loads(self.foo)
#
#     def __str__(self):
#         return f"{self.user.username} PlacesToVisit"
