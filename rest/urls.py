
from django.urls import path
from .views import PropertyView,UserPropertyListView
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
  path('api/search/',UserPropertyListView.as_view(), name = 'user-projects'),
  path('api/properties/', views.PropertyView.as_view()),
  path('api/properties/<int:pk>', views.PropertyView.as_view()),
  path('api/properties/create', views.PropertyView.as_view('post')), 
  path('api/properties/<int:pk>', views.PropertyView.as_view('delete'))
  
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)