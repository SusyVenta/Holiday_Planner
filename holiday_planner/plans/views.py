from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Plan

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
    return render(request, 'plans/home.html')


def plans_done(request):
    context = {
        "plans": plans
    }
    return render(request, 'plans/plans_done.html', context=context)


# class PlansListView(ListView):
#     model = Plan
#     template_name = 'plans/plans_done.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'plans'
#     ordering = ['-date_posted']
#     paginate_by = 5
#
#
# class PlansWithUserListView(ListView):
#     model = Plan
#     template_name = 'plans/plans_with_user.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'posts'
#     paginate_by = 5
#
#     def get_queryset(self):
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         return Plan.objects.filter(author=user).order_by('-date_posted')
#
#
# class PlanDetailView(DetailView):
#     model = Plan
#
#
# class PlanCreateView(LoginRequiredMixin, CreateView):
#     model = Plan
#     fields = ['title', 'content']
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
#
#
# class PlanUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Plan
#     fields = ['title', 'content']
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
#
#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False
#
#
# class PlanDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Plan
#     success_url = '/'
#
#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False




