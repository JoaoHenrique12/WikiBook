from django.urls import re_path, include, reverse_lazy
from django.contrib.auth.views import PasswordChangeView

from .views import *

app_name = 'social_media'
urlpatterns = [
    re_path(r'^$', index, name="index"),
    re_path(r'profile/(?P<user_id>\d+)/', ProfileUpdateView.as_view(), name="profile"),

    re_path(r'^accounts/',include("django.contrib.auth.urls")),
    re_path(r'^accounts/register', RegisterView.as_view(), name="register"), # type: ignore
    re_path(r'^accounts/password_change/done', password_change_done, name="password_change_done"), # type: ignore
    re_path(r'^accounts/password_change', PasswordChangeView.as_view(success_url=reverse_lazy('social_media:password_change_done')), name="password_change"), # type: ignore
]
