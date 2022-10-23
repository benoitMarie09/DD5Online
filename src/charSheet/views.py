from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ClassForm, CreateForm, ClassProfForm
from .models import Character
# Create your views here.


def create_character(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            character = form.save()
            return HttpResponseRedirect('/{}/classe/'.format(character.id))
    else:
        form = CreateForm()
    return render(request, 'charSheet/createForm.html', {'form': form})


def classe(request, id):
    character = Character.objects.get(id=id)
    if request.method == 'POST':
        form = ClassForm(request.POST, instance=character)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/{}/proficiencies/'.format(id))
    else:
        form = ClassForm(instance=character)
    return render(request, 'charSheet/classeForm.html', {'form': form})


def proficiencies(request, id):
    character = Character.objects.get(id=id)
    if request.method == 'POST':
        form = ClassProfForm(
            request.POST, character=character, instance=character)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/{}/thanks/'.format(id))
    else:
        form = ClassProfForm(character=character, instance=character)
    return render(request, 'charSheet/profForm.html', {'form': form})


def thanks(request, id):
    character = Character.objects.get(id=id)
    context = dict()
    context['name'] = character.name
    context['classe'] = character.classe
    return render(request, 'charSheet/thanks.html', context)
