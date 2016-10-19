# Get company stock information
# API documentation from:  http://www.jarloo.com/yahoo_finance/

import urllib

def getQuote(symbol):
    # set the Yahoo finance base url
    baseURL = 'http://finance.yahoo.com/d/quotes.csv'

    # concatenate the stock symbol
    stockSpecificURL = baseURL + '?s=' + symbol

    # add in the formatting info:  n is name, a is ask price, g is days's low, h is day's high
    fullURLWithParameters  = stockSpecificURL + '&f=nagh'

    #print 'Full URL of request:', stockSpecificURL
    
    # read all the data
    response = urllib.urlopen(fullURLWithParameters).read()

    #print 'Response is: ', response

    # use split to convert the returned comma separated answer information into a list
    responseList = response.split(',')

    # return the list of values from the response
    return responseList


while True:
    symbol = raw_input('Enter a stock symbol or return/enter to quit: ')
    if symbol == '':
        break
    
    listOfValues = getQuote(symbol)

    # element 0 is name, element 1 is ask price, element 2 is low, element 3 is high
    print 'Price of: ' + listOfValues[0] +  ' is: ' + listOfValues[1]
    print '   Low for the day: ' + listOfValues[2] + '   High for the day: ', listOfValues[3]

print 'Bye'
