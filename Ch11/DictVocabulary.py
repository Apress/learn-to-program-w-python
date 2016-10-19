# Using a dictionary to represent a dictionary of programming terms

programmingDict = {
    'variable': 'A named memory location that holds a value',
    'loop' : 'A block of code that is repeated until a certain condition is met.',
    'function' : 'A series of related steps that form a larger task, often called from multiple places in a program',
    'constant' : 'A variable whose value does not change',
    'Boolean' : 'A data type that can only have values of True or False'}

while True:
    print
    usersWord = raw_input('Enter a word to look up (or Return to quit): ')
    if usersWord == '':
        break
    
    if usersWord in programmingDict:
        definition = programmingDict[usersWord]
        print 'The definition of', usersWord, 'is:'
        print definition

    else:
        print
        print 'The word', usersWord, 'is not in our dictionary.'
        yesOrNo = raw_input('Would you like to add a definition for ' + usersWord + ' (y/n) ')
        if yesOrNo.lower() == 'y':
            usersDefinition = raw_input('Please give a defintion for ' + usersWord + ': ')
            programmingDict[usersWord] = usersDefinition
            print 'Thanks, got it!'
     
print 'Done.'
