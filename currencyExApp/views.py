from django.shortcuts import render
from django.template.defaulttags import register
from django.http import JsonResponse
from .allCurrencies import allCurrenciesDetails
from .getRequest import *


def home(request):
    getResults = getRequest(request)
    return render(request, 'home.html', getResults)


def result(request):
    getResults = getRequest(request)
    return render(request, 'result.html', getResults)
   
def showError(request):
    return render(request, 'error.html', {}, status=500)
    
# custom filter sym->currency name
@register.filter
def get_currency_name(sym):
    return allCurrenciesDetails.get(sym)[0]

# custom filter sym->flag tag
@register.filter
def get_flag(sym):
    return allCurrenciesDetails.get(sym)[1]
