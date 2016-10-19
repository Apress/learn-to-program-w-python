# Multiple choice test

import random
from FileReadWrite import *

FILE_PATH = 'MultipleChoiceQuestions.txt'
LETTERS_LIST = ['a', 'b', 'c', 'd']

# Open the file for reading, read in the title line
fileHandle = openFileForReading(FILE_PATH)
titleText = readALine(fileHandle)

# Find out how many questions there will be
nQuestions = readALine(fileHandle)
nQuestions = int(nQuestions) 

print 'Welcome!  This test is:'
print
print titleText  # print whatever title we got from the file
print
print 'There will be', nQuestions, 'questions.'
print
print "Let's go ..."
print

score = 0
# Each time through the loop, handle a single question
for questionNumber in range(0, nQuestions):
    questionText = readALine(fileHandle)  # read a line of a question
    
    answers =[]
    for i in range(0, 4):
        thisAnswer = readALine(fileHandle)  # read each answer
        answers.append(thisAnswer)
   
    correctAnswer = answers[0]  # save away the correct answer
    random.shuffle(answers)  # randomize the 4 answers
    indexOfCorrectAnswer = answers.index(correctAnswer) # see where the correct answer is 

    # present the question and the four randomized answers
    print
    print str(questionNumber + 1) +'. ' + questionText #ask question
    for index in range(0, 4): 
        thisLetter = LETTERS_LIST [index]
        thisAnswer = answers[index]
        thisAnswerLine = '' + thisLetter  + ')  ' + thisAnswer
        print thisAnswerLine    
    
    print

    # Ensure that the user enters a valid letter answer
    while True:
        userAnswer = raw_input('Your answer (a, b, c, or d): ')
        userAnswer = userAnswer.lower()  # convert usersAnswer to lowercase
        if userAnswer in LETTERS_LIST:  # valid answer
            break   
        else:  # invalid answer
            print 'Please enter a, b, c, or d'
        
    # Find the index associated with the user's answer
    # The following maps a to 0, b to 1, c to 2, d to 3
    indexOfUsersAnswer = LETTERS_LIST.index(userAnswer)

    # Give feedback
    if indexOfCorrectAnswer == indexOfUsersAnswer:
        score = score + 1
        print 'Correct!'        
    else:
        print "Sorry, that's not it."
        correctLetter = LETTERS_LIST[indexOfCorrectAnswer]
        print 'The correct answer was: ', correctLetter + ')  ' + correctAnswer
        
    print
    print 'Your score is:', score 

# Done, show the percent correct and close the file
pctCorrect = (score * 100.)/ nQuestions
print
print 'All done!    You got:', str(pctCorrect) + '% correct'

closeFile(fileHandle)
