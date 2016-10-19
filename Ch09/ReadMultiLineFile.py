# Read in multiple lines of text from a file

from FileReadWrite import *

DATA_FILE_PATH = 'MultiLineData.txt'

myFileHandle = openFileForReading(DATA_FILE_PATH)

data1 = readALine(myFileHandle)
print data1
data2 = readALine(myFileHandle)
print data2
data3 = readALine(myFileHandle)
print data3
# Could add code to split data3 into several different pieces of data

closeFile(myFileHandle)
