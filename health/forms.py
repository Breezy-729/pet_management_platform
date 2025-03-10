# health/forms.py
from django import forms
from .models import HealthRecord
from pets.models import Pet

class HealthRecordForm(forms.ModelForm):
    class Meta:
        model = HealthRecord
        fields = ['pet', 'record_type', 'record_date', 'status', 'weight',
                 'temperature', 'symptoms', 'diagnosis', 'treatment',
                 'next_visit_date', 'vet_name', 'clinic_name', 'notes']
        widgets = {
            'record_date': forms.DateInput(attrs={'type': 'date'}),
            'next_visit_date': forms.DateInput(attrs={'type': 'date'}),
            'symptoms': forms.Textarea(attrs={'rows': 3}),
            'diagnosis': forms.Textarea(attrs={'rows': 3}),
            'treatment': forms.Textarea(attrs={'rows': 3}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'pet': 'pet',
            'record_type': 'Record Type',
            'record_date': 'Record Date',
            'status': 'Status',
            'weight': 'Weight (kg)',
            'temperature': 'Temperature (℃)',
            'symptoms': 'Symptoms',
            'diagnosis': 'Diagnosis',
            'treatment': 'Treatment',
            'next_visit_date': 'Next Visit Date',
            'vet_name': 'Veterinarian',
            'clinic_name': 'Clinic',
            'notes': 'notes'
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.warnings = {}
        if user:
            self.fields['pet'].queryset = Pet.objects.filter(owner=user)

    def clean(self):
        cleaned_data = super().clean()
        weight = cleaned_data.get('weight')
        temperature = cleaned_data.get('temperature')
        
        if weight and weight <= 0:
            self.add_error('weight', 'Weight should be larger than 0')
            
        if temperature and (temperature < 35 or temperature > 43):
            self.warnings['temperature'] = 'Abnormal temperature, please confirm.'
            #self.add_error('temperature', 'Abnormal temperature, please confirm.')

        return cleaned_data