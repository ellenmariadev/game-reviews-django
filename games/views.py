from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, 'games/pages/index.html')

def lista(request, id):
    return render(request, 'games/pages/lista.html')