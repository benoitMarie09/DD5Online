from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ClassForm

# Create your views here.


def charSheet(request):

    form = ClassForm(request=request)

    return render(request, 'charSheet/charSheet.html', {'form': form})
