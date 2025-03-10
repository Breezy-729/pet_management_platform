# pets/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.pet_management, name='pet_management'),
    path('add/', views.add_pet, name='add_pet'),
    path('<int:pet_id>/', views.pet_profile, name='pet_profile'),
    path('<int:pet_id>/edit/', views.edit_pet, name='edit_pet'),
    path('<int:pet_id>/delete/', views.delete_pet, name='delete_pet'),
]