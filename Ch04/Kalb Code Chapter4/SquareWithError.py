def square(number):
    answer = number * number
    return     #  Note: this is an error, does not return an answer


userNumber = raw_input('Enter a number: ')
userNumber = float(userNumber)   # convert to a float
numberSquared = square(userNumber)   # call the function and save the result
print 'The square of your number is', numberSquared
