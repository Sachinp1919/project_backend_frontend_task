from django.urls import path
from .views import PersonAPI, PersonDetailsAPI

urlpatterns = [
    path('person/', PersonAPI.as_view()),
    path('person/<int:pk>/',PersonDetailsAPI.as_view())
]