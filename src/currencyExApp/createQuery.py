import requests
import datetime
from .allCurrencies import commonCurrencies


def createExRateQuery(froCurr, toCurr):
    # currencies to query
    currencies = "(" + "'" + froCurr + toCurr + "'"
    for curr in commonCurrencies:
        currencies = currencies + ", " + "'" + froCurr + curr + "'"
    currencies = currencies + ")"

    # yahoo get query
    query = "https://query.yahooapis.com/v1/public/yql?q=select Name, Rate from yahoo.finance.xchange where pair in " + str(currencies) + " &format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
    ratesJson = requests.get(query).json()['query']['results']['rate']
    return ratesJson


def createHistoricQuery(froCurr, toCurr):
    result = []
    startDate = (datetime.datetime.now() - datetime.timedelta(days=30)).strftime("%Y/%m/%d")
    endDate = datetime.datetime.now().strftime("%Y/%m/%d")
    for curr in [froCurr, toCurr]:
        query = "https://query.yahooapis.com/v1/public/yql?q=select * from yahoo.finance.historicaldata where symbol = '" + curr + "=X' and startDate ='" + startDate + "'and endDate ='" + endDate + "' &format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
        HistoricJson = requests.get(query).json()['query']['results']['quote']
        result.append(HistoricJson)
    return result
