from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic.base import TemplateView



# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'


class AboutAs(TemplateView):
    template_name = 'about.html'



