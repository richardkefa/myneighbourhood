from django.db import models
from django.urls import reverse 
from cloudinary.models import CloudinaryField
from django.conf import settings



class Neighbourhoods(models.Model):
  hood_name = models.CharField(max_length=100)
  hood_location = models.CharField(max_length=100)
  occupant_count = models.IntegerField()
  
  def __str__(self):
    return self.hood_name
  
class Business(models.Model):
  business_name = models.CharField(max_length=200)
  hood = models.ForeignKey(Neighbourhoods,on_delete=models.CASCADE)
  business_email = models.EmailField()
  description = models.TextField()
  business_img = CloudinaryField('image')
  
  def __str__(self):
    return self.business_name
  
class Posts(models.Model):
  post = models.TextField()
  hood = models.ForeignKey(Neighbourhoods,on_delete=models.CASCADE)
  post_date = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.post
  
  def get_absolute_url(self):
    return reverse('post',kwargs={'hood':self.hood})
  
class public_amenities(models.Model):
  amenity_name = models.CharField(max_length=200)
  tel_number = models.IntegerField()
  location = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  email = models.EmailField()
  hood = models.ForeignKey(Neighbourhoods,on_delete=models.CASCADE)
  
  def __str__(self):
    return self.amenity_name
  
  
  
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from cloudinary.models import CloudinaryField

class Profiles(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
  bio = models.TextField()
  profile_pic = CloudinaryField('image')
  hood = models.OneToOneField(Neighbourhoods,on_delete=models.CASCADE)
  
  def __str__(self):
    return bio
  

  
class User(AbstractUser):
  hood = models.ForeignKey(Neighbourhoods,on_delete=models.CASCADE,default='1')
