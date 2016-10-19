# Absolute Value Program

# Function to generate the absolute value of a number
def absoluteValue(valueIn):
    if valueIn >= 0 :
        valueOut = valueIn
    else:
        valueOut = -1 * valueIn
    return valueOut

#Test cases
result = absoluteValue(10.5)
print 'The absolute value of 10.5 is', result
    
result = absoluteValue(-8)
print 'The absolute value of -8 is', result
    
