from aes import *
import commands
import os
from datetime import datetime, date, time

@profile


def enc():
    print "AES Encrypt started....."
    before_time_enc = datetime.now()
    print "Start Time of Encryption: ", before_time_enc
    moo = AESModeOfOperation()
    with open ("testfile.txt", "rb") as file:
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
    print "Start Time of Decryption: ", before_time_dec
    decr = moo.decrypt(ciph, orig_len, mode, cypherkey,
            moo.aes.keySize["SIZE_128"], iv)
    after_time_dec = datetime.now()
    print "End Time of Decryption: ", after_time_dec
    total_time_dec = after_time_dec - before_time_dec
    print "Total Time of Decryption: ", total_time_dec
    print decr


enc()
