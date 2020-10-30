from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Profiles(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  bio = models.TextField()
  profile_pic = CloudinaryField('image')
  
  def __str__(self):
    return bio