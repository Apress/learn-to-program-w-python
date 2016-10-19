# Calculate sum - repeated 

def calculateSum(target):
    total = 0
    nextNumberToAddIn = 1
    while nextNumberToAddIn <= target:
        # add in the next value
        total = total + nextNumberToAddIn
        #increment 
        nextNumberToAddIn = nextNumberToAddIn + 1
    return total


answer = 'y'
while answer == 'y':
    usersTarget = raw_input('Enter a target number: ')
    usersTarget = int(usersTarget)
    thisTotal = calculateSum(usersTarget)
    print 'The sum of the numbers 1 to', usersTarget, 'is:', thisTotal

    answer = raw_input('Do you want to try again (y or n): ')

print 'OK Bye'
