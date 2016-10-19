# Write multiple lines of text to a file

from FileReadWrite import *

DATA_FILE_PATH = 'MultiLineData.txt'

myFileHandle = openFileForWriting(DATA_FILE_NAME)

data1 = 'Here is some data as a string'
writeALine(myFileHandle, data1)
data2 = 'Here is a second line of string data'
writeALine(myFileHandle, data2)

# Could have some code join several pieces of data into a single string
data3 = '123,Joe Schmoe,123.45,0'
writeALine(myFileHandle, data3)

closeFile(myFileHandle)
