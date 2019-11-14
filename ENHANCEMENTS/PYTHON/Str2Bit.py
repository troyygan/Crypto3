#!/uisr/bin/python

import commands
import os
from binstr import *









#This will convert the string to binary in array format
def strbin(s):
    binary = [ bin(ord(ch))[2:].zfill(8) for ch in s ] 
    print "Binary Value: ", binary
#    for i in range(len(s)):
#        print "Element: %s %s " % (i, binary[i])

def bin_to_gray():
    


