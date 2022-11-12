from django.shortcuts import render

from .models import Games

# Create your views here.

def home_view(request):
    games = Games.objects.all().order_by('title')
    return render(request, 'games/pages/home.html', context={
        'games': games,
    })

def lista(request, id):
    return render(request, 'games/pages/lista.html')