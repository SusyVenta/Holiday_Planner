from django.contrib import admin
from django.urls import path
from .views import (
    VisitedCountriesListView,
)

urlpatterns = [
    path('places_visited/', VisitedCountriesListView.as_view(), name="places-visited"),
]
