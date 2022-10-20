from django.urls import path
from .views import charSheet


urlpatterns = [
    path('', charSheet, name="charSheet"),
]
