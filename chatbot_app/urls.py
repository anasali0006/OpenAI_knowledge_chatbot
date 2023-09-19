from django.urls import path
from . import views


urlpatterns = [
    path("health_check", views.ChatbotHealthCheck.as_view()),
    path("health_check/", views.ChatbotHealthCheck.as_view()),
]