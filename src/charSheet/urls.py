from django.urls import path
from .views import UpdateCaractView, CreatePJView, UpdateClasseView, UpdateRaceView, UpdateCompetencesView, PJDetails

urlpatterns = [
    path('', CreatePJView.as_view(), name='create'),
    path('<int:pk>/race/', UpdateRaceView.as_view(), name="race"),
    path('<int:pk>/classe/', UpdateClasseView.as_view(), name="classe"),
    path('<int:pk>/competences/',
         UpdateCompetencesView.as_view(), name='competences'),
    path('<int:pk>/caract/',
         UpdateCaractView.as_view(), name='caract'),
    path('<int:pk>/detail/', PJDetails.as_view(), name='detail'),
]
