from django.urls import path
from .views import ask_question, home

urlpatterns = [
    path("", home),
    path("ask/", ask_question),
]