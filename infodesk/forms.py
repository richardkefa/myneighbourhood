from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Profiles
User = get_user_model()

class UserRegistrationForm(UserCreationForm):
  email = forms.EmailField()
  
  
  class Meta:
    model = User
    fields = ['username','email','password1','password2','first_name','last_name','hood']
    
class UserUpdateForm(forms.ModelForm):
  email = forms.EmailField()
  
  class Meta:
    model = User
    fields =['username','email']
    
class ProfileUpdateForm(forms.ModelForm):
  
  class Meta:
    model = Profiles
    fields =['profile_pic','bio']