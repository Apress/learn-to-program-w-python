# Get the population of a given state

statesDict = {
    'California':38802000, 'Texas':26956000, 'Florida':19893000, 'New York':19746000,\
    'Illinois': 12880000, 'Pennsylvania': 12787000, 'Ohio':11594000, 'Georgia': 10097000,\
    'North Carolina': 9943964, 'Michigan':9909000, 'New Jersey': 8938000}

while True:
    usersState = raw_input('Enter a state: ')
    if usersState == '':
        break
    if usersState in statesDict:
        population = statesDict[usersState]
        print 'The population of', usersState, 'is', population

    else:
        print 'Sorry, but we do not have any information about', usersState
    print

