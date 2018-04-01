import datetime
from requests import get
from os import getenv
from .allCurrencies import *

def getExchange(amt, froCurr, toCurr):
    API_KEY = getenv("API_KEY")
    request_url = "https://openexchangerates.org/api/latest.json?app_id={}".format(API_KEY)
    ratesJson = get(request_url).json()

    # result object
    exRates = {
        "timestamp" : datetime.datetime.now().strftime("%b, %d %I:%M%p"),
        "value" : None,
        "commonConversion" : list(),  # exchange rates for common currencies
        "commonInConversion" : list() # inverse exchange rates
    }

    # exchange rate
    if froCurr != "USD":
        fro = float(ratesJson["rates"][froCurr])
        to =  float(ratesJson["rates"][toCurr])
        exRate = 1 / (fro * (1 / to))
    else:
        exRate = float(ratesJson["rates"][toCurr])

    exRates["value"] = round(float(amt) * exRate, 2)

    for curr in commonCurrencies:
        if froCurr != "USD":
            fro = float(ratesJson["rates"][froCurr])
            to =  float(ratesJson["rates"][curr])
            exRate = round(1 / (fro * (1 / to)), 4)
        else:
            exRate =  float(ratesJson["rates"][curr])

        inExRate = round(1 / exRate, 4)
        exRates["commonConversion"].append(exRate)
        exRates["commonInConversion"].append(inExRate)
   
    return exRates

