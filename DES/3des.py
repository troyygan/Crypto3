from pyDes import *
#from time import time
from datetime import datetime, date, time

@profile
def tri_des():
     # example of DES encrypting in CBC mode with the IV of "\0\0\0\0\0\0\0\0"
    print ("Tiple DES Encryption using CBC Mode\n")
#    t = time()
    before_time_enc = datetime.now()
    #this is using 24 byte key for single DES
    print "\n"
    k = triple_des("abcdefghijklmnopqrstuvwx", CBC, "\0\0\0\0\0\0\0\0", padmode=PAD_PKCS5)
    with open ("testfile.txt", "rb") as file:
        data = file.read()
#    data = "DES encryption algorithm"
#    print ("Key      : %r" % k.getKey())
#    print ("Data     : %r" % data)
    print "----CIPHERKEY----"
    print k.getKey()
    print "\n"
    print "----PLAINTEXT----"
    print data

    d = k.encrypt(data)
    after_time_enc = datetime.now()
    total_time_enc = after_time_enc - before_time_enc
#    print ("Encrypted: %r" % d)
    print "----CIPHERTEXT----"
    print d

    before_time_dec = datetime.now()
    d = k.decrypt(d)
    after_time_dec = datetime.now()
    total_time_dec = after_time_dec - before_time_dec
    print"\n"
    print ("Decrypted:\n %r" % d)
    print "\n"
    print""
    print "----ENCRYPTION TIME----"
    print "Start Time: ", before_time_enc
    print "End Time: ", after_time_enc
    print "Total Time of Execution: ", total_time_enc
    print "\n"

    print "----DECRYPTION TIME----"
    print "Start Time: ", before_time_dec
    print "End Time: ", after_time_dec
    print "Total Time of Execution: ", total_time_dec
    print "\n"
#    print ("Decrypted: %r" % d)
#    print ("DES time taken: %f (6 crypt operations)" % (time() - t))
#    print ("")

tri_des()

