# Guess the Number  (version 2)

#Show introduction
#Choose random target
target = 10     # start with a known value

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
    if guessCounter == 5:
        print 'Sorry, you did not get it in 5 guesses'
        print 'The number was:', target
        break

print 'Thanks for playing.'
