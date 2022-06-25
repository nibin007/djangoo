from unicodedata import name
from django.urls import path
from .views import *
urlpatterns=[
    path('emails/',mail,name='em'),
    path('flup/',flup,name='flup'),
    
]