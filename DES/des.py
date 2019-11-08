import commands
import os
from datetime import datetime, date, time
from pyDes import *

@profile

def des_enc():
    print "Encryption Starte..."
    before_time = datetime.now()
    with open ('testfile.txt', 'rb') as file:
        data = file.read()

    k = triple_des("TROYTROYTROYTROYTROYTROY", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    d = k.encrypt(data)

    print "Encrypted: %r" % d
    print "Decrypted: %r" % k.decrypt(d)

    assert k.decrypt(d, padmode=PAD_PKCS5) == data
    after_time = datetime.now()
    total_time = after_time - before_time
    print "Total Time conceeded by DES", total_time


des_enc()


