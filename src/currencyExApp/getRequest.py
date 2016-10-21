import datetime
from .getData import *
# all currencies constants
from .allCurrencies import *


def getRequest(request):
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
        exRates = getExchange(amt, froCurr, toCurr)

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

    return getResults


def getHistoricRequest(request):
    return getHistoricData(request.GET['froCurr'], request.GET['toCurr'])
