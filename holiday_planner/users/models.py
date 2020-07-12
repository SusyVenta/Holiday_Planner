from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.conf import settings


class Profile(models.Model):
    """
    Extending user profile to have additional attribute profile picture
    If user gets deleted, it deletes their profile.
    After creating a model, run makemigrations and migrate

    To view profile details from shell:

    py -3.6 manage.py shell
    from django.contrib.auth.models import User
    user = User.objects.filter(username="susanna").first()
    user.profile.image.width
    exit()
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to=settings.MEDIA_ROOT)

    def __str__(self):
        return f"{self.user.username} Profile"
