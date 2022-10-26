# Generated by Django 4.1.1 on 2022-10-26 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charSheet', '0019_racecapacite_valeurcaracteristique_race_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='race',
            name='bonus_caracteristique',
        ),
        migrations.AddField(
            model_name='race',
            name='bonus_caracteristique',
            field=models.ManyToManyField(
                through='charSheet.BonusCaracteristique', to='charSheet.caracteristique'),
        ),
    ]