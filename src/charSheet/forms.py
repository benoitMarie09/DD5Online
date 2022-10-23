from django import forms
import requests
from .models import Character

class CreateForm(forms.ModelForm):

    class Meta:
        model = Character
        fields = ['name',]

class ClassForm(forms.ModelForm):
    classe = forms.ChoiceField(widget=forms.RadioSelect,
                               choices=())

    class Meta:
        model = Character
        fields = ('classe',)

    def __init__(self, *args, request=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['classe'].choices = self.get_classes_choices()

    def get_classes_choices(self):
        r = requests.get(
            'https://www.dnd5eapi.co/api/classes')
        classes_data = r.json()
        choices = []
        for DDclass in classes_data['results']:
            choices.append((DDclass['index'], DDclass['index'].capitalize()))
        return choices
