from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 
from cloudinary.models import CloudinaryField


class Neighbourhoods(models.Model):
  hood_name = models.CharField(max_length=100)
  hood_location = models.CharField(max_length=100)
  occupant_count = models.IntegerField()
  
  def __str__(self):
    return self.hood_name