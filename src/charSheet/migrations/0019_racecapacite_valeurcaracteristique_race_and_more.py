# Generated by Django 4.1.1 on 2022-10-26 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charSheet', '0018_alter_classe_nb_competences'),
    ]

    operations = [
        migrations.CreateModel(
            name='RaceCapacite',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('desc', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ValeurCaracteristique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valeur', models.IntegerField(default=10)),
                ('PJ', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='valeur_caract', to='charSheet.pj')),
                ('caracteristique', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='valeur_caract', to='charSheet.caracteristique')),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('taille_max', models.IntegerField(null=True)),
                ('taille_min', models.IntegerField(null=True)),
                ('vitesse', models.IntegerField(null=True)),
                ('bonus_caracteristique', models.ManyToManyField(to='charSheet.caracteristique')),
            ],
        ),
        migrations.CreateModel(
            name='BonusCaracteristique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valeur', models.IntegerField(default=1)),
                ('caracteristique', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bonus_caract', to='charSheet.caracteristique')),
                ('race', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bonus_caract', to='charSheet.race')),
            ],
        ),
    ]