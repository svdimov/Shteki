from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django.utils import timezone
from django.db.models import Q
from events.models import Event
from events.serializers import EventSerializer

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
