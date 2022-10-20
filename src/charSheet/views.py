from django.shortcuts import render
import requests

# Create your views here.


def charSheet(request):
    r = requests.get(
        ' https://www.dnd5eapi.co/api/classes', params=request.GET)
    classes_data = r.json()
    context = dict()
    context['classes'] = []
    for DDclass in classes_data['results']:
        context['classes'].append(DDclass['index'])
    return render(request, 'charSheet/charSheet.html', context)
