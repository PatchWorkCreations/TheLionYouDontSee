from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name='index'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('contact/', views.contact, name='contact'),
    path('get-response/', views.get_response, name='get_response'),
    path('support/', views.support, name='support'), 
    path("christmaslion/", views.christmaslion_index, name="christmaslion_index"),
    path("christmaslion/support/", views.christmaslion_support, name="christmaslion_support"),
    path('christmaslion/thank-you/', views.thank_you, name='thank_you'),
    path('thelionyoudontsee/thank-you/', views.thankyou, name='thank_you'),
]