import os
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
import folium
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from IPython.display import HTML, display
from django.utils.decorators import method_decorator
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from django.contrib.auth.models import User
from friendship.models import Friend, Follow, Block
from .models import Plan
from holiday_planner.settings import BASE_DIR

""" Fake data for plans """
plans = [
    {
        "author": "Susanna",
        "title": "First plan",
        "content": "plan for holidays 1 test",
        "date_posted": "July 10th, 2020"
    },
    {
        "author": "Merav",
        "title": "Plan #2",
        "content": "plan for holidays 2 test",
        "date_posted": "July 12th, 2020"
    }
]

""" By default django looks at 'plans/templates/plans'"""


def home(request):
    """ Passing user friends as context """
    if request.user.is_authenticated:
        friends = Friend.objects.friends(request.user)
        print(friends)
        return render(request, 'plans/home.html', context={"friends": friends})
    return render(request, 'plans/home.html')


# class homeMapView(TemplateView):
#     template_name = "plans/home.html"
#
#     def get_color(self, country_data, countries_list):
#         """
#         function which returns color of the map.
#         if name of chosen country is equal to the country name from json file it returns red colour
#         for that country, if not it returns blue"""
#
#         for x in countries_list:
#             if x in country_data['properties']['NAME']:
#                 return 'red'
#         else:
#             return 'blue'
#
#     def get_context_data(self, **kwargs):
#         # m = folium.Map([51.5, -0.25], zoom_start=10)
#         # m.save("map.html")
#         # return {'my_map': m._repr_html_()}
#         my_map = folium.Map(location=None, tiles='Mapbox Bright', no_wrap=True, width=500, height=300)
#
#         # creating and adding a features to the map
#
#         gj = folium.GeoJson(
#             data=open(os.path.join(BASE_DIR, "plans", "static", "plans", "world.json"), "r",
#                       encoding="utf-8-sig").read(),
#             style_function=lambda country_data: {
#                 'fillColor': '#00eb9c',  # self.get_color(country_data, countries_list),
#                 'fillOpacity': 0.5,
#                 'color': 'black',
#                 'line_opacity': 0.5,
#                 'weight': 1
#             })
#         gj.add_to(my_map)
#         context = my_map.get_root().render()
#         return {'my_map': context}



# def plans_done(request):
#     # to get dummy objects: "plans": plans
#     context = {
#         "plans": Plan.objects.all()
#     }
#     return render(request, 'plans/plans_done.html', context=context)

class PlansListView(LoginRequiredMixin, ListView):
    model = Plan
    template_name = 'plans/plans_done.html'
    context_object_name = 'plans'
    # """ Newest to oldest """
    # ordering = ['-date_posted']
    paginate_by = 3

    def get_queryset(self):
        """
        I want to display only plans created by the user:
         option 1: user = get_object_or_404(User, username=self.request.user) """
        user = get_object_or_404(User, username=self.request.user)
        return Plan.objects.filter(author=user).order_by('-date_posted')


class PlanDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """ To display single plan details.
     By default it looks for a template in: <app>/<model>_<viewtype>.html - plans/templates/plans/plan_detail.html"""
    model = Plan

    def test_func(self):
        plan = self.get_object()
        if self.request.user == plan.author:
            return True
        return False


class PlansWithUserListView(ListView):
    model = Plan
    template_name = 'plans/plans_with_user.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Plan.objects.filter(author=user).order_by('-date_posted')


class PlanCreateView(LoginRequiredMixin, CreateView):
    """ By default it uses plans/templates/plans/plan_form.html"""
    model = Plan
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PlanUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ UserPassesTestMixin runs test_func, to make sure they're editing a plan they created """
    model = Plan
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        plan = self.get_object()
        if self.request.user == plan.author:
            return True
        return False


class PlanDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ default template: plans/templates/plans/post_confirm_delete.html"""
    model = Plan
    """ On success delete, it redirects to the home page """
    success_url = '/'

    def test_func(self):
        plan = self.get_object()
        if self.request.user == plan.author:
            return True
        return False
