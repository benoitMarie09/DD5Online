from django.contrib import admin
from .models import PJ, Caracteristique, Classe, Competence, Race, RaceCapacite, BonusCaracteristique, RaceAdmin, CaracteristiqueAdmin
from .forms import ClasseAdmin, PJAdmin
# Register your models here.

admin.site.register(PJ, PJAdmin)
admin.site.register(Competence)
admin.site.register(Classe, ClasseAdmin)
admin.site.register(Caracteristique, CaracteristiqueAdmin)
admin.site.register(Race, RaceAdmin)
admin.site.register(RaceCapacite)
admin.site.register(BonusCaracteristique)

