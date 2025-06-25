from django.urls.conf import path

from common import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    # path('contact/', views.ContactPageView.as_view(), name='contact'),
]