def myFunction():
    global someVariable    # tell Python that you are using a global variable
    someVariable = someVariable + 1

someVariable = 20
myFunction()
print someVariable
