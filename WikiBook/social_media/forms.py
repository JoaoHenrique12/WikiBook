from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile

class UserForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ["username", "email", "password1","password2"]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['public_profile','like_read', 'birth', 'gender', 'state', 'image_link', 'description']

        widgets = {
            'birth': forms.DateInput(attrs={ 'type':'date'}, format='%Y-%m-%d'),
        }
