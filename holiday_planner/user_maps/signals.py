from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import PlacesVisited, CitiesVisited


@receiver(post_save, sender=User)
def create_places_visited(sender, instance, created, **kwargs):
    """ Whenever a user is saved, a signal is sent to the receiver (receiver= create places visited model) """
    if created:
        PlacesVisited.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_places_visited(sender, instance, **kwargs):
    """ Save places visited whenever there is a new submission """
    instance.placesvisited.save()

@receiver(post_save, sender=User)
def create_cities_visited(sender, instance, created, **kwargs):
    """ Whenever a user is saved, a signal is sent to the receiver (receiver= create places visited model) """
    if created:
        CitiesVisited.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_cities_visited(sender, instance, **kwargs):
    """ Save places visited whenever there is a new submission """
    instance.citiesvisited.save()


@receiver(post_save, sender=User)
def create_places_to_visit(sender, instance, created, **kwargs):
    """ Whenever a user is saved, a signal is sent to the receiver (receiver= create places to visit model) """
    if created:
        PlacesVisited.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_places_to_visit(sender, instance, **kwargs):
    """ Save places visited whenever there is a new submission """
    instance.placestovisit.save()




