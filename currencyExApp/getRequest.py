from .getData import getExchange
# all currencies constants
from .allCurrencies import allCurrencies, commonCurrencies


def getRequest(request):
    amt = None
    froCurr = None
    toCurr = None
    exRates = None
    getResults = None
    # checking GET parameters
    if 'amt' in request.GET and request.GET['amt'] != "":
        amt = round(float(request.GET['amt']), 2)
    if 'froCurr' in request.GET and request.GET['froCurr'] != "":
        froCurr = request.GET['froCurr']
    if 'toCurr' in request.GET and request.GET['toCurr'] != "":
        toCurr = request.GET['toCurr']
    # getting exchange rates
    if(amt and froCurr and toCurr):
        exRates = getExchange(amt, froCurr, toCurr)

    getValues = {
        "amt": amt,
        "toCurr": toCurr,
        "froCurr": froCurr
    }

    # result object
    getResults = {
        'getValues': getValues,
        'exRates': exRates,
        'commonCurrencies': commonCurrencies,
        'allCurrencies': allCurrencies
    }

    return getResults
