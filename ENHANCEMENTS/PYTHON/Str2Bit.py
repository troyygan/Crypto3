#!/usr/bin/python

import commands
import os
import sys
from binstr import *


text = "hello"

bin_join = []



#This will convert the string to binary in array format
def strbin(s):
    binary = [ bin(ord(ch))[2:].zfill(8) for ch in s ] 
    return binary
#    for i in range(len(s)):
#        print "Element: %s %s " % (i, binary[i])

def bin_to_gray(b):
    gray_bin = b_base2_to_gray(A=b)
    return gray_bin



    

#This is to convert from bin to array

bin_array = strbin(text)

#print "Binary values of text %s: %s" % (text, bin_array)


os.system("clear")



#Joining the converted string of binary





print "---Plaintext will be converted to Base2 Binary and Gray Code--- \n"
print "Plaintext = ", text
print "Binary = ", ''.join(strbin(text))

#For looping on the binary values and convert to gray code
for i in range(len(bin_array)):
    print "Element #", i
    print "Base2 Value = ", bin_array[i]
    print "Gray Code Value = ", bin_to_gray(bin_array[i])
    print 
    

