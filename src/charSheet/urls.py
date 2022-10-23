from django.urls import path
from .views import classe, thanks, create_character, proficiencies


urlpatterns = [
    path('', create_character, name='create'),
    path('<int:id>/classe/', classe, name="classe"),
    path('<int:id>/proficiencies/', proficiencies, name='proficiencies'),
    path('<int:id>/thanks/', thanks, name='thanks'),
]
