from django.urls import path, include
from .views import stockPicker, stockTracker

urlpatterns = [
    path('', stockPicker, name='stockpicker'),
    path('stocktracker/', stockTracker, name='stocktracker'),
]