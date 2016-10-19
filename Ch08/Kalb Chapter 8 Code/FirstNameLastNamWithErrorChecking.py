# Read in first name last name, produce directory style with error detection

while True:
    fullName = raw_input('Please enter your full name: ')
    fullName = fullName.strip()     # remove any spaces before or after
    nSpaces = fullName.count(' ')
    if nSpaces == 1:  # OK if there is a single space
        break
    print 'Please try again.  Enter your name as first name, space, last name'
    print
    
indexOfSpace = fullName.index(' ')

firstName = fullName[:indexOfSpace]
firstName = firstName[0].upper() + firstName[1:]   # Force first letter to uppercase

lastName = fullName[indexOfSpace + 1:]
lastName = lastName[0].upper() + lastName[1:]   # Force first letter to uppercase

print lastName + ', ' + firstName

 
