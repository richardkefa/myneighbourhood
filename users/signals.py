from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from .models import Profiles,Contact_info

@receiver(post_save, sender=User)
def create_profile(sender,instance,created,**kwargs):
  if created:
    Profiles.objects.create(user=instance)
    
@receiver(post_save, sender=User)
def save_profile(sender,instance,**kwargs):
  try:
    instance.profiles.save()
  except ObjectDoesNotExist:
    Profiles.objects.create(user=instance)
