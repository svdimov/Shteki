from django.urls.conf import path, include

from events import views
from events.api_views import PastEventsAPI, EventPostListCreateView, EventLikeToggleView

urlpatterns = [
    path('new-events/', views.NewEventView.as_view(), name='new-events'),
    path('past-events/', views.PastEventView.as_view(), name='past-events'),
    path('api/past-events/', PastEventsAPI.as_view(), name='api-past-events'),

    path('event/create/', views.CreateEventView.as_view(), name='create-event'),
    path('events/<int:event_id>/', include([
        path('', views.EventDetailView.as_view(), name='event-details'),
        path('posts/', EventPostListCreateView.as_view(), name='event-posts'),
        path('like/', EventLikeToggleView.as_view(), name='event-like'),

    ])),


]
