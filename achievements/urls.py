# achievements/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.achievements, name='achievements'),
]