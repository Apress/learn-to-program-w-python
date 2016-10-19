def F2C(nDegreesF):
    nDegreesF = (nDegreesF - 32) * 0.5556
    return nDegreesF


def C2F(nDegreesC):
    nDegreesF = (1.8 * nDegreesC) + 32
    return nDegreesF

Given these function definitions, we can now build some main code to use these functions interactively.  We can ask the user for a temperature in each scale, then convert and print it in the other scale.

# Code to ask the user to input values for conversion:

usersTempF = raw_input('Enter a value of degrees Fahrenheit: ')
usersTempF = float(usersTempF)
convertedTempC = F2C(usersTempF)
print usersTempF, 'degrees Fahrenheit is:', convertedTempC, 'degrees Centigrade.'

usersTempC = raw_input('Enter a value of degrees Celsius: ')
usersTempC = float(usersTempC)
convertedTempF = C2F(usersTempC)
print usersTempC, 'degrees Centigrade is:', convertedTempF, 'degrees Fahrenheit.'

