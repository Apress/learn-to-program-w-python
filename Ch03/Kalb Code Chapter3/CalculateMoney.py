# Calculate the amount of money interactively

# Use raw_input to get info from the user
nOnes = raw_input('How many ones do you have? ')
nFives = raw_input('How many fives do you have? ')
nTens = raw_input('How many tens do you have? ')
nTwenties = raw_input('How many twenties do you have? ')

# Use int to convert the inputted strings to integer values before multiplying
total = int(nOnes) + (int(nFives) * 5) + (int(nTens) * 10) + (int(nTwenties) * 20)

# Use str to convert to a string, then concatenate on a decimal point and zeros
totalAsString = str(total) + '.00'

# Concatentate strings and print
print 'You have $' + totalAsString
