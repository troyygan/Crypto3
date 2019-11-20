#!/usr/bin/python

import os
import sys
import string

ini_cip_b = raw_input("Enter Ciphertext in Binary: ")
ini_cip_g = raw_input("Enter Ciphertext in Gray: ")

cip_b = ini_cip_b.replace(" ", "")
cip_g = ini_cip_g.replace(" ", "")

#cip_b = 'E4673CAE4026AE9C75C7816A2DC242B6'

#for index, value in enumerate(input):
#    r = (bin(int(value,16)+16)[3:])
#    return r

bin_b = ''.join([bin(int(x,16)+16)[3:] for y,x in enumerate(cip_b)])
bin_g = ''.join([bin(int(x,16)+16)[3:] for y,x in enumerate(cip_g)])


print "Value of Ciphertext in Binary: ", bin_b

print" Value of Ciphertext in GrayCode: ", bin_g


####XOR 


ava = b'bin_b ^ bin_g'
print ava
#ava_percent = ava / 128

#print "Avalance Value = %s = %s\% " % (ava, ava_percent)

