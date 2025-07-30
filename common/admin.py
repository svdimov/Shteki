from django.contrib import admin

from common.models import EventParticipation


# Register your models here.
@admin.register(EventParticipation)
class EventParticipationAdmin(admin.ModelAdmin):
    pass