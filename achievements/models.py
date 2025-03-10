# achievements/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Achievement(models.Model):
    name = models.CharField(_('achievement name'), max_length=100)
    description = models.TextField(_('description'))
    requirement = models.TextField(_('requirement'))
    points = models.IntegerField(_('points'))
    badge_image = models.ImageField(_('badge image'), upload_to='badges/')
    category = models.CharField(_('category'), max_length=50)
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)

    class Meta:
        verbose_name = _('Achievement')
        verbose_name_plural = _('Achievements')

    def __str__(self):
        return self.name

class UserAchievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='achievements')
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    achieved_date = models.DateTimeField(_('achieved_date'), auto_now_add=True)

    class Meta:
        verbose_name = _('User Achievement')
        verbose_name_plural = _('User Achievements')
        unique_together = ['user', 'achievement']

    def __str__(self):
        return f"{self.user.username}'s {self.achievement.name}"