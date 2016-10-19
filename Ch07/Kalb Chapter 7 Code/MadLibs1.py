# MadLib (version 1)

while True:
    name = raw_input('Enter a name: ')
    verb = raw_input('Enter a verb: ')
    adjective = raw_input('Enter an adjective: ')
    noun = raw_input('Enter a noun: ')
    
    sentence = name + ' ' + verb + ' down the hill, hoping to escape the ' + \
                     adjective + ' ' + noun + '.'
    print
    print sentence
    print
    
    # See if the user wants to quit or continue
    answer = raw_input('Type "q" to quit, or anything else (even Return/Enter) to continue: ')
    if answer == 'q':
        break

print 'Bye'
