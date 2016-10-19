# Determine if two numbers represent a square

# Function to determine if length and width represent a square
def isSquare(length, width):

    if length == width:
        itsASquare = True
    else:
        itsASquare = False
    return itsASquare

#Test cases
result = isSquare(5, 5)
if result:
    print '5 and 5 represent a square'
else:
    print '5 and 5 do not represent a square'
    

if isSquare(7.5, 8.5):
    print '7.5 and 8.5 represent a square'
else:
    print '7.5 and 8.5 do not represent a square'


# Get user inputconvert to floats and call the function.
userLength = raw_input('Enter a length: ')
userLength = float(userLength)
userWidth = raw_input('Enter a width: ')
userWidth = float(userWidth)
if isSquare(userLength, userWidth):
    print userLength, 'and', userWidth, 'represent a square'
else:
    print userLength, 'and', userWidth, 'do not represent a square'


