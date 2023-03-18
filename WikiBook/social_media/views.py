from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.urls import reverse

from .forms import *

def index(request):
    return render(request, 'social_media/main.html')

def register(request):
    if request.method == "GET":
        return render(request, 'social_media/register.html', {'form':RegistrationForm()})
    elif request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            form.save()
            login(request,user)
            return redirect(reverse("index"))
