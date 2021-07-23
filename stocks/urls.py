from django.urls import path, include
from .views import stockPicker

urlpatterns = [
    path('', stockPicker, name='stocktracker'),
]