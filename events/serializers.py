from rest_framework import serializers
from events.models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id', 'name', 'location', 'location_url', 'description',
            'start_date', 'city',
            'image1', 'image2', 'image3',
        ]
