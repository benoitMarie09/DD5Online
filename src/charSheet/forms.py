from django import forms
from django.db import models
from django.contrib import admin
from django.forms import RadioSelect, CheckboxSelectMultiple
import requests
from .models import PJ, Classe, Competence, Historique
from django.db.models import Q


class CheckboxSelectMultipleWithDisabledOption(forms.CheckboxSelectMultiple):
    def __init__(self, *args, **kwargs):
        super(forms.CheckboxSelectMultiple, self).__init__(*args, **kwargs)
        self.disabled_options = None

    def create_option(self, *args, **kwargs):
        options_dict = super().create_option(*args, **kwargs)

        if options_dict['value'] in self.disabled_options:
            options_dict['attrs']['class'] = 'readonly'

        return options_dict


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
                                                          widget=CheckboxSelectMultipleWithDisabledOption)

    class Meta:
        model = PJ
        fields = ['maitrise_competences', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.classe = self.instance.classe
        self.historique = self.instance.historique
        self.nb_competences = self.classe.nb_competences + 2
        choix_competence = Competence.objects.filter(
            Q(classes=self.classe) | Q(historiques=self.historique)).distinct()
        self.fields['maitrise_competences'].queryset = choix_competence
        self.comp_hist = [c.id for c in Competence.objects.filter(
            historiques=self.historique)]
        self.comp_selected = [
            c.id for c in self.instance.maitrise_competences.all()]
        self.initial = {'maitrise_competences': list(
            set(self.comp_hist + self.comp_selected))}
        self.fields['maitrise_competences'].widget.disabled_options = [c.id for c in Competence.objects.filter(
            historiques=self.historique)]

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
