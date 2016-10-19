# Powerball Checker - how much did we win?

import urllib
import sys

POWERBALL_URL = 'http://www.powerball.com/powerball/winnums-text.txt'
MAX_REGULAR_NUMBER = 69
MAX_POWERBALL_NUMBER = 26


def getIntegerInRange(prompt, theMin, theMax):
    while True:
        number = raw_input(prompt)
        if number == '':
            print 'OK, bye'
            sys.exit()
        try:
            number = int(number)
        except:
            print 'That is not an integer, please try again.'
        if (number < theMin) or (number > theMax):
            print 'That is not in the range of', theMin, 'to', theMax
        else:
            return number


print "Welcome to my PowerBall checker.  Getting the latest draw ..."
print

allDrawnData = urllib.urlopen(POWERBALL_URL).read()
allDrawnData = allDrawnData.split("\n") # then split it into lines

# drawnData[0] is a header line of the text:  Draw Date   WB1 WB2 WB3 WB4 WB5 PB  PP

mostCurrentDrawLine = allDrawnData[1]  # this is the line we care about
drawnList = mostCurrentDrawLine.split('  ')  # split into a list

mostRecentDrawDate = drawnList[0]  # element zero is the date
numbersDrawnList = []
for i in range(1, 6):  # elements 1 through 5 are the data we want
    numbersDrawnList.append(int(drawnList[i]))
numbersDrawnList.sort()
powerBallDrawn = int(drawnList[6])  # element 6 is the powerball


print 'The latest draw on ' + mostRecentDrawDate + ' was:'
print 
for value in numbersDrawnList:
    print ' ' + str(value),  # comma here means stay on the same line
print ' PowerBall:  ', powerBallDrawn


#  Allow the user to enter sets of PowerBall numbers from one ticket

while True:
    print
    print "OK, let's see how much you've won from your ticket(s)."
    userList = []
    while True:
        thisNumber = getIntegerInRange('Enter a number: ', 1, MAX_REGULAR_NUMBER)
        if thisNumber in userList:
            print 'Hey, you already entered that number.'
        else:
            userList.append(thisNumber)
            if len(userList) == 5:  # When we have 5 numbers, we're done
                break

    userPowerBall = getIntegerInRange('Enter your powerball number: ', 1, MAX_POWERBALL_NUMBER)
    print

    matchList = []
    for userNumber in userList:
        if userNumber in numbersDrawnList:
            matchList.append(userNumber)

    nMatches = len(matchList)  # See how many matches there were
    if powerBallDrawn == userPowerBall:
        powerBallMatch = True
    else:
        powerBallMatch = False

    if nMatches == 1:
        print 'You matched 1 number:', matchList[0]
    else:
        print 'You matched', nMatches, 'numbers:',
        for number in matchList:
            print ' ', number,
        print
    if powerBallMatch:
        print '... and you matched the power ball!'

    if nMatches == 5:
        if powerBallMatch:
            print 'You won the WHOLE ENCHILADA!  Time to quit your job!'
        else:
            print 'You won a million dollars!'
    elif nMatches == 4:
        if powerBallMatch:
            print 'You won $50,000'
        else:
            print 'You won $100'
    elif nMatches == 3:
        if powerBallMatch:
            print 'You won $100'
        else:
            print 'You won $7'
    elif nMatches == 2:
        if powerBallMatch:
            print 'You won $7'
        else:
            print 'You won $4'
    elif powerBallMatch:
        print 'You won $4'
    else:
        print 'Sorry Charlie, you lost it all'

    print

        


