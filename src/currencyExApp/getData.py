import datetime
from .createQuery import *


def getExchange(amt, froCurr, toCurr):
    ratesJson = createExRateQuery(froCurr, toCurr)
    # result object
    exRates = {}
    exRates["timestamp"] = datetime.datetime.now().strftime("%b, %d %I:%M%p")
    exRates["value"] = round(float(amt) * float(ratesJson[0]["Rate"]), 5)
    # exchange rates for common currencies
    exRates["commonConversion"] = []
    # inverse exchange rates
    exRates["commonInConversion"] = []

    for rate in ratesJson[1:]:
        exRates["commonConversion"].append(float(rate['Rate']))
        exRates["commonInConversion"].append(round(1 / float(rate['Rate']), 4))
    return exRates


def getHistoricData(froCurr):
    return createHistoricQuery(froCurr)
