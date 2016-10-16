from django.shortcuts import render
from .exchange import exchange
from django.template.defaulttags import register
# all currencies constants
from .allCurrencies import *


def home(request):
    amt = None
    froCurr = None
    toCurr = None
    exRates = None
    getResults = None
    # checking GET parameters
    if 'amt' in request.GET and request.GET['amt'] != "":
        amt = request.GET['amt']
    if 'froCurr' in request.GET and request.GET['froCurr'] != "":
        froCurr = request.GET['froCurr']
    if 'toCurr' in request.GET and request.GET['toCurr'] != "":
        toCurr = request.GET['toCurr']
    # getting exhange rates
    if(amt and froCurr and toCurr):
        exRates = exchange(amt, froCurr, toCurr)

    getValues = {}
    getValues["amt"] = amt
    getValues["toCurr"] = toCurr
    getValues["froCurr"] = froCurr

    # result object    
    getResults = {
        'getValues': getValues,
        'exRates': exRates,
        'commonCurrencies': commonCurrencies,
        'allCurrencies': allCurrencies
    }

    return render(request, 'index.html', getResults)

# custom filter sym->currency name
@register.filter
def get_currency_name(dictionary, sym):
    return dictionary.get(sym)[0]

# custom filter sym->flag tag
@register.filter
def get_flag(dictionary, sym):
    return dictionary.get(sym)[1]
