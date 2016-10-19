# Determine if two numbers represent a square

# Function to determine if length and width represent a square
def isSquare(length, width):

    if length == width:
        itsASquare = True
    else:
        itsASquare = False
    return itsASquare

# Intermediate function that checks for a square and prints the result
def printSquare(aLength, aWidth):
    theResult = isSquare(aLength, aWidth)
    if theResult:
        print aLength, 'and', aWidth, 'represent a square'
    else:
        print aLength, 'and', aWidth, 'do not represent a square'

        
#Test cases
printSquare(5, 5)

printSquare(7.5, 8.5)

# Get user inputconvert to floats and call the function.
userLength = raw_input('Enter a length: ')
userLength = float(userLength)
userWidth = raw_input('Enter a width: ')
userWidth = float(userWidth)
printSquare(userLength, userWidth)

