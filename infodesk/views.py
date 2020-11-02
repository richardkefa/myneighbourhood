from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Neighbourhoods,Business,Posts

def biz_in_hood(requests,hood):
  business = Business.objects.filter(hood=hood)
  return render(request,'infodesk/home.html',{'business'=businesses})