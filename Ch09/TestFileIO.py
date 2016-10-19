# FileReadWrite.py
# Functions for checking if a file exists, read from a file, write to a file

import os

def fileExists(filePath):
    exists = os.path.exists(filePath)
    return exists

def readFile(filePath):
    if not fileExists(filePath):
        print 'The file, ' + filePath + ' does not exist - cannot read it.'
        return ''

    fileHandle = open(filePath, 'r')
    data = fileHandle.read()
    fileHandle.close()
    return data
        

def writeFile(filePath, textToWrite):
    fileHandle = open(filePath, 'w')
    fileHandle.write(textToWrite)
    fileHandle.close()


DATA_FILE_PATH = 'TestData.txt'  # path to the file as a constant

stringToWriteOutToFile = 'abcdefghijkl'   # contents could be anything, this is just a test
writeFile(DATA_FILE_PATH, stringToWriteOutToFile)

stringReadInFromFile = readFile(DATA_FILE_PATH)
print 'Read in: ', stringReadInFromFile
