# MadLib (version 4)

import random

namesList = ['Weird Al Yankovic', 'The Teenage Mutant Ninja Turtles', 'Supergirl', \
             'The Stay Puft Marshmallow Man', 'Shrek', 'Sherlock Holmes', \
             'The Beatles', 'Powerpuff Girl', 'The Pillsbury Doughboy', 'Sam-I-Am']
nNames = len(namesList)  # find out how many names are in the list of names
verbsList = ['screamed', 'burped', 'ran', 'galumphed', 'rolled', 'ate', 'laughed', \
                  'complained', 'whistled']
nVerbs = len(verbsList)
adjectivesList = ['purple', 'giant', 'lazy', 'curly-haired', 'wireless electric', \
                  'ten foot tall']
nAdjectives = len(adjectivesList)
nounsList = ['ogre', 'dinosaur', 'Frisbee', 'robot', 'staple gun', 'hot dog vendor', \
                  'tortoise', 'rodeo clown', 'unicorn', 'Santa hat', 'garbage can']
nNouns = len(nounsList)

while True:
    nameIndex = random.randrange(0, nNames)  # Choose a random index into the namesList
    name = namesList[nameIndex]  # Use the index to choose a random name
    verbIndex = random.randrange(0, nVerbs)  
    verb = verbsList[verbIndex]  
    adjectiveIndex = random.randrange(0, nAdjectives)  
    adjective = adjectivesList[adjectiveIndex]  
    nounIndex = random.randrange(0, nNouns)  
    noun = nounsList[nounIndex]  
    
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
