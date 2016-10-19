# First name last name, produce directory style:

fullName = raw_input('Please enter your full name: ')
indexOfSpace = fullName.index(' ')
firstName = fullName[:indexOfSpace]
lastName = fullName[indexOfSpace + 1:]
print lastName + ', ' + firstName
