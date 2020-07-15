from django.contrib import admin
from django.urls import path
from .views import (
    PlansListView,
    PlanDetailView,
    PlanCreateView,
    PlanUpdateView,
    PlanDeleteView,
    PlansWithUserListView,
)
from . import views


# home is empty path
#http://127.0.0.1:8000/upload_section/
#http://127.0.0.1:8000/upload_section/about

""" path('', views.home, name="plans-home"), 
'plan/<int:pk>/'    integer primary key

plan-create and plan-update will use 
"""
urlpatterns = [
    path('', views.home, name='plans-home'),
    path('plans_done/', PlansListView.as_view(), name="plans-done"),
    path('plans_done_with/<str:username>', PlansListView.as_view(), name="plans-with-user"),
    path('plan/<int:pk>/', PlanDetailView.as_view(), name='plan-detail'),
    path('plan/new/', PlanCreateView.as_view(), name='plan-create'),
    path('plan/<int:pk>/update/', PlanUpdateView.as_view(), name='plan-update'),
    path('plan/<int:pk>/delete/', PlanDeleteView.as_view(), name='plan-delete'),
]
