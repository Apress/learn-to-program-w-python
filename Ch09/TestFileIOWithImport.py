# FileReadWrite.py
# Functions for checking if a file exists, read from a file, write to a file

from FileReadWrite import *


DATA_FILE_PATH = 'TestData.txt'  # path to the file as a constant

stringToWriteOutToFile = 'abcdefghijkl'   # contents could be anything, this is just a test
writeFile(DATA_FILE_PATH, stringToWriteOutToFile)

stringReadInFromFile = readFile(DATA_FILE_PATH)
print 'Read in: ', stringReadInFromFile
