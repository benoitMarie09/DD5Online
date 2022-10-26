from django.db import models
from django.contrib import admin


# Create your models here.

class RaceCapacite(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    desc = models.TextField(null=True)

    def __str__(self):
        return self.id


class Race(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    desc = models.TextField(null=True, blank=True)
    taille_max = models.IntegerField(null=True, blank=True)
    taille_min = models.IntegerField(null=True, blank=True)
    vitesse = models.DecimalField(
        decimal_places=1, max_digits=4, null=True, blank=True)
    bonus_caracteristique = models.ManyToManyField(
        'Caracteristique', through='BonusCaracteristique')
    capacite = models.ManyToManyField('RaceCapacite')
    famille = models.CharField(null=True, blank=True, max_length=20)
    #sorts = manytomany

    def __str__(self):
        return self.id


class BonusCaracteristique(models.Model):
    caracteristique = models.ForeignKey(
        'Caracteristique', related_name='bonus_caract', on_delete=models.SET_NULL, null=True)
    race = models.ForeignKey(
        'Race', related_name='bonus_caract', on_delete=models.SET_NULL, null=True)
    valeur = models.IntegerField(default=1)


class ValeurCaracteristique(models.Model):
    caracteristique = models.ForeignKey(
        'Caracteristique', related_name='valeur_caract', on_delete=models.SET_NULL, null=True)
    PJ = models.ForeignKey(
        'PJ', related_name='valeur_caract', on_delete=models.SET_NULL, null=True)
    valeur = models.IntegerField(default=10)


class Caracteristique(models.Model):
    id = models.CharField(primary_key=True, max_length=3)
    nom = models.CharField(null=True, max_length=20)
    desc = models.TextField(null=True)

    def __str__(self):
        return self.id


class Competence(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    desc = models.TextField(null=True)
    caracteristique = models.ForeignKey(
        'Caracteristique', null=True, related_name='competences', on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class Classe(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    desc = models.TextField(null=True)
    dv = models.IntegerField(null=True)
    choix_competences = models.ManyToManyField('Competence')
    nb_competences = models.IntegerField(default=2)
    jets_sauvegarde = models.ManyToManyField('Caracteristique')

    def __str__(self):
        return self.id


class PJ(models.Model):
    nom = models.CharField(null=True, max_length=100)
    classe = models.ForeignKey(
        'Classe', null=True, related_name='PJs', on_delete=models.CASCADE)
    maitrise_competences = models.ManyToManyField('Competence')

    def __str__(self):
        return '{}-{}-{}'.format(self.id, self.nom, self.classe)


# Gestion des formulaire admin pour le m2m

class BonusCaracteristique_inline(admin.TabularInline):
    model = BonusCaracteristique
    extra = 1


class RaceAdmin(admin.ModelAdmin):
    inlines = (BonusCaracteristique_inline,)


class CaracteristiqueAdmin(admin.ModelAdmin):
    inlines = (BonusCaracteristique_inline,)
