#!/usr/bin/python

import commands
import os
import sys
from binstr import *



def bin_to_gray(b):
    bin2gray = b_base2_to_gray(A=b)
    return bin2gray


while True:
    ini_bin = raw_input("Enter Binary: ")
    result = bin_to_gray(ini_bin)
    print "Gray Code Value: ", result
    continue






