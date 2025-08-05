from django.contrib import admin
from django.contrib import admin
from .models import EventParticipation, StatusChoice
from common.models import EventParticipation


# # Register your models here.
# @admin.register(EventParticipation)
# class EventParticipationAdmin(admin.ModelAdmin):
#     pass



@admin.register(EventParticipation)
class EventParticipationAdmin(admin.ModelAdmin):
    pass
