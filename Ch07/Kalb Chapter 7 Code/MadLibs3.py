# MadLib (version 3)

import random

namesList = ['Weird Al Yankovic', 'The Teenage Mutant Ninja Turtles', 'Supergirl', \
             'The Stay Puft Marshmallow Man', 'Shrek', 'Sherlock Holmes', \
             'The Beatles', 'Powerpuff Girl', 'The Pillsbury Doughboy', 'Sam-I-Am']
nNames = len(namesList)  # find out how many names are in the list of names

while True:
    nameIndex = random.randrange(0, nNames)  # Choose a random index into the namesList
    name = namesList[nameIndex]  # Use the index to choose a random name
    verb = raw_input('Enter a verb: ')
    adjective = raw_input('Enter an adjective: ')
    noun = raw_input('Enter a noun: ')
    
    sentence = name + ' ' + verb + ' through the forest, hoping to escape the ' + \
                     adjective + ' ' + noun + '.'
    print
    print sentence
    print
    
    # See if the user wants to quit or continue
    answer = raw_input('Type "q" to quit, or anything else (even Return/Enter) to continue: ')
    if answer == 'q':
        break

print 'Bye'
