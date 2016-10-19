# Adding game version 2

import random

score = 0

# Main loop        
while True:
    firstNumber = random.randrange(0, 11)
    secondNumber = random.randrange(0, 11)
    correctAnswer = firstNumber + secondNumber
    
    question = 'What is:  ' + str(firstNumber) + ' + ' + str(secondNumber) + '?  '
    userAnswer = raw_input(question)
    if userAnswer == '':
        break  # user wants to quit
    
    userAnswer = int(userAnswer)

    if userAnswer == correctAnswer:
        print 'Yes, you got it!'
        score = score + 2

    else:
        print 'No, sorry, the correct answer was:  ', correctAnswer
        score = score - 1

    print 'Your current score is: ', score
    print

print 'Thanks for playing' 
