# Generated by Django 4.1.1 on 2022-11-03 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charSheet', '0051_remove_historique_outils_alter_arme_degat_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Outil',
        ),
        migrations.AlterField(
            model_name='arme',
            name='type_degat',
            field=models.CharField(blank=True, choices=[('CTD', 'Contondant'), ('PRF', 'Cerforant'), ('TRC', 'Tranchant'), (None, '(Aucun)')], max_length=3, null=True),
        ),
    ]
