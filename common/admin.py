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
    list_display = ('user', 'event', 'status')
    actions = ['set_status_will_go', 'set_status_maybe', 'set_status_not_going']

    def set_status_will_go(self, request, queryset):
        updated = queryset.update(status=StatusChoice.WILL_GO)
        self.message_user(request, f"{updated} участници бяха маркирани като 'Will go'.")
    set_status_will_go.short_description = "Set status to 'Will go'"

    def set_status_maybe(self, request, queryset):
        updated = queryset.update(status=StatusChoice.MAYBE)
        self.message_user(request, f"{updated} участници бяха маркирани като 'Maybe'.")
    set_status_maybe.short_description = "Set status to 'Maybe'"

    def set_status_not_going(self, request, queryset):
        updated = queryset.update(status=StatusChoice.NOT_GOING)
        self.message_user(request, f"{updated} участници бяха маркирани като 'Not going'.")
    set_status_not_going.short_description = "Set status to 'Not going'"
