from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .forms import CreateForm, ClasseForm, CompetencesForm
from .models import PJ
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
# Create your views here.


class CreatePJView(CreateView):
    model = PJ
    form_class = CreateForm
    template_name = 'charSheet/pj_form.html'

    def get_success_url(self):
        return reverse('classe', kwargs={'pk': self.object.pk})


class UpdateClasseView(UpdateView):
    model = PJ
    form_class = ClasseForm
    template_name = 'charSheet/classe_form.html'

    def get_success_url(self):
        return reverse('competences', args=(self.object.id,))


class UpdateCcompetencesView(UpdateView):
    model = PJ
    form_class = CompetencesForm
    template_name = 'charSheet/comp_form.html'

    def get_success_url(self):
        return reverse('detail', args=(self.object.id,))


class PJDetails(DetailView):
    model = PJ

