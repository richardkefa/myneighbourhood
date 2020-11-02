from django.conf.urls import  url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  url(r'^nood/(?P<pk>\d+)/$',views.biz_in_hood,name='home'),  
]

# if settings.DEBUG:
#   static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)