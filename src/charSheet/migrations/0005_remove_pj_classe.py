# Generated by Django 4.1.1 on 2022-10-25 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charSheet', '0004_remove_pj_proficiencies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pj',
            name='classe',
        ),
    ]
