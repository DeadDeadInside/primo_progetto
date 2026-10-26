from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "prova_pratica_1_C/index.html")

def prodotto(request):
    return render(request, "prova_pratica_1_C/prodotto.html")

def conteggio(request):
    return render(request, "prova_pratica_1_C/conteggio.html")

def temperature(request):
    return render(request, "prova_pratica_1_C/temperature.html")