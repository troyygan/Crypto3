#!/usr/bin/python3

####It will be implemented in PYTHON3
###There is an installation with gmpy2
## apt install libmpc-dev
## apt install python3-pi
## pip3 install --user gmpy2==2.1.0a2




from Crypto.Util.number import *
from Crypto import Random
import Crypto
import gmpy2
import sys

bits=1023
msg="Hello"


def strbin(s):
    binary = [ bin(ord(ch))[2:].zfill(8) for ch in s ]
    print("Binary Value: ", binary)

strbin(msg)





if (len(sys.argv)>1):
        msg=str(sys.argv[1])
if (len(sys.argv)>2):
        bits=int(sys.argv[2])

p = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
q = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)

print("Value of P:\n ", long_to_bytes(p))
print("Value of Q:\n ", q)


n = p*q
PHI=(p-1)*(q-1)

e=65537
d=(gmpy2.invert(e, PHI))

m=  bytes_to_long(msg.encode('utf-8'))
print("Value of Message after bytes_to_long and encode as utf-8\n ", m)

c=pow(m,e, n)
res=pow(c,d ,n)


print("Message=%s\np=%s\nq=%s\n\nd=%d\ne=%d\nN=%s\n\nPrivate key (d,n)\nPublic key (e,n)\n\ncipher=%s\ndecipher=%s" % (msg,p,q,d,e,n,c,(long_to_bytes(res))))

#print("Value of P: %d") % (p)
#print("Value of Q: %d") % (q)
