from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'profiles/edit_profile.html'


# class ContactPageView(TemplateView):
#     template_name = 'contacts.html'