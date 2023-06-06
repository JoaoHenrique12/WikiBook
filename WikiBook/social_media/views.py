from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from .forms import ProfileForm, UserForm
from .models import Profile, User
from .utils_views import get_image_or_default, get_profiles_with_images


@login_required
def password_change_done(request):
    return render(request, 'registration/password_change_done.html',
                  {'information_updated': True})


@login_required()
def index(request):
    return render(request, 'social_media/index.html')


@login_required
def search_user(request):
    found_profiles = Profile.objects.all()

    profiles_with_images = get_profiles_with_images(found_profiles)
    return render(request, 'social_media/search_user.html',
                  {'found_profiles': profiles_with_images})


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
        return render(self.request, self.template_name,
                      {'form': UserForm(), 'field_errors': form.errors})


# LoginRequiredMixin, must be the first class in inheritance.
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'social_media/profile.html'

    def get_success_url(self):
        return reverse_lazy('social_media:profile',
                            kwargs={'user_id': self.object.user_id})

    def get_object(self):
        user_id = self.kwargs.get('user_id')
        if user_id != str(self.request.user.id):
            user_id = self.request.user.id
        return get_object_or_404(Profile, pk=user_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        image_link = get_image_or_default(
            self.object.image_link, self.object.gender)
        context['image_link'] = image_link
        return context

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user_id = self.request.user.id
        profile.save()
        return self.render_to_response(
            self.get_context_data(form=form, information_updated=True))

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form, field_errors=form.errors))
