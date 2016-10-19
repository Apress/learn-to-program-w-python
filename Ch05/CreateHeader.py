# Create Header 

def createHeader(fullName, gender):

    if gender == 'm':
        title = 'Mr.'
    elif gender == 'f':
        title = 'Ms.'
    else:    #not sure, could be male or female
        title = 'Mr. or Ms.'
    header = 'Dear ' + title + ' ' + fullName + ',' # use concatenation
    return header


print createHeader('Joe Smith', 'm') 
print createHeader('Susan Jones', 'f') 
print createHeader('Henry Jones', 'm') 
print createHeader('Chris Smith', '?')  #  Not sure if this is male or female
