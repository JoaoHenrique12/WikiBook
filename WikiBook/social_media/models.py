from django.db import models
from django.contrib.auth.models import User
from .types import states, gender

# Create your models here.

image_help_text = 'Se você tem uma conta no github vá até sua página de perfil, digite ".png" no final da url, copie e cole a url neste campo.'
class Profile(models.Model):
    user = models.OneToOneField(User, models.CASCADE, primary_key=True)

    like_read = models.BooleanField(verbose_name='Gosta de ler', default=False)
    birth = models.DateField(verbose_name='Data de nascimento', null=True, blank=False)

    gender = models.CharField(max_length=1, choices=gender, default='N', verbose_name='Sexo')
    state = models.CharField(max_length=2, choices=states, default='NI', verbose_name='Estado')

    image_link = models.CharField(max_length=200, blank=True, default='', help_text=image_help_text, verbose_name='Imagem do perfil')
    description = models.TextField(max_length=800, blank=True, default='', verbose_name='Descição')

    def __str__(self):
        return self.user.username + ": '"+ self.gender + "'"
