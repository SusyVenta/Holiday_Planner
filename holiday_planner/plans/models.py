from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Plan(models.Model):
    title = models.CharField(max_length=100)
    """ Unrestricted text """
    content = models.TextField()
    """ now = models.DateTimeField(auto_now=True) 
    date_posted = models.DateTimeField(default=timezone.now)
    """
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #
    # def __str__(self):
    #     return self.title
    #
    # def get_absolute_url(self):
    #     return reverse('plan-detail', kwargs={'pk': self.pk})