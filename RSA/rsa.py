from rsa_ob import *
import commands
import os
from datetime import datetime, date, time


@profile

def func_rsa():
  print "RSA Encryption-Decryption Started....."
  before_time_enc = datetime.now()
  r = RSA()
  encrypt = r.encrypt
  decrypt = r.decrypt
  print "RSA Encrypter/ Decrypter"


##If you want to make the script interactive you can uncomment the lines below
#  p = int(raw_input("Enter a prime number (17, 19, 23, etc): "))
#  q = int(raw_input("Enter another prime number (Not one you entered above): "))
  p = 89
  q = 97
  print "Using %s and %s for generating keys" % (p, q)
  print "Generating your public/private keypairs now . . ."
  public, private = r.generate_keypair(p, q)
  print "Your public key is ", public ," and your private key is ", private
#  message = raw_input("Enter a message to encrypt with your private key: ")
  with open ("testfile.txt", "rb") as file:
      message = file.read()
  encrypted_msg = encrypt(private, message)
  print "Encrypted message is: "
  print ''.join(map(lambda x: str(x), encrypted_msg))
  after_time_enc = datetime.now()
  total_time_enc = after_time_enc - before_time_enc


###DECRYPTIOn

  print "Decryption Started..."
  before_time_dec = datetime.now()
  print "Decrypting message with public key ", public ," . . ."
  print "Decrypted Message:"
  print decrypt(public, encrypted_msg)
  after_time_dec = datetime.now()
  total_time_dec = after_time_dec - before_time_dec

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



func_rsa()

