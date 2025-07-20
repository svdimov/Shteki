from django.urls.conf import path, include

from events import views

urlpatterns = [
    path('new-events/', views.NewEventView.as_view(), name='new-events'),
    path('past-events/', views.PastEventView.as_view(), name='past-events'),

    path('evetnts/create/', views.CreateEventView.as_view(), name='create-event'),
    path('events/<int:pk>/', include([
        path('', views.EventDetailView.as_view(), name='event-details'),

    ])),

]
