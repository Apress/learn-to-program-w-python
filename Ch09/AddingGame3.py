# Adding game version 3
# Save only the score

import random
from FileReadWrite import *    # means import everything as though it were typed here

DATA_FILE_PATH = 'GameData.txt'

# Start up code
if not fileExists(DATA_FILE_PATH):
    score = 0
    print 'Hi, and welcome to the adding game.'
else:
    score = readFile(DATA_FILE_PATH)
    score = int(score)
    print 'Welcome back.  Your saved score is:', score

# Main loop
        
while True:
    firstNumber = random.randrange(0, 11)
    secondNumber = random.randrange(0, 11)
    correctAnswer = firstNumber + secondNumber
    
    question = 'What is:  ' + str(firstNumber) + ' + ' + str(secondNumber) + '?  '
    userAnswer = raw_input(question)
    if userAnswer == '':
        break

    userAnswer = int(userAnswer)

    if userAnswer == correctAnswer:
        print 'Yes, you got it!'
        score = score + 2

    else:
        print 'No, sorry, the correct answer was:  ', correctAnswer
        score = score - 1

    print 'Your current score is: ', score
    print

writeFile(DATA_FILE_PATH, str(score))
print 'Thanks for playing' 
