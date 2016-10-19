# Get conversion factors from one currency to another
# API documentation from: fixer.io

import urllib
import sys
import json

currencyList = ["AUD","BGN","BRL","CAD","CHF","CNY","CZK","DKK","EUR", "GBP","HKD","HRK","HUF",\
                "IDR","ILS","INR","JPY","KRW","MXN","MYR","NOK","NZD","PHP","PLN","RON","RUB",\
                "SEK","SGD","THB","TRY","USD","ZAR"]

##### Approach: convert the returned string from JSON to a dict  #######
def getInfo(currencyFrom, currencyTo):
    URL = 'http://api.fixer.io/latest?base=' + currencyFrom 
    
    # Make the request and save the response as a string.
    response = urllib.urlopen(URL).read()

    # Use json package to convert response to a dict
    responseAsDict = json.loads(response)  
    #print responseAsDict
    ratesDict = responseAsDict['rates']  # get the rates as a dict
    conversionFactor = ratesDict[currencyTo]  # find the appropriate conversion

    return conversionFactor

print 'Welcome to my currency conversion factor program.'
print "It will show today's conversion factor between any of the following currencies:"
print

abbrevString = ' '.join(currencyList)  # use join to make one string from all our abbreviations
print abbrevString


while True:
    print
    while True:
        currencyFrom = raw_input('Convert currency from? ')
        currencyFrom = currencyFrom.upper()  # Force to upper case
        if currencyFrom == '':
            sys.exit()
        if currencyFrom in currencyList:
            break
        else:
            print 'Sorry', currencyFrom, 'is not in the list of currencies.'

    print
    while True:
        currencyTo = raw_input('Convert currency to? ')
        currencyTo = currencyTo.upper()  # Force to upper case
        if currencyTo == '':
            sys.exit()
        if currencyTo in currencyList:
            break
        else:
            print 'Sorry', currencyTo, 'is not in the list of currencies.'

    conversion = getInfo(currencyFrom, currencyTo)
    print
    print 'Conversion factor from:', currencyFrom, 'to: ', currencyTo, 'is:',  conversion
    print

print 'Bye'


