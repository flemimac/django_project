from django.contrib import admin
from django.urls import path, include
from app.views import *

app_name = 'app'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
]
