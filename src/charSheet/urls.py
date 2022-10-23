from django.urls import path
from .views import classe, thanks, create_character


urlpatterns = [
    path('', create_character, name='create'),
    path('<int:id>/classe/', classe, name="classe"),
    path('<int:id>/thanks/', thanks, name='thanks'),
]
