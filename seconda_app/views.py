from django.shortcuts import render
import datetime

def esempio_if(request):
    dic = { 'var1' : 200, 'var2' : 200, 'var3' : 300 }
    return render(request, "seconda_app/es_if.html", dic)

def esempio_if_else_elif(request):
    dic = { 'var1' : 200, 'var2' : 200, 'var3' : 300 }
    return render(request, "seconda_app/if_else_elif.html", dic)

def esempio_for(request):
    dic = { 'listi': [1, datetime.date(2019,7,16), 'Do not give up!'], 'list2': [1, datetime.date(2019,7,16), 'Do not give up!'], 'my_dict' : {'chiave1': 'Valore 1', 'chiave2': 'Valore 2'} }
    return render(request, "seconda_app/es_for.html", dic)