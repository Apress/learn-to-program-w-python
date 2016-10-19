# MadLib (version 5)

import random

def chooseRandomFromList(aList):
    nItems = len(aList)
    randomIndex = random.randrange(0, nItems)
    randomElement = aList[randomIndex]
    return randomElement

namesList = ['Weird Al Yankovic', 'The Teenage Mutant Ninja Turtles', 'Supergirl', \
             'The Stay Puft Marshmallow Man', 'Shrek', 'Sherlock Holmes', \
             'The Beatles', 'Powerpuff Girl', 'The Pillsbury Doughboy', 'Sam-I-Am']
verbsList = ['screamed', 'burped', 'ran', 'galumphed', 'rolled', 'ate', 'laughed', \
                  'complained', 'whistled']
adjectivesList = ['purple', 'giant', 'lazy', 'curly-haired', 'wireless electric', \
                  'ten foot tall']
nounsList = ['ogre', 'dinosaur', 'Frisbee', 'robot', 'staple gun', 'hot dog vendor', \
                  'tortoise', 'rodeo clown', 'unicorn', 'Santa hat', 'garbage can']

while True:
    name = chooseRandomFromList(namesList) 
    verb = chooseRandomFromList(verbsList)
    adjective = chooseRandomFromList(adjectivesList)
    noun = chooseRandomFromList(nounsList)
    
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
