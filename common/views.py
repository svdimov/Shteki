

from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from accounts.models import Profile


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'


class AboutAs(ListView):
    model = Profile
    template_name = 'about.html'
    context_object_name = 'profiles'
    paginate_by = 6
    #
    def get_queryset(self):
        return Profile.objects.select_related('user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_profiles'] = Profile.objects.count()
        return context


