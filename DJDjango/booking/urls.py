from django.contrib import admin
from django.urls import path, include
from booking.views import *

app_name = 'booking'

urlpatterns = [
    path('booking/', booking, name='booking'),
]