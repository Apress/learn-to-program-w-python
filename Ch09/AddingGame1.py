# Adding game version 1

import random

firstNumber = random.randrange(0, 11)
secondNumber = random.randrange(0, 11)
correctAnswer = firstNumber + secondNumber
    
question = 'What is:  ' + str(firstNumber) + ' + ' + str(secondNumber) + '?  '
userAnswer = raw_input(question)
userAnswer = int(userAnswer)

if userAnswer == correctAnswer:
    print 'Yes, you got it!'

else:
    print 'No, sorry, the correct answer was:  ', correctAnswer

