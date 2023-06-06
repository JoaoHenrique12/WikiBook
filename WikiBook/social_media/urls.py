from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import include, re_path, reverse_lazy

from .forms import UserLoginForm
from .views import (ProfileUpdateView, RegisterView, index,
                    password_change_done, search_user)

app_name = 'social_media'
urlpatterns = [
    re_path(r'^$', index, name="index"),

    re_path(r'^search_user/$', search_user, name="search_user"),

    re_path(r'profile/(?P<user_id>\d+)/',
            ProfileUpdateView.as_view(), name="profile"),

    re_path(r'^accounts/login', LoginView.as_view(
        authentication_form=UserLoginForm
    ),
        name="login"),

    re_path(r'^accounts/', include("django.contrib.auth.urls")),

    re_path(r'^accounts/register', RegisterView.as_view(),
            name="register"),

    re_path(r'^accounts/password_change/done', password_change_done,
            name="password_change_done"),

    re_path(r'^accounts/password_change', PasswordChangeView.as_view(
        success_url=reverse_lazy('social_media:password_change_done')),
        name="password_change"),
]
