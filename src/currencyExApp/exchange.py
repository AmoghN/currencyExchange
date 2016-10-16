from yahoo_finance import Currency
from .allCurrencies import commonCurrencies


def exchange(amt, froCurr, toCurr):
    froCurr = Currency(froCurr)
    toCurr = Currency(toCurr)
    value = round(float(amt) * float(toCurr.get_rate()) / float(froCurr.get_rate()), 6)

    # getting exchange rates for common currencies
    commonConversion = []
    # inverse convertion rate
    commonInConversion = []
    for commonCurrency in commonCurrencies:
        commonCurrency = Currency(commonCurrency)
        convertionRate = float(commonCurrency.get_rate()) / float(froCurr.get_rate())
        convertion = round(convertionRate, 6)
        inConversion = round(1 / convertionRate, 6)
        commonConversion.append(convertion)
        commonInConversion.append(inConversion)

    exRates = {}
    exRates["value"] = value
    exRates["commonConversion"] = commonConversion
    exRates["commonInConversion"] = commonInConversion
    return exRates
