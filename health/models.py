# health/models.py
from django.db import models
from django.utils.translation import gettext_lazy as _
from pets.models import Pet

class HealthRecord(models.Model):
    RECORD_TYPES = [
        ('vaccine', 'Vaccine'),
        ('checkup', 'Checkup'),
        ('treatment', 'Treatment'),
        ('routine', 'Routine')
    ]
    
    HEALTH_STATUS = [
        ('healthy', 'Healthy'),
        ('sick', 'Sick'),
        ('recovering', 'Recovering'),
        ('critical', 'Critical')
    ]

    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='health_records')
    record_type = models.CharField(_('record type'), max_length=20, choices=RECORD_TYPES)
    record_date = models.DateField(_('record date'))
    status = models.CharField(_('status'), max_length=20, choices=HEALTH_STATUS)
    weight = models.DecimalField(_('weight(kg)'), max_digits=5, decimal_places=2)
    temperature = models.DecimalField(_('temperature(℃)'), max_digits=4, decimal_places=1)
    symptoms = models.TextField(_('symptoms'), blank=True)
    diagnosis = models.TextField(_('diagnosis'), blank=True)
    treatment = models.TextField(_('treatment'), blank=True)
    next_visit_date = models.DateField(_('next visit date'), null=True, blank=True)
    vet_name = models.CharField(_('vet name'), max_length=100)
    clinic_name = models.CharField(_('clinic name'), max_length=200)
    notes = models.TextField(_('notes'), blank=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('health record')
        verbose_name_plural = _('health record')
        ordering = ['-record_date']

    def __str__(self):
        return f"{self.pet.name}'s {self.get_record_type_display()}"