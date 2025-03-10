# users/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class UserRegisterForm(UserCreationForm):
    email = forms.CharField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        
        self.fields['username'].label = 'Username'
        self.fields['email'].label = 'Email'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'SurePassword'

class UserUpdateForm(forms.ModelForm):
    email = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        labels = {
            'username': 'Username',
            'email': 'Email',
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'timezone', 'notification_preference']
        labels = {
            'avatar': 'Avatar',
            'timezone': 'Timezone',
            'notification_preference': 'Notification Preference'
        }