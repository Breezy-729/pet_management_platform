# pet_management/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path('', include('users.urls')),
    path('pets/', include('pets.urls')),
    path('health/', include('health.urls')),
    path('achievements/', include('achievements.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)