from django.conf.urls import  url
from . import views
from .views import PostDetailView,PostCreateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import ListProfileView


urlpatterns = [
  url(r'^hood/$',views.biz_in_hood,name='home'), 
  url(r'^hood_details/(?P<pk>\d+)/$',PostDetailView.as_view(),name='hood_details'),
  url(r'^post/new/',PostCreateView.as_view(),name='new_post'),
  url(r'^post/(?P<hood>\d+)/$',views.hood_posts,name='post'),
  url('^newuser/',views.register,name='register'),
  url('^login/',auth_views.LoginView.as_view(template_name='infodesk/login.html'),name='login'),
  url('^logout',auth_views.LogoutView.as_view(template_name='infodesk/logout.html'),name='logout'),
  url('^profiles/',views.profile,name='profile'),
  url('^project/profile$',ListProfileView.as_view(), name='all_profiles'),  
 
]

if settings.DEBUG:
  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)