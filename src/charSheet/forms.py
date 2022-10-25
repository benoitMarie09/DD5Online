from django import forms
import requests
from .models import PJ


class CreateForm(forms.ModelForm):

    class Meta:
        model = PJ
        fields = ['nom', ]

"""
class ClassForm(forms.ModelForm):
    classe = forms.ChoiceField(widget=forms.RadioSelect,
                               choices=())

    class Meta:
        model = PJ
        fields = ('classe',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['classe'].choices = self.get_classes_choices()

    def get_classes_choices(self):
        r = requests.get(
            'https://www.dnd5eapi.co/api/classes')
        classes_data = r.json()
        choices = []
        for DDclass in classes_data['results']:
            choices.append((DDclass['index'], DDclass['index'].capitalize()))
        print(choices)
        return choices
"""

"""
class ClassProfForm(forms.ModelForm):
    proficiencies = forms.ChoiceField(widget=forms.Select,
                                      choices=())

    class Meta:
        model = PJ
        fields = ('proficiencies',)

    def __init__(self, *args, character, **kwargs):
        super().__init__(*args, **kwargs)
        self.character = character
        self.classe = character.classe
        self.fields['proficiencies'].choices = self.get_prof_choices(
            self.classe)

    def get_prof_choices(self, classe):
        r = requests.get(
            'https://www.dnd5eapi.co/api/classes/'+classe)
        classe_data = r.json()
        choices = []
        for elem in classe_data['proficiency_choices']:
            for option in elem['from']['options']:
                prof = option['item']['index'].split('-')[-1]
                choices.append((prof, prof.capitalize()))
        print(choices)
        return choices"""
