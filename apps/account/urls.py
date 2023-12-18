from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path('users/', views.UserListView.as_view()),
    path('register/', views.RegistrationView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
