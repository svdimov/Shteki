from django.contrib.auth import views as auth_views
from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.views import LogoutView, LoginView
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from accounts.forms import AppUserCreationForm, ProfileEditForm, CustomAuthenticationForm
from accounts.models import Profile

UserModel = get_user_model()


class RegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'profiles/register.html'

    # def form_valid(self, form):
    #     self.object = form.save()
    #
    #     return HttpResponseRedirect(self.get_success_url())
    def form_valid(self, form):
        response = super().form_valid(form)
        # Note: Signal for profile creation

        if response.status_code in [301, 302]:
            login(self.request, self.object)

        return response

    def get_success_url(self):
        return reverse('profile-details', kwargs={'pk': self.object.pk})

        # Note: Signal for profile creation


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'profiles/login.html'


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profiles/profile-details.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        # We assume the Profile model has a field named 'user' that links to the UserModel.
        return get_object_or_404(Profile, user__pk=self.kwargs.get('pk'))


class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profiles/edit-profile.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Profile, user=self.request.user)

    def test_func(self):
        return self.request.user.pk == self.kwargs['pk']

    def get_success_url(self) -> str:
        return reverse('profile-details', kwargs={'pk': self.object.pk})



class ProfileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = UserModel
    template_name = 'profiles/delete-profile.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        # This ensures a user can only delete their own account.
        # self.get_object() safely retrieves the user instance from the URL's pk.
        return self.request.user == self.get_object()
