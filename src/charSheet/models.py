from django.db import models


# Create your models here.


"""class Character(models.Model):
    name = models.CharField(max_length=100)
    race = models.CharField(max_length=100)
    classe = models.CharField(max_length=100,choices())
    background = models.CharField(max_length=100)
    # stats
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()"""


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
        Caracteristique, null=True, related_name='competences', on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class Classe(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    desc = models.TextField(null=True)
    dv = models.IntegerField(null=True)
    choix_competences = models.ManyToManyField(Competence)
    nb_competences = models.IntegerField(default=2)
    jets_sauvegarde = models.ManyToManyField(Caracteristique)

    def __str__(self):
        return self.id


class PJ(models.Model):
    nom = models.CharField(null=True, max_length=100)
    classe = models.ForeignKey(
        Classe, null=True, related_name='PJs', on_delete=models.CASCADE)
    maitrise_competences = models.ManyToManyField(Competence)

    def __str__(self):
        return '{}-{}-{}'.format(self.id, self.nom, self.classe)
