from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from events.models import Event
from events.choices import StatusChoice  # 🔔 Import your existing choices

class EventParticipation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='participations')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='participations')
    status = models.CharField(max_length=20, choices=StatusChoice.choices)  # 🔔 Reuse StatusChoice

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('event', 'user')  # Prevent duplicate participations

    def __str__(self):
        return f'{self.user} - {self.event} - {self.status}'
