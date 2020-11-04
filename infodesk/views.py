from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Neighbourhoods,Business,Posts,User,public_amenities
from django.views.generic import DetailView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

def biz_in_hood(request):
  business = Business.objects.all()
  amenities = public_amenities.objects.all()
  return render(request,'infodesk/home.html',{'businesses':business,'amenities':amenities})

class PostDetailView(DetailView):
  model = Neighbourhoods
  template_name = 'infodesk/hood_details.html'
  context_object_name = 'hood'
  
class PostCreateView(CreateView):
  model = Posts
  fields = ['post']
  
  def form_valid(self,form):
    form.instance.user = self.request.user
    form.instance.hood = self.request.user.hood
    return super().form_valid(form)

def hood_posts(request,hood):
  posts = Posts.objects.filter(hood=hood)
  return render(request,'infodesk/post_form',{'posts':posts})

  
  

from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegistrationForm,UserUpdateForm,ProfileUpdateForm
from cloudinary.models import CloudinaryField
from rest_framework import generics
from .models import Profiles
from .serializers import ProfileSerializer

def register(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request,f'Your account has been created successfuly')
      return redirect('login')
  else:
    form = UserRegistrationForm()
    
  return render(request,'infodesk/register.html',{"form":form})

def profile(request):
  if request.method == 'POST':
    u_form = UserUpdateForm(request.POST,instance=request.user)
    p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profiles)
    
    if u_form.is_valid() and p_form.is_valid():
      u_form.save()
      p_form.save()
      
      messages.success(request,f'Profile updated successfuly')
      return redirect('profile')
  else:
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profiles)
  context ={
    "u_form":u_form,
    "p_form":p_form,
  }
  
  return render(request,'infodesk/profile.html',context)

  
class ListProfileView(generics.ListAPIView):
  """
  Provides a get method
  """
  queryset = Profiles.objects.all()
  serializer_class = Profiles
