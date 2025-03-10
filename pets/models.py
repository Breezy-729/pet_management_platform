# pets/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Pet(models.Model):
    SPECIES_CHOICES = [
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('rabbit', 'Rabbit'),
        ('hamster', 'Hamster'),
        ('other', 'Other')
    ]
    
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unknown')
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pets')
    name = models.CharField(_('Name'), max_length=50)
    species = models.CharField(_('Species'), max_length=20, choices=SPECIES_CHOICES)
    breed = models.CharField(_('Breed'), max_length=50)
    birthdate = models.DateField(_('Birthdate'))
    gender = models.CharField(_('Gender'), max_length=1, choices=GENDER_CHOICES)
    weight = models.DecimalField(_('Weight(kg)'), max_digits=5, decimal_places=2)
    photo = models.ImageField(_('Photo'), upload_to='pets/', null=True, blank=True)
    description = models.TextField(_('Description'), blank=True)
    created_at = models.DateTimeField(_('reated_at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated_at'), auto_now=True)

    class Meta:
        verbose_name = _('pet')
        verbose_name_plural = _('pet')
        ordering = ['-created_at']

    def __str__(self):
        return self.name