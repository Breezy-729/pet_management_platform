# pets/forms.py
from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'species', 'breed', 'birthdate', 'gender', 
                 'weight', 'photo', 'description']
        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'name': 'Pet Name',
            'species': 'Species',
            'breed': 'Breed',
            'birthdate': 'Birthdate',
            'gender': 'Gender',
            'weight': 'Weight(kg)',
            'photo': 'Photo',
            'description': 'Description'
        }

    def clean_weight(self):
        weight = self.cleaned_data.get('weight')
        if weight <= 0:
            raise forms.ValidationError('Weight should larger than 0')
        return weight