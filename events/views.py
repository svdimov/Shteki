import json
from profile import Profile

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query_utils import Q
from accounts.models import Profile
from django.urls.base import reverse_lazy
from django.views.generic.base import TemplateView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.utils import timezone


from common.models import EventParticipation

from events.forms import CreateEventForm, DetailsEventForm
from events.models import Event


class NewEventView(LoginRequiredMixin,TemplateView):
    template_name = 'events/new-events.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = timezone.now().date()

        new_events = Event.objects.filter(start_date__gte=today).order_by('start_date')

        context['new_events'] = new_events

        return context



class PastEventView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'events/past-event.html'
    context_object_name = 'past_events'
    paginate_by = 8  #

    def get_queryset(self):
        today = timezone.now().date()
        queryset = Event.objects.filter(start_date__lt=today).order_by('-start_date')

        query = self.request.GET.get('q', '').strip()
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(location__icontains=query)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '').strip()
        return context

class CreateEventView(CreateView):
    model = Event
    template_name = 'events/create-event.html'
    success_url = reverse_lazy('new-events')
    form_class = CreateEventForm


class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = 'events/events-details.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = self.object

        # All participants who chose "Will go"
        participants = EventParticipation.objects.filter(event=event, status='Will go').select_related('user')

        # Get related profiles (optional optimization)
        profiles = Profile.objects.filter(user__in=[p.user for p in participants])

        context['participants'] = profiles
        context['will_go_count'] = participants.count()

        return context