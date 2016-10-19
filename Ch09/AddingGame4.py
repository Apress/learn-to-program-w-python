# Adding Game version 4
# Saving lots of data

import random
from FileReadWrite import *    # means import everything as though it were typed here

DATA_FILE_PATH = 'AddingGameData.txt'


#  Main program starts here
    
if not fileExists(DATA_FILE_PATH):
    userName = raw_input('You must be new here, please enter your name:  ')
    score = 0
    nProblems = 0
    nCorrect = 0

    print 'To quit the game, press RETURN/ENTER and your info will be saved'
    print 'OK', userName, "let's get started ..."
    print

else:
    savedDataString = readFile(DATA_FILE_PATH)  #read the whole file into a variable
    savedDataList = savedDataString.split(',')  # turn that into a list
    userName = savedDataList[0]
    score = savedDataList[1]
    score = int(score)
    nProblems = savedDataList[2]
    nProblems = int(nProblems)
    nCorrect = int(savedDataList[3])  # can do both in a  combined step
    
    print 'Welcome back', userName, 'nice to see you again! '
    print 'Your current score is: ', score
    print


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
    nProblems = nProblems + 1

    if userAnswer == correctAnswer:
        print 'Yes, you got it!'
        score = score + 2
        nCorrect = nCorrect + 1

    else:
        print 'No, sorry, the correct answer was:  ', correctAnswer
        score = score - 1

    print 'Your current score is: ', score
    print


print 'Thanks for playing'
print
print 'You have tried', nProblems, 'problems and you have correctly answered', nCorrect    

# Make a list of the useruserName,  userScore, nProblems, nCorrect then
# create a string from that using join
dataList = [userName, str(score), str(nProblems), str(nCorrect)] 
outputText = ','.join(dataList)

writeFile(DATA_FILE_PATH, outputText)    
