from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import ListProfileView

urlpatterns=[
  url('^newuser/',views.register,name='register'),
  url('^login/',auth_views.LoginView.as_view(template_name='user/login.html'),name='login'),
  url('^logout',auth_views.LogoutView.as_view(template_name='user/logout.html'),name='logout'),
  url('^profiles/',views.profile,name='profile'),
  url('^project/profile$',ListProfileView.as_view(), name='all_profiles'),
  
]

if settings.DEBUG:
  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)