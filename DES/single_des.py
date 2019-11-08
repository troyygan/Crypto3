from pyDes import *
from time import time

@profile
def _example_des_():
     # example of DES encrypting in CBC mode with the IV of "\0\0\0\0\0\0\0\0"
    print ("Example of DES encryption using CBC mode\n")
    t = time()
    #this is using 8 byte key for single DES
    k = des("abcdefgh", CBC, "\0\0\0\0\0\0\0\0", padmode=PAD_PKCS5)
    with open ("testfile.txt", "rb") as file:
        data = file.read()
#    data = "DES encryption algorithm"
    print ("Key      : %r" % k.getKey())
    print ("Data     : %r" % data)

    d = k.encrypt(data)
    print ("Encrypted: %r" % d)

    d = k.decrypt(d)
    print ("Decrypted: %r" % d)
    print ("DES time taken: %f (6 crypt operations)" % (time() - t))
    print ("")

_example_des_()

