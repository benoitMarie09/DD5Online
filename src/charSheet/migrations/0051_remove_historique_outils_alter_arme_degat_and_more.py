# Generated by Django 4.1.1 on 2022-11-03 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charSheet', '0050_alter_arme_degat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historique',
            name='outils',
        ),
        migrations.AlterField(
            model_name='arme',
            name='degat',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='arme',
            name='type_degat',
            field=models.CharField(blank=True, choices=[('CTD', 'contondant'), ('PRF', 'perforant'), ('TRC', 'tranchant'), (None, '(Aucun)')], max_length=3, null=True),
        ),
    ]
