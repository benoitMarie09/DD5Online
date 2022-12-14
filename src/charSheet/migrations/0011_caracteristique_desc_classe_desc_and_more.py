# Generated by Django 4.1.1 on 2022-10-25 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charSheet', '0010_pj_maitrise_competences'),
    ]

    operations = [
        migrations.AddField(
            model_name='caracteristique',
            name='desc',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='classe',
            name='desc',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='competence',
            name='caracteristique',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='competences', to='charSheet.caracteristique'),
        ),
        migrations.AddField(
            model_name='competence',
            name='desc',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='pj',
            name='classe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PJs', to='charSheet.classe'),
        ),
    ]
