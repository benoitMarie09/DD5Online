from django import forms
from django.db import models
from django.contrib import admin
from django.forms import RadioSelect, CheckboxSelectMultiple
import requests
from .models import PJ, Classe


class CreateForm(forms.ModelForm):

    class Meta:
        model = PJ
        fields = ['nom', ]


class ClasseForm(forms.ModelForm):
    class Meta:
        model = PJ
        fields = ['classe', ]
        widgets = {'classe': RadioSelect}


class CompetencesForm(forms.ModelForm):
    maitrise_competences = forms.ModelMultipleChoiceField(queryset=None,
                                                          widget=CheckboxSelectMultiple)

    class Meta:
        model = PJ
        fields = ['maitrise_competences', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.classe = self.instance.classe
        self.nb_competences = self.classe.nb_competences
        self.fields['maitrise_competences'].queryset = self.classe.choix_competences.all()

    def clean_maitrise_competences(self):
        value = self.cleaned_data['maitrise_competences']
        if len(value) != self.nb_competences:
            raise forms.ValidationError(
                f"Vous devez sélectionner {self.nb_competences} compétences.")
        return value


class ClasseAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


class PJAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
