# Read grades from csv file, compute grade letter for course

import csv   # Comma separated value package

DATA_FILE_NAME = 'GradesExample.csv'

#Convert a number score to a letter grade:
def letterGrade(score):
    if score >= 90:
        letter = 'A'
    elif score >= 80:
        letter = 'B'
    elif score >= 70:
       letter = 'C'
    elif score >= 60:
        letter = 'D'
    else:
        letter = 'F'  #fall through or default case
    return letter


# Open the file in 'read Universal' (return char) mode)
# This allows for dealing with files created by spreadsheet programs like Excel
fileHandle = open(DATA_FILE_NAME, 'rU')

# Let the csv reader parse the file into rows
csvParsed = csv.reader(fileHandle)

# Treat each row (which represents data for a single student) as a list
readingHeaderLine = True
for row in csvParsed:   # iterate through each line

    if readingHeaderLine:  # first line?
        readingHeaderLine = False
        continue   #  skip the header line

    # This is what the data looks like coming in to the program
    #print 'Original: ', row
    
    name = row[0]  # save the student's name
    total = 0  # prepare to add 'em up
    for index in range(1, 8):   # elements 1 through 7 are the scores
        thisGrade = row[index]
        if thisGrade == '':   
            thisGrade = 0.0  # change a nothing to a zero
        else:
            thisGrade = float(thisGrade)  # convert score from string to float
        total = total + thisGrade
        
    percent = (total  * 100.)/ 200.   # out of a possible 200 points

    gradeToReport = letterGrade(percent)

    print name, '   Percent:', percent, '  Letter Grade:',  gradeToReport
    
fileHandle.close()  #close the file

