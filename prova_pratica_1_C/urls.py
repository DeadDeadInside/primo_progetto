from django.urls import path
from prova_pratica_1_C.views import index, prodotto, conteggio, temperature

app_name = "prova_pratica_1_C"
urlpatterns = [
    path('prodotto', prodotto, name='prodotto'),
    path('conteggio', conteggio, name='conteggio'),
    path('temperature', temperature, name='temperature'),
    path('index', index, name='index'),
]