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


class Character(models.Model):
    name = models.CharField(null=True, max_length=100)
    classe = models.CharField(null=True, max_length=100)
    proficiencies = models.CharField(null=True, max_length=100)

    def __str__(self):
        return '{}-{}-{}'.format(self.id, self.name, self.classe)
