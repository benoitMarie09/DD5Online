from django import forms
import requests


class ClassForm(forms.Form):
    your_class = forms.ChoiceField(widget=forms.RadioSelect,
                                   choices=())

    class Meta:
        fields = ('your_class',)

    def __init__(self, *args, request=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        self.fields['your_class'].choices = self.get_classes_choices()

    def get_classes_choices(self):
        r = requests.get(
            'https://www.dnd5eapi.co/api/classes', params=self.request.GET)
        classes_data = r.json()
        choices = []
        for DDclass in classes_data['results']:
            choices.append((DDclass['index'], DDclass['index'].capitalize()))

        return choices
