from django.urls.conf import path

from common import views, api_views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('api/events/<int:pk>/status/', api_views.EventStatusAPI.as_view(), name='api-event-status'),


]