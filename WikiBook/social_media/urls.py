from django.urls import re_path, include

from .views import *

app_name = 'social_media'
urlpatterns = [
    re_path(r'^$',index, name="index"),
    re_path(r'^accounts/',include("django.contrib.auth.urls")),
    re_path(r'^accounts/register',register, name="register"), # type: ignore
]
