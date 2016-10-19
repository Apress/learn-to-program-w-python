# Get weather data from openweathermap.org - as XML

import urllib
import xml.etree.ElementTree as etree

# API documentation from:  http://openweathermap.org/API

# Go to openweathermap.org, get an API Key, and paste it between the quotes below'
API_KEY = ''

def getInfo(city):
   
    urlWithParams = 'http://api.openweathermap.org/data/2.5/weather?q='\
                             + city + '&mode=xml' + '&APPID=' + API_KEY
    
    # Make the request and save the response as an XML-formatted string.
    responseAsXML = urllib.urlopen(urlWithParams).read()

    # Turn the string into an XML tree
    tree = etree.fromstring(responseAsXML)

    # Find the temperature node, then get the value attribute inside it
    temperatureInfo =  tree.find('temperature')
    degrees = temperatureInfo.attrib['value']
    
    return float(degrees)

# Convert from Kelvin degrees to Fahrenheit
def convertKToF(degreesK):
    degreesF = (1.8 * (degreesK - 273.)) + 32
    return degreesF


while True:
    city = raw_input('What city would you like the temperature of? ')
    if city == '':
        break
    tempK = getInfo(city)

    tempF = convertKToF(tempK)
    print tempF
    print






