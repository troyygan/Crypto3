#!/usr/bin/python

import os
import sys
import string


while True:
    ini_hex = raw_input("Enter Hex Value: ")
    hexa = ini_hex.replace(" ", "")
    hexa_v = ''.join([bin(int(x,16)+16)[3:] for y,x in enumerate(hexa)])
    print "Hexa Value: ", hexa_v
    continue
