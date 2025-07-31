from django.urls.base import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from accounts.models import Profile
from django.views.generic import FormView
from django.core.mail import send_mail
from django.conf import settings

from common.forms import ContactForm


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'


class AboutAs(ListView):
    model = Profile
    template_name = 'members.html'
    context_object_name = 'profiles'
    paginate_by = 6
    #
    def get_queryset(self):
        return Profile.objects.select_related('user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_profiles'] = Profile.objects.count()
        return context






class ContactView(FormView):
    template_name = 'contacts/contacts.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact-success')

    def form_valid(self, form):


        send_mail(
            subject=f"Contact form submission from {form.cleaned_data['name']}",
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=[settings.DEFAULT_CONTACT_EMAIL],
            fail_silently=False,
        )

        return super().form_valid(form)


class ContactSuccessView(TemplateView):
    template_name = 'contacts/contact-success.html'