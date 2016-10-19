import urllib

# Example of 'screen scraping' from Google financial page

# This can break if Google changes the layout of items in their page (Google's html may change)

# Sample page:  http://finance.google.com/finance?q=aapl

# Treat the page full of html as one long string, and find the information we want from it

def get_quote(symbol):
    # set the google finance base url
    baseURL = 'http://finance.google.com/finance?q='
    # concatenate the stock symbol
    stockSpecificURL = baseURL + symbol
    # read all the data
    response = urllib.urlopen(stockSpecificURL).read()

    # look for the itemprop of "price" - I know the price comes right after this
    key = '<meta itemprop="price"\n        content="'

    # do some small math to figure out the start and end index of the real price:
    keyPosition = response.index(key)
    keyLength = len(key)

    start = keyPosition + keyLength
    end = response.index('"', start)

    # extract the price using a slice, and return it
    price = response[start:end]
    return price


print "Price of Apple stock is " + get_quote('aapl')
print
print "Price of Google stock is " + get_quote('goog')
print

