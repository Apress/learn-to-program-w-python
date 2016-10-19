# Pizza toppings program

# Function to show the list of toppings
def showPizzaToppings(theList):
    print 
    if len(theList) == 0:
        print 'Your pizza has no toppings.'
    else:
        print 'The toppings on your pizza are:'
        print
        for thisItem in theList:  # iterate through the list, print each item
            print '   ' + thisItem
    print #blank line

#main code
print 'Welcome to my Pizzeria, where you get to choose your toppings.'
print 'When prompted, enter the first letter or the full word what you want to do.'
print 
print '---- Operations ----'
print 'a/add           Add a topping'
print 'c/change      Change a topping'
print 'o/order         Order the pizza'
print 'q/quit           Quit'
print 'r/remove       Remove a topping'
print 's/startover    Start over'
print

toppingsList = [ ]  #begin as an empty list
while True:

    print 'What would you like to do?'
    menuChoice = raw_input('   add, change, order, quit, remove, startover: ')
    
    if (menuChoice == 'a') or (menuChoice == 'add'):  #add a topping
        newTopping = raw_input('Type in a topping to add: ')
        toppingsList.append(newTopping)  #append adds to the end of a list
        
    elif (menuChoice == 'c') or (menuChoice == 'change'):  #change a topping
        oldTopping = raw_input('What topping would you like to change: ')
        if oldTopping in toppingsList:  # is it in the list
            index = toppingsList.index(oldTopping)  #find out where it is in the list
            newTopping = raw_input('What is the new topping: ')
            toppingsList[index] = newTopping   # set a new value at that index
        else:
            print oldTopping, 'was not found.'

    elif (menuChoice == 'o') or (menuChoice == 'order'):  #order the pizza
        showPizzaToppings(toppingsList)
        print
        print 'Thanks for your order!'
        print 
        another = raw_input('Would you like to order another pizza (y/n) ? ')
        if another == 'y':
            toppingsList = [ ]  #reset to the empty list
        else:
            break

    elif (menuChoice == 'q') or (menuChoice == 'quit'): #quit
        break
    
    elif (menuChoice == 'r') or (menuChoice == 'remove'):  #remove a topping
        delTopping = raw_input('What topping would you like to remove: ')
        if delTopping in toppingsList:  #check to see if the topping is in our list
            index = toppingsList.index(delTopping)  # find out where it is
            toppingsList.pop(index)    # remove it
             # The code above only removes the first occurrence of the topping.  
        else:
            print delTopping, 'was not found'
            
    elif (menuChoice == 's') or (menuChoice == 'startover'):  #reset to no toppings
        print "OK, let's start over."
        toppingsList = [ ]  #reset to the empty list

    else:
        print "Uh ... sorry, I'm not sure what you said, please try again."

    showPizzaToppings(toppingsList)  # show the list of toppings on the pizza
 
print
print 'Goodbye'
