#  Function to determine shipping cost, based on country and quantity
def calculateShipping(country, nWidgets):

    if (country == 'USA') or (country == 'US') or (country == 'United States'):
        if nWidgets < 50:
            shippingCost = 6.25
        elif nWidgets < 100:
            shippingCost = 9.50
        elif nWidgets < 150:
            shippingCost =12.75
        else:
            shippingCost = 15.00

    elif country == 'Canada':
        if nWidgets < 50:
            shippingCost = 8.25
        elif nWidgets < 100:
            shippingCost = 12.50
        elif nWidgets < 150:
            shippingCost = 18.00
        else:
            shippingCost = 25.00

    else:
        shippingCost = -1  #  special value to say that we don't ship to this country

    return shippingCost


# Get user input then call the above function
userWidgets = raw_input('How many widgets are you buying? ')
userWidgets = int(userWidgets) # convert to integer

userCountry = raw_input('What country are you shipping to? ')
# Other questions about the shipment here


#call the function to see how much it will cost to ship
amountForShipping = calculateShipping(userCountry, userWidgets)
if amountForShipping >= 0:
    print 'It will cost $', amountForShipping, 'to ship your package'
    # more code here to process the shipment
else:
    print 'Sorry, we do not ship to', userCountry
    

    

