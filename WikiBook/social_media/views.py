from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .forms import *

@login_required()
def index(request):
    return render(request, 'social_media/index.html')

def register(request):
    if request.method == "GET":
        return render(request, 'registration/register.html', {'form':RegistrationForm()})
    elif request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            form.save()
            login(request,user)
            return redirect(reverse("social_media:index"))
        else:
            print(form.errors)
            return render(request, 'registration/register.html', { 'form':RegistrationForm(), 'field_errors':form.errors })