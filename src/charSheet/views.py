from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .forms import CaractForm, CreateForm, ClasseForm, CompetencesForm, HistoriqueForm, RaceForm
from .models import PJ, BonusCaracteristique
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
# Create your views here.


class CreatePJView(CreateView):
    model = PJ
    form_class = CreateForm
    template_name = 'charSheet/pj_form.html'

    def get_success_url(self):
        return reverse('race', kwargs={'pk': self.object.pk})


class UpadateNomView(UpdateView):
    model = PJ
    form_class = CreateForm
    template_name = 'charSheet/pj_form.html'

    def get_success_url(self):
        return reverse('race', kwargs={'pk': self.object.pk})


class UpdateRaceView(UpdateView):
    model = PJ
    form_class = RaceForm
    template_name = 'charSheet/race_form.html'

    def get_success_url(self):
        return reverse('classe', args=(self.object.id,))


class UpdateClasseView(UpdateView):
    model = PJ
    form_class = ClasseForm
    template_name = 'charSheet/classe_form.html'

    def get_success_url(self):
        return reverse('historique', args=(self.object.id,))


class UpdateHistoriqueView(UpdateView):
    model = PJ
    form_class = HistoriqueForm
    template_name = 'charSheet/classe_form.html'

    def get_success_url(self):
        return reverse('competences', args=(self.object.id,))


class UpdateCompetencesView(UpdateView):
    model = PJ
    form_class = CompetencesForm
    template_name = 'charSheet/comp_form.html'

    def get_success_url(self):
        return reverse('caract', args=(self.object.id,))


class UpdateCaractView(UpdateView):
    model = PJ
    form_class = CaractForm
    template_name = 'charSheet/caract_form.html'

    def get_success_url(self):
        return reverse('detail', args=(self.object.id,))


class PJDetails(DetailView):
    model = PJ
