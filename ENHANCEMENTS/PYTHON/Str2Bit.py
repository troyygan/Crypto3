#!/usr/bin/python

def strbin(s):
    binary = [ bin(ord(ch))[2:].zfill(8) for ch in s ] 
    print "Binary Value: ", binary
#    for i in range(len(s)):
#        print "Element: %s %s " % (i, binary[i])

strbin("aaaaaaaa")
