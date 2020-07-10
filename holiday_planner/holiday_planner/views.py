from django.shortcuts import render
from django.http import HttpResponse

""" By default django looks at 'plans/templates/plans'"""
def home(request):
    return render(request, 'home.html')



