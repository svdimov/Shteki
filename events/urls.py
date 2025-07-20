from django.urls.conf import path, include

from events import views
from events.api_views import PastEventsAPI

urlpatterns = [
    path('new-events/', views.NewEventView.as_view(), name='new-events'),
    path('past-events/', views.PastEventView.as_view(), name='past-events'),
    path('api/past-events/', PastEventsAPI.as_view(), name='api-past-events'),

    path('event/create/', views.CreateEventView.as_view(), name='create-event'),
    path('events/<int:pk>/', include([
        path('', views.EventDetailView.as_view(), name='event-details'),

    ])),

]
