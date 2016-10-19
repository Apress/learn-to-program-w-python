# Calculate the total of numbers up to a number entered by the user

usersNumber = raw_input('Please enter an integer: ')
usersNumber = int(usersNumber)
highEndOfRange = usersNumber + 1

total = 0
for number in range(1, highEndOfRange):
    total = total + number

print 'The total numbers from 1 to', usersNumber, 'is', total
    
