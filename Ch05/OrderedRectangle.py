# Determine if the four side lengths represent a Rectangle or not:

# Function to determine if four sides represent a Rectangle
# Is a rectangle if left is the same as the right
# and top is the same as the bottom
def isRectangle(left, top, right, bottom):
    if left == right:
        if top == bottom:
            return True
    return False

def printRectangle(someLeft, someTop, someRight, someBottom):
    if isRectangle(someLeft, someTop, someRight, someBottom):
        print someLeft, someTop, someRight, someBottom, 'represents a rectangle'
    else:
        print someLeft, someTop, someRight, someBottom, 'does not represent  a rectangle'

#Test cases
printRectangle(5, 6, 5, 6)
    
printRectangle(5, 6, 7, 8)

# Get user input and call the function.
userLeft = raw_input('Enter the left: ')
userLeft = int(userLeft)
userTop = raw_input('Enter the top: ')
userTop = int(userTop)
userRight = raw_input('Enter the right: ')
userRight = int(userRight)
userBottom = raw_input('Enter the bottom: ')
userBottom = int(userBottom)

printRectangle(userLeft, userTop, userRight,  userBottom)


