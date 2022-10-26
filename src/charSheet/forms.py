from django import forms
from django.db import models
from django.contrib import admin
from django.forms import RadioSelect, CheckboxSelectMultiple
import requests
from .models import PJ, Classe, Competence, Historique
from django.db.models import Q


class CreateForm(forms.ModelForm):

    class Meta:
        model = PJ
        fields = ['nom', ]


class RaceForm(forms.ModelForm):
    class Meta:
        model = PJ
        fields = ['race', ]
        widgets = {'race': RadioSelect}


class ClasseForm(forms.ModelForm):
    class Meta:
        model = PJ
        fields = ['classe', ]
        widgets = {'classe': RadioSelect}


class HistoriqueForm(forms.ModelForm):
    class Meta:
        model = PJ
        fields = ['historique', ]
        widgets = {'historique': RadioSelect}


class CompetencesForm(forms.ModelForm):
    maitrise_competences = forms.ModelMultipleChoiceField(queryset=None,
                                                          widget=CheckboxSelectMultiple)

    class Meta:
        model = PJ
        fields = ['maitrise_competences', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.classe = self.instance.classe
        self.historique = self.instance.historique
        self.nb_competences = self.classe.nb_competences + 2
        choix_competence = Competence.objects.filter(
            classes=self.classe, historiques=self.historique)
        self.fields['maitrise_competences'].queryset = choix_competence

    def clean_maitrise_competences(self):
        values = self.cleaned_data['maitrise_competences']
        if len(values) != self.nb_competences:
            raise forms.ValidationError(
                f"Vous devez sélectionner {self.nb_competences} compétences.")
        for comp in self.instance.historique.competences.all():
            if comp not in values:
                raise forms.ValidationError(
                    f"Vous devez sélectionner les compétences historiques {self.instance.historique.competences.all()[0]} et {self.instance.historique.competences.all()[0]}.")
        return values


class CaractForm(forms.ModelForm):

    class Meta:
        model = PJ
        fields = ['force', 'constitution', 'dexterite',
                  'intelligence', 'sagesse', 'charisme', ]


class ClasseAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


class PJAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
