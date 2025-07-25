from rest_framework import serializers
from events.models import Event

from .models import EventPost, EventLike


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id', 'name', 'location', 'location_url', 'description',
            'start_date', 'city',
            'image1', 'image2', 'image3',
        ]



class EventPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventPost
        fields = ['id', 'event', 'user', 'text', 'created_at']
        read_only_fields = ['user', 'created_at']

class EventLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLike
        fields = ['id', 'event', 'user', 'created_at']
        read_only_fields = ['user', 'created_at']