# Generated by Django 4.1.1 on 2022-10-25 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charSheet', '0002_rename_character_pj'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pj',
            old_name='name',
            new_name='nom',
        ),
    ]