# Generated by Django 4.1.1 on 2022-10-26 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charSheet', '0031_caractform_competence_charisme_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competence',
            name='charisme',
        ),
        migrations.RemoveField(
            model_name='competence',
            name='constitution',
        ),
        migrations.RemoveField(
            model_name='competence',
            name='dexterite',
        ),
        migrations.RemoveField(
            model_name='competence',
            name='force',
        ),
        migrations.RemoveField(
            model_name='competence',
            name='intelligence',
        ),
        migrations.RemoveField(
            model_name='competence',
            name='sagesse',
        ),
        migrations.AddField(
            model_name='pj',
            name='charisme',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pj',
            name='constitution',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pj',
            name='dexterite',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pj',
            name='force',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pj',
            name='intelligence',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pj',
            name='sagesse',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
