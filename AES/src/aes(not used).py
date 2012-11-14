"""
AES Encryption
CSE178-Network Security
By Adrian Wang
Git Repository:
https://github.com/splinter500/AES.git
"""
import numpy
test
"""
Function that will return a 16 byte string into a 4 x 4 array
"""
def storeArray(plainBytes,counter):
    roundArry = numpy.empty((4,4),numpy.byte)
    for i in range(0,4):
        for j in range (0,4):
            if counter<countBytes:
                roundArry[j][i] = plainBytes[counter]
                counter+=1
            else:
                roundArry[j][i] = 0;
    return roundArry

"""
Initialized Variables
"""
roundArryList = [];
keyLength = 128;    #128-bit keys
numRounds = 10;     #Number of rounds
countBytes = 0;
counter = 0;
numConversion = 0;

"""
Code Starts Here
"""
plainBytes = bytearray(raw_input("Please input string to encode: "));
countBytes = plainBytes.count('')-1

if countBytes%16 != 0:
    numConversion = (countBytes/16)+1
else: 
    numConversion = (countBytes/16)

for i in range (0,numConversion):
    roundArryList.append(storeArray(plainBytes,16*i))




