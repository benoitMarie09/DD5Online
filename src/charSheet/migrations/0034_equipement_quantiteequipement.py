# Generated by Django 4.1.1 on 2022-10-26 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charSheet', '0033_historique_langue_outil_delete_caractform_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipement',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('desc', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuantiteEquipement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.IntegerField(default=1)),
                ('equipement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quantite_equipement', to='charSheet.equipement')),
                ('historique', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quantite_equipement', to='charSheet.historique')),
            ],
        ),
    ]
