from django.db import models
from django.contrib.auth.models import User
from .types import states, gender

# Create your models here.

image_help_text = 'If you have an github account go to your profile, type .png at end of url, then copy and paste that url in this field.'
class Profile(models.Model):
    user = models.OneToOneField(User, models.CASCADE, primary_key=True)

    like_read = models.BooleanField()
    birth = models.DateField()

    gender = models.CharField(max_length=1, choices=gender, default='N', blank=True)
    state = models.CharField(max_length=2, choices=states, default='??', blank=True)

    image_link = models.CharField(max_length=200, blank=True, null=True, help_text=image_help_text, verbose_name='Profile image link')
    description = models.TextField(max_length=800, blank=True, default='No information given.')

    def __str__(self):
        return self.user.username + ": '"+ self.description + "'"