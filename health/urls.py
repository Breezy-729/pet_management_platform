# health/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reminders, name='reminders'),
    path('add/', views.add_reminder, name='add_reminder'),
    path('<int:reminder_id>/edit/', views.edit_reminder, name='edit_reminder'),
]