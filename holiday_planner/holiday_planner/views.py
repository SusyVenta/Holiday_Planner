from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    """ By default django looks at 'plans/templates/plans'"""
    return render(request, 'home.html')



