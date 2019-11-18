from aes import *
import commands
import os
from datetime import datetime, date, time

@profile


def enc():
    print "AES Encrypt started....."
    before_time_enc = datetime.now()
    moo = AESModeOfOperation()
    with open ("128bit_plaintext.txt", "rb") as file:
        cleartext = file.read()
    cypherkey = [143,194,34,208,145,203,230,143,177,246,97,206,145,92,255,84]
    iv = [103,35,148,239,76,213,47,118,255,222,123,176,106,134,98,92]
    mode, orig_len, ciph = moo.encrypt(cleartext, moo.modeOfOperation["CBC"],
            cypherkey, moo.aes.keySize["SIZE_128"], iv)
    print 'm=%s, ol=%s (%s), ciph=%s' % (mode, orig_len, len(cleartext), ciph)
    after_time_enc = datetime.now()
    print "End Time of Encryption: ", after_time_enc
    total_time_enc = after_time_enc - before_time_enc
    print "Total Time of Encryption: ", total_time_enc
   
    print "Decryption Started..."
    before_time_dec = datetime.now()
    decr = moo.decrypt(ciph, orig_len, mode, cypherkey,
            moo.aes.keySize["SIZE_128"], iv)
    after_time_dec = datetime.now()
    total_time_dec = after_time_dec - before_time_dec
   
    print "\n" 
    print "----DECRYPTED CIPHERTEXT----\n", decr

#Timestamps for encryption and decryption
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

    print "----INPUTS----"
    print "Cipherkey: ", cypherkey
    print "IV: ", iv
    

#


enc()
