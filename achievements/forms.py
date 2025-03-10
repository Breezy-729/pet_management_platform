# achievements/forms.py
from django import forms
from .models import Achievement

class AchievementForm(forms.ModelForm):
    """AchievementForm（for administrator）"""
    class Meta:
        model = Achievement
        fields = ['name', 'description', 'requirement', 'points',
                 'badge_image', 'category', 'difficulty', 'is_public']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'requirement': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'name': 'Name',
            'description': 'Description',
            'requirement': 'requirement',
            'points': 'Points',
            'badge_image': 'Badge Image',
            'category': 'Category',
            'difficulty': 'Difficulty',
            'is_public': 'Is Public'
        }

    def clean_points(self):
        points = self.cleaned_data.get('points')
        if points < 0:
            raise forms.ValidationError('Points should be not be negative.')
        return points