from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .forms import *
from .models import *

@login_required()
def index(request):
    return render(request, 'social_media/index.html')

def register(request):
    if request.method == "GET":
        return render(request, 'registration/register.html', {'form':RegistrationForm()})

    form = RegistrationForm(request.POST)
    if form.is_valid():
        user = form.save()
        Profile.objects.create(user_id=user.id).save()
        form.save()
        login(request,user)
        return redirect(reverse("social_media:index"))
    else:
        return render(request, 'registration/register.html', { 'form': RegistrationForm(), 'field_errors': form.errors })

@login_required
def profile(request, user_id):

    if request.method == "GET":
        profile = get_object_or_404(Profile, pk=user_id)
        form = ProfileForm(instance=profile)
        return render(request, 'social_media/profile.html', { 'form': form })
    else :
        form = ProfileForm(request.POST)
        if form.is_valid():
            social_media_profile = form.save(commit=False)
            social_media_profile.user_id = request.user.id
            social_media_profile.save()
            return render(request, 'social_media/profile.html', { 'form': form , 'information_updated': True })

        return render(request, 'social_media/profile.html', { 'form': form , 'field_errors': form.errors })
