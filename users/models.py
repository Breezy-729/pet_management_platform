# users/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class UserProfile(models.Model):
    """User Profile Model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    timezone = models.CharField(max_length=50, default='UTC')
    notification_preference = models.CharField(
        max_length=10,
        choices=[
            ('email', 'Email'),
            ('app', 'App')
        ],
        default='app'
    )

    class Meta:
        verbose_name = _('User Profile')
        verbose_name_plural = _('User Profile')

    def __str__(self):
        return f"{self.user.username} profile"