# Assumes that values passed in could be values representing strings
def calculateHypotenuse(side1, side2):
    side1= float(side1)
    side2 = float(side2)
    hypot = ((side1 ** 2) + (side2 ** 2)) ** 0.5
    return hypot

firstTriangleSide1 = raw_input('Enter side 1: ')
firstTriangleSide2 = raw_input('Enter side 2: ')
hypot1 = calculateHypotenuse(firstTriangleSide1, firstTriangleSide2) # call function to do calc

secondTriangeSide1 = raw_input('Enter the first side: ')
secondTriangeSide2 = raw_input('Enter second side: ')
hypot2 = calculateHypotenuse(secondTriangeSide1, secondTriangeSide2) # call function to do calc

print 'The hypotenuse of the first triangle is: ', hypot1
print 'The hypotenuse of the second triangle is: ', hypot2
