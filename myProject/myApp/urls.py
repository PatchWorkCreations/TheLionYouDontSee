from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name='index'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('contact/', views.contact, name='contact'),
   path('get-response/', views.get_response, name='get_response'),
    
]