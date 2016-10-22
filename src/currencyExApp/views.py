from django.shortcuts import render
from django.template.defaulttags import register
from django.http import JsonResponse
from .getRequest import *
from .allCurrencies import allCurrenciesDetails


def home(request):
    getResults = getRequest(request)
    return render(request, 'home.html', getResults)


def result(request):
    getResults = getRequest(request)
    return render(request, 'result.html', getResults)


def hresult(request):
    getHresults = getHistoricRequest(request)
    return JsonResponse(getHresults, safe=False)

# custom filter sym->currency name
@register.filter
def get_currency_name(sym):
    return allCurrenciesDetails.get(sym)[0]

# custom filter sym->flag tag
@register.filter
def get_flag(sym):
    return allCurrenciesDetails.get(sym)[1]
