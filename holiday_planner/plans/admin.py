from django.contrib import admin
from .models import Plan

# need to register the model in order for it to show on the admin page
admin.site.register(Plan)
