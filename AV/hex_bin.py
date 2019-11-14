/usr/bin/python

import binascii


#
binary_string = binascii.unhexlify(hex_string)

# Python Program - Convert Hexadecimal to Binary
hexdec = input("Enter Hexadecimal string: ")
print(hexdec," in Binary = ", end="")    # end is by default "\n" which prints a new line
for _hex in hexdec:
    dec = int(_hex, 16)    # 16 means base-16 wich is hexadecimal
    print(bin(dec)[2:].rjust(4,"0"), end="")    # the [2:] skips 0b, and the


#another implementation

input = 'ABC123EFFF'
for index, value in enumerate(input):
    print(value)
    print(bin(int(value,16)+16)[3:])

string = ''.join([bin(int(x,16)+16)[3:] for y,x in enumerate(input)])
print(string) 
