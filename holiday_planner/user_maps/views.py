import os
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
import folium
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from IPython.display import HTML, display
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from django.contrib.auth.models import User
from friendship.models import Friend
from .models import CountryVisited
from user_maps.maps_creation import MapCreation
from .forms import CountriesChoice
from .maps_creation import MapCreation

class VisitedCountriesListView(LoginRequiredMixin, ListView):
    model = CountryVisited
    template_name = 'user_maps/visited_places.html'
    context_object_name = 'user_maps'

    def post(self, request, *args, **kwargs):
        form = CountriesChoice(request.POST)
        if form.is_valid():
            europe = form.cleaned_data.get("Europe")
            asia = form.cleaned_data.get("Asia")
            africa = form.cleaned_data.get("Africa")
            oceania = form.cleaned_data.get("Oceania")
            antarctica = form.cleaned_data.get("Antarctica")
            north_america = form.cleaned_data.get("North_America")
            south_america = form.cleaned_data.get("South_America")

            countries_list = europe+africa+oceania+antarctica+north_america+south_america+asia
            maps_as_string = MapCreation().create_base_map(countries_list)

            # my_map_object = CountriesChoice(id=1, html_string=maps_as_string)
            # my_map_object.save()

            return HttpResponseRedirect("/places_visited")

    def get(self, request, *args):
        form = CountriesChoice
        return render(request, self.template_name, {'form': form})

    # def get_queryset(self):
    #     """
    #     I want to display only plans created by the user:
    #      option 1: user = get_object_or_404(User, username=self.request.user) """
    #     user = get_object_or_404(User, username=self.request.user)
    #     return Plan.objects.filter(author=user).order_by('-date_posted')


# class PlanDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
#     """ To display single plan details.
#      By default it looks for a template in: <app>/<model>_<viewtype>.html - plans/templates/plans/plan_detail.html"""
#     model = Plan
#
#     def test_func(self):
#         plan = self.get_object()
#         if self.request.user == plan.author:
#             return True
#         return False
#
#
# class PlansWithUserListView(ListView):
#     model = Plan
#     template_name = 'plans/plans_with_user.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'posts'
#     paginate_by = 3
#
#     def get_queryset(self):
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         return Plan.objects.filter(author=user).order_by('-date_posted')
#
#
# class PlanCreateView(LoginRequiredMixin, CreateView):
#     """ By default it uses plans/templates/plans/plan_form.html"""
#     model = Plan
#     fields = ['title', 'content']
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
#
#
# class PlanUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     """ UserPassesTestMixin runs test_func, to make sure they're editing a plan they created """
#     model = Plan
#     fields = ['title', 'content']
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
#
#     def test_func(self):
#         plan = self.get_object()
#         if self.request.user == plan.author:
#             return True
#         return False
#
#
# class PlanDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     """ default template: plans/templates/plans/post_confirm_delete.html"""
#     model = Plan
#     """ On success delete, it redirects to the home page """
#     success_url = '/'
#
#     def test_func(self):
#         plan = self.get_object()
#         if self.request.user == plan.author:
#             return True
#         return False
