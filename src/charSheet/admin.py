from django.contrib import admin
from .models import PJ, Caracteristique, Classe, Competence
# Register your models here.
admin.site.register(PJ)
admin.site.register(Competence)
admin.site.register(Classe)
admin.site.register(Caracteristique)
