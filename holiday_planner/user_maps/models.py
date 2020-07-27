from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from PIL import Image
from users.models import Profile


class CountryVisited(models.Model):
    """
    CountryVisited is a ManyToOne field to user Profile. Each user profile can have multiple countries visited
    If user gets deleted, it deletes their profile.
    After creating a model, run makemigrations and migrate

    Will be able to access coutries visited with related name specified: user.countries_visited
    """

    user = models.ForeignKey(to=Profile,
                             related_name='countries_visited',
                             on_delete=models.CASCADE)
    country_visited = models.TextField()

    def __str__(self):
        return f"{self.user.country_visited} CoutryVisited"

    def save(self, *args, **kwargs):
        """ Runs after model is saved. Method already exists in parent class, but I'm extending it to add functionality.
         To run parent class method: super().save()
         """

        """ Open instance of the image and resize it to smaller whenever image is updated / saved """
        if len(self.country_visited) > 0:
            self.country_visited = self.country_visited.capitalize()
        super(CountryVisited, self).save(*args, **kwargs)
