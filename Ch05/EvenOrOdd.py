# Determine if a given integer is even or odd:

# Function to determine if a number is even or odd
def isEven(valueIn):
    remainder = valueIn % 2
    if remainder == 0:
        return True
    else:
        return False

def printEvenOrOdd(someValue):
    if isEven(someValue):
        print someValue, 'is even'
    else:
        print someValue, 'is odd'

#Test cases
printEvenOrOdd(10)
    
printEvenOrOdd(11)
     
# Get user input and convert to an integer
userNumber = raw_input('Enter an integer: ')
userNumber = int(userNumber)

# Pass in the users number
printEvenOrOdd(userNumber)

