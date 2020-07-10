from django.contrib import admin
from django.urls import path
# from .views import (
#     PlansListView,
#     PlansWithUserListView,
#     PlanDetailView,
#     PlanCreateView,
#     PlanUpdateView,
#     PlanDeleteView
# )
from . import views

# home is empty path
#http://127.0.0.1:8000/upload_section/
#http://127.0.0.1:8000/upload_section/about

urlpatterns = [
    path('', views.home, name="plans-home"),
    path('plans_done/', views.plans_done, name="plans-done")
]

# urlpatterns = [
#     path('', PlansListView.as_view(), name='blog-home'),
#     path('user/<str:username>', PlansWithUserListView.as_view(), name='user-posts'),
#     path('post/<int:pk>/', PlanDetailView.as_view(), name='post-detail'),
#     path('post/new/', PlanCreateView.as_view(), name='post-create'),
#     path('post/<int:pk>/update/', PlanUpdateView.as_view(), name='post-update'),
#     path('post/<int:pk>/delete/', PlanDeleteView.as_view(), name='post-delete'),
# ]