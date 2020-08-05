from django.contrib import admin
from .models import PlacesVisited, CitiesVisitedCountry, CitiesVisited

# need to register the model in order for it to show on the admin page
admin.site.register(PlacesVisited)
admin.site.register(CitiesVisitedCountry)
admin.site.register(CitiesVisited)
