from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django.utils import timezone
from django.db.models import Q
from events.serializers import EventSerializer
from rest_framework import generics, permissions, status
from .models import EventPost, EventLike, Event
from .serializers import EventPostSerializer, EventLikeSerializer
from django.shortcuts import get_object_or_404



class PastEventsAPIPagination(PageNumberPagination):
    page_size = 8

class PastEventsAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        today = timezone.now().date()
        queryset = Event.objects.filter(start_date__lt=today).order_by('-start_date')

        query = request.GET.get('q', '').strip()
        if query:
            queryset = queryset.filter(Q(name__icontains=query) | Q(location__icontains=query))

        paginator = PastEventsAPIPagination()
        page = paginator.paginate_queryset(queryset, request)
        serializer = EventSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)



class EventPostListCreateView(generics.ListCreateAPIView):
    serializer_class = EventPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



    def get_queryset(self):
        event_id = self.kwargs['event_id']
        return EventPost.objects.filter(event_id=event_id).order_by('-created_at')

    def perform_create(self, serializer):
        event = get_object_or_404(Event, pk=self.kwargs['event_id'])
        serializer.save(user=self.request.user, event=event)

class EventLikeToggleView(generics.GenericAPIView):
    serializer_class = EventLikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, event_id):
        event = get_object_or_404(Event, pk=event_id)
        like, created = EventLike.objects.get_or_create(event=event, user=request.user)
        if not created:
            like.delete()
            liked = False
        else:
            liked = True
        count = EventLike.objects.filter(event=event).count()
        return Response({'liked': liked, 'likes_count': count})