# Guess the Number  (version 1)

#Show introduction
#Choose random target
target = 10     # start with a known value
#Initialize a guess counter

#Loop forever
#Ask the user to for a guess
userGuess = raw_input('Take a guess: ')
userGuess = int(userGuess)

#Increment guess counter
#If user's guess is correct, congratulate user, we're done
if userGuess == target:
    print 'You got it!'

#If user's guess is too low, tell user
elif userGuess < target:
    print 'Your guess was too low.'
    
#If user's guess is too high, tell user
else:
    print 'Your guess was too high.'
    
#If reached max guesses, tell answer correct answer, we're done.
