# Generated by Django 4.1.1 on 2022-10-25 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charSheet', '0009_pj_classe'),
    ]

    operations = [
        migrations.AddField(
            model_name='pj',
            name='maitrise_competences',
            field=models.ManyToManyField(to='charSheet.competence'),
        ),
    ]