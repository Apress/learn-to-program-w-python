def myFunction(aVariable):
    aVariable = aVariable + 1  # change a local (parameter) variable
    return aVariable    # and return it

someVariable = 20
someVariable = myFunction(someVariable)  # pass in global, and re-assign the the answer
print someVariable

