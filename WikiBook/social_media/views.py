from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy

from django.views.generic.edit import CreateView

from .forms import *
from .models import *
from .utils_views import *

@login_required
def password_change_done(request):
    return render(request, 'registration/password_change_done.html', { 'information_updated': True })

@login_required()
def index(request):
    return render(request, 'social_media/index.html')

class RegisterView(CreateView):
    form_class = UserForm
    model = User

    template_name = 'registration/register.html'
    success_url = reverse_lazy("social_media:index")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
    
    def form_invalid(self, form):
        return render(self.request, self.template_name, { 'form': UserForm(), 'field_errors': form.errors })

@login_required
def profile(request, user_id):
    image_link = get_image_or_default()
    if request.method == "GET":
        profile = get_object_or_404(Profile, pk=user_id)
        form = ProfileForm(instance=profile)
        image_link = get_image_or_default(profile.image_link, profile.gender)
        return render(request, 'social_media/profile.html', { 'form': form, 'image_link': image_link})
    else :
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user_id = request.user.id
            profile.save()
            image_link = get_image_or_default(profile.image_link, profile.gender)
            return render(request, 'social_media/profile.html', { 'form': form ,'image_link': image_link, 'information_updated': True })

        return render(request, 'social_media/profile.html', { 'form': form ,'image_link': image_link ,'field_errors': form.errors })
