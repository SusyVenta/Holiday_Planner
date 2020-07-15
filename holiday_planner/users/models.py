from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from PIL import Image


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

    def save(self):
        """ Runs after model is saved. Method already exists in parent class, but I'm extendign it to add functionality.
         To run parent class method: super().save()
         When saving I also want to remove user's old image
         """
        super().save()
        """ Open instance of the image and resize it to smaller whenever image is updated / saved """
        image = Image.open(self.image.path)
        if image.height > 300 or image.width > 300:
            output_size = (300, 300)
            image.thumbnail(output_size)
            image.save(self.image.path)
