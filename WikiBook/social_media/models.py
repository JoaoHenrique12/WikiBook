from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from .types import states, gender, profile_connectivity

# Create your models here.

image_help_text = 'Se você tem uma conta no github, vá até sua página de perfil, digite ".png" no final da url, copie e cole a url neste campo.'
class Profile(models.Model):
    user = models.OneToOneField(User, models.RESTRICT, primary_key=True)

    public_profile = models.BooleanField(verbose_name="Perfil é público ?", default=True)

    like_read = models.BooleanField(verbose_name='Gosta de ler ?', default=False)
    birth = models.DateField(verbose_name='Data de nascimento', null=True, blank=False)

    gender = models.CharField(max_length=1, choices=gender, default='N', verbose_name='Sexo')
    state = models.CharField(max_length=2, choices=states, default='NI', verbose_name='Estado')

    image_link = models.CharField(max_length=200, blank=True, default='', help_text=image_help_text, verbose_name='Imagem do perfil')
    description = models.TextField(max_length=800, blank=True, default='', verbose_name='Descição')

    articles = models.ManyToManyField('Article', related_name="profiles" , through='ProfileInteractArticle')
    articles_read = models.ManyToManyField('Article',related_name="profiles_read", through='ProfileReadArticle')

    def __str__(self):
        return self.user.username + ": '"+ self.state + "'"

class ProfileConnectProfile(models.Model):
    sender_id = models.ForeignKey(Profile,related_name='sent_connections', on_delete=models.RESTRICT)
    receiver_id = models.ForeignKey(Profile,related_name='received_connections', on_delete=models.RESTRICT)

    sender_status = models.CharField(max_length=1, choices=profile_connectivity, default='U')
    receiver_status = models.CharField(max_length=1, choices=profile_connectivity, default='U')

    class Meta:
        constraints = [
                models.UniqueConstraint(fields=["sender_id", "receiver_id"], name="profile_connect_profile_pk"),
                models.UniqueConstraint(fields=["receiver_id", "sender_id"], name="reverse_profile_connect_profile_pk")
            ]

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, unique=True)
    creation_date = models.DateField()
    number_editions = models.IntegerField()
    number_words = models.BigIntegerField()
    number_subtitles = models.IntegerField()
    number_links = models.IntegerField()
    number_images = models.IntegerField()

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, unique=True)

    articles = models.ManyToManyField('Article')
    sub_categories = models.ManyToManyField('Category')

class ProfileInteractArticle(models.Model):
    profile_id = models.ForeignKey(Profile, on_delete=models.RESTRICT)
    article_id = models.ForeignKey(Article, on_delete=models.RESTRICT)

    is_offensive = models.BooleanField(default=False)
    like = models.BooleanField()
    date_time_acess = models.DateTimeField(default=timezone.now)

    class Meta:
        constraints = [
                models.UniqueConstraint(fields=["profile_id", "article_id"], name="profile_article_pk")
            ]

class ProfileReadArticle(models.Model):
    profile_id = models.ForeignKey(Profile, on_delete=models.RESTRICT)
    article_id = models.ForeignKey(Article, on_delete=models.RESTRICT)

    date_time_acess = models.DateTimeField(default=timezone.now)

    time_read = models.TimeField()
    class Meta:
        constraints = [
                models.UniqueConstraint(fields=["profile_id", "article_id", "date_time_acess"], name="profile_read_article_pk")
            ]
