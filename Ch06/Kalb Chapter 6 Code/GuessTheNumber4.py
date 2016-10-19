# Guess the Number  (version 4)

import random

MAX_GUESSES = 5  # maximum number of guesses allowed
MAX_RANGE = 20 # highest possible number

#Show introduction
print 'Welcome to my Guess the Number program.'
print 'Guess my number between 1 and', MAX_RANGE
print 'You will have', MAX_GUESSES, 'guesses.'

def playOneRound():
    #Choose random target
    target = random.randrange(1, MAX_RANGE + 1)

    #Initialize a guess counter
    guessCounter = 0

    #Loop forever
    while True:
        #Ask the user to for a guess
        userGuess = raw_input('Take a guess: ')
        userGuess = int(userGuess)

        #Increment guess counter
        guessCounter = guessCounter + 1

        #If user's guess is correct, congratulate user, we're done
        if userGuess == target:
            print 'You got it!'
            print 'It only took you', guessCounter, 'guess(es).'
            break

        #If user's guess is too low, tell user
        elif userGuess < target:
            print 'Your guess was too low.'
            
        #If user's guess is too high, tell user
        else:
            print 'Your guess was too high.'
            
        #If reached max guesses, tell answer correct answer, we're done.
        if guessCounter == MAX_GUESSES:
            print 'Sorry, you did not get it in', MAX_GUESSES, 'guesses.'
            print 'The number was:', target
            break

#main code
while True:
    playOneRound()  # call a function to play one round of the game
    goAgain = raw_input('Play again? (Press ENTER to continue, or q to quit): ')
    if goAgain == 'q':
        break

print 'Thanks for playing.'
