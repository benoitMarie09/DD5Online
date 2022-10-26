from django.contrib import admin
from .models import PJ, Caracteristique, Classe, Competence, Equipement, EquipementAdmin, Historique, HistoriqueAdmin, Langue, Outil, QuantiteEquipement, Race, RaceCapacite, BonusCaracteristique, RaceAdmin, CaracteristiqueAdmin, QuantiteEquipement
from .forms import ClasseAdmin, PJAdmin
# Register your models here.

admin.site.register(PJ, PJAdmin)
admin.site.register(Competence)
admin.site.register(Classe, ClasseAdmin)
admin.site.register(Caracteristique, CaracteristiqueAdmin)
admin.site.register(Race, RaceAdmin)
admin.site.register(RaceCapacite)
admin.site.register(BonusCaracteristique)
admin.site.register(Historique, HistoriqueAdmin)
admin.site.register(Equipement, EquipementAdmin)
admin.site.register(Outil)
admin.site.register(QuantiteEquipement)
admin.site.register(Langue)
