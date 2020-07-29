from django.contrib import admin
from django.urls import path
from .views import (
    VisitedCountriesView,
)

urlpatterns = [
    path('places_visited/', VisitedCountriesView.as_view(), name="places-visited"),
]
