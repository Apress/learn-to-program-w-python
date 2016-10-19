# Get temperature for a given city

import urllib
import json

# API documentation from:  http://openweathermap.org/API

# Go to openweathermap.org, get an API Key, and paste it between the quotes below'
API_KEY = ''

def getTemperature(city):
   
    urlAndParams = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&mode=json'+ '&APPID=' + API_KEY
    
    # Make the request and save the response as a string.
    response = urllib.urlopen(urlAndParams).read()

    responseDict = json.loads(response)  # convert from JSON to a Python dictionary

    mainDict = responseDict['main']  # get the information associated with the main key
    
    degrees = mainDict['temp']   # get the temperature from that dictionary
    
    return float(degrees)


# Convert from Kelvin degrees to Fahrenheit
def convertKToF(degreesK):
    degreesF = (1.8 * (degreesK - 273.)) + 32
    return degreesF


while True:
    city = raw_input('What city would you like the temperature of? ')
    if city == '':
        break
    tempK = getTemperature(city)
    tempF = convertKToF(tempK)
    print tempF
    print 




