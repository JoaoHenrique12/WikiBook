from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class UserForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'placeholder': 'username'}
    ), label='')

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'password',
        }
    ), label='')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['public_profile', 'like_read', 'gender', 'state', 'birth',
                  'image_link', 'description']

        widgets = {
            'birth': forms.DateInput(attrs={'type': 'date'},
                                     format='%Y-%m-%d'),
        }
