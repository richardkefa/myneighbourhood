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
  
class Business(models.Model):
  business_name = models.CharField(max_length=200)
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  hood = models.ForeignKey(Neighbourhoods,on_delete=models.CASCADE)
  business_email = models.EmailField()
  description = models.TextField()
  business_img = CloudinaryField('image')
  
  def__str__(self):
    return self.business_name
  
class Posts(models.Model):
  post = models.TextField()
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  hood = models.ForeignKey(Neighbourhoods,on_delete=models.CASCADE)
  
  def__str__(self):
    return self.post
  

