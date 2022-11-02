from django.contrib import admin
from .models import PJ, Caracteristique, Classe, Competence, Equipement, EquipementAdmin, Historique, HistoriqueAdmin, Langue, Outil, QuantiteEquipement, Race, RaceCapacite, BonusCaracteristique, RaceAdmin, CaracteristiqueAdmin, QuantiteEquipement
from .models import *
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
admin.site.register(De)
admin.site.register(Type_degat)
admin.site.register(Arme, ArmeAdmin)
admin.site.register(ProprieteArme)
admin.site.register(CategorieArme)
