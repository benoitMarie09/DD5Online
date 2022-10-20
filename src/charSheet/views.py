from django.shortcuts import render

# Create your views here.


def charSheet(request):
    return render(request, 'charSheet/charSheet.html')
