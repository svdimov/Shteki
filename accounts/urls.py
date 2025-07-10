

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from accounts import views
from accounts.views import CustomLoginView

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name='register'),
    path("login/", CustomLoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("profile/<int:pk>/", include([
        path('', views.ProfileDetailView.as_view(), name='profile-details'),
        path('edit/', views.ProfileEditView.as_view(), name='edit-profile'),
        path('delete/', views.ProfileDeleteView.as_view(), name='delete-profile'),
    ])),
]
