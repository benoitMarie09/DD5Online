from django.urls import path
from .views import UpadateNomView, UpdateCaractView, CreatePJView, UpdateClasseView, UpdateRaceView, UpdateCompetencesView, PJDetails, UpdateHistoriqueView

urlpatterns = [
    path('', CreatePJView.as_view(), name='create'),
    path('<int:pk>/nom/', UpadateNomView.as_view(), name="nom"),
    path('<int:pk>/race/', UpdateRaceView.as_view(), name="race"),
    path('<int:pk>/classe/', UpdateClasseView.as_view(), name="classe"),
    path('<int:pk>/historique/', UpdateHistoriqueView.as_view(), name="historique"),
    path('<int:pk>/competences/',
         UpdateCompetencesView.as_view(), name='competences'),
    path('<int:pk>/caract/',
         UpdateCaractView.as_view(), name='caract'),
    path('<int:pk>/detail/', PJDetails.as_view(), name='detail'),
]
