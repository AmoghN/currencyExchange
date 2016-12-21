import datetime
import time
from .createQuery import *


def getExchange(amt, froCurr, toCurr):
    ratesJson = createExRateQuery(froCurr, toCurr)
    # result object
    exRates = {}
    exRates["timestamp"] = datetime.datetime.now().strftime("%b, %d %I:%M%p")
    exRates["value"] = round(float(amt) * float(ratesJson[0]["Rate"]), 2)
    # exchange rates for common currencies
    exRates["commonConversion"] = []
    # inverse exchange rates
    exRates["commonInConversion"] = []

    for rate in ratesJson[1:]:
        exRates["commonConversion"].append(float(rate['Rate']))
        exRates["commonInConversion"].append(round(1 / float(rate['Rate']), 4))
    return exRates


def getHistoricData(froCurr, toCurr):
    hresults = []
    if(froCurr != 'USD' and toCurr != 'USD'):
        froHresults = createHistoricQuery(froCurr)
        toHresults = createHistoricQuery(toCurr)
        for hresult in range(0, len(toHresults)):
            result = []
            # changing timestamp to UNIX milliseconds
            # result.append(int(datetime.datetime.strptime(toHresults[hresult]['Date'], "%Y-%m-%d").timestamp()) * 1000)
            timestamp = time.mktime(datetime.datetime.strptime(toHresults[hresult]['Date'], "%Y-%m-%d").timetuple())
            result.append(int(timestamp * 1000))
            result.append(round(float(toHresults[hresult]['Close']) / float(froHresults[hresult]['Close']), 4))
            hresults.append(result)
    else:
        # historic graphs for USD
        hresult = None
        if(froCurr != "USD"):
            getHresult = createHistoricQuery(froCurr)
        else:
            getHresult = createHistoricQuery(toCurr)

        for hresult in range(0, len(getHresult)):
            result = []
            #result.append(int(datetime.datetime.strptime(getHresult[hresult]['Date'], "%Y-%m-%d").timestamp()) * 1000)
            timestamp = time.mktime(datetime.datetime.strptime(getHresult[hresult]['Date'], "%Y-%m-%d").timetuple())
            result.append(int(timestamp * 1000))
            if(toCurr == 'USD'):
                result.append(round(1 / float(getHresult[hresult]['Close']), 4))
            else:
                result.append(float(getHresult[hresult]['Close']))
            hresults.append(result)

    # made list to acending order
    hresults.reverse()
    return hresults
