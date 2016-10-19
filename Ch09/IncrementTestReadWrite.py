# Increment test

from FileReadWrite import *

# Here is a constant - the name of the data file that we will use throughout
DATA_FILE_PATH = 'CountData.txt'

# Main program - reads from file, increments a counter, writes to file

if not fileExists(DATA_FILE_PATH):
    # The file was not found, this is the first time we are running the program
    print 'First time - creating the data file.'  # for testing
    writeFile(DATA_FILE_PATH, '1')

else:
    # The file was found.  We have run this program before
    count = readFile(DATA_FILE_PATH)
    print 'Found the file, data read was: ', count  # for testing
    count = int(count)
    count = count + 1
    textToWrite = str(count)
    writeFile(DATA_FILE_PATH, textToWrite)    

    print 'This was run number:', count
    
