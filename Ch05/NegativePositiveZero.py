# Determine if a number is negative, positive, or zero

# Function to determine negative, positive, or zero
# Returns an appropriate string
def negativePositiveZero(value):

    if value < 0.0:
        answer = 'negative'
    elif value > 0.0:
        answer = 'positive'
    else:   # not negative, not positive, must be zero
        answer = 'zero'
    return answer

#Test cases
result = negativePositiveZero(-25.7)
print '-25.7 is', result
    
result = negativePositiveZero(0.0)
print '0.0 is', result

result = negativePositiveZero(123.45)
print '123.45 is', result


# Get user input and call the function.
userValue = raw_input('Enter a number: ')
userValue = float(userValue)
userResult = negativePositiveZero(userValue)
print userValue, 'is', userResult



