import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query_utils import Q
from django.http.response import JsonResponse
from django.urls.base import reverse_lazy
from django.views.generic.base import TemplateView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.utils import timezone

from events.choices import StatusChoice
from events.froms import CreateEventForm, DetailsEventForm
from events.models import Event


class NewEventView(LoginRequiredMixin,TemplateView):
    template_name = 'events/new-events.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = timezone.now().date()

        new_events = Event.objects.filter(start_date__gte=today).order_by('start_date')

        context['new_events'] = new_events

        return context


# class PastEventView(LoginRequiredMixin,TemplateView):
#     template_name = 'events/past-event.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         today = timezone.now().date()
#         query = self.request.GET.get('q')
#
#
#         past_events = Event.objects.filter(start_date__lt=today).order_by('-start_date')
#
#         if query is not None and query.strip() != '':
#             query = query.strip()
#             past_events = past_events.filter(
#                 Q(name__icontains=query) | Q(location__icontains=query)
#             )
#
#
#         context['past_events'] = past_events
#         context['query'] = query or ''
#
#         return context
class PastEventView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'events/past-event.html'
    context_object_name = 'past_events'
    paginate_by = 6  #

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


class EventDetailView(LoginRequiredMixin,DetailView):
    model = Event
    form_class = DetailsEventForm
    template_name = 'events/events-details.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event'] = self.object
        return context

# class UpdateEventStatusView(LoginRequiredMixin, View):
#     def post(self, request, pk):
#         event = Event.objects.get(pk=pk)
#         data = json.loads(request.body)
#         status = data.get('status')
#
#         if status in StatusChoice.values:
#             event.status = status
#             event.save()
#             return JsonResponse({'success': True})
#         return JsonResponse({'success': False, 'error': 'Invalid status'}, status=400)
