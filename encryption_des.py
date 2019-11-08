import commands 
import os
from datetime import datetime, date, time
from pyDes import *
#from utils import profile


@profile

def enc_des():
#  os.system("clear")  
  print "DES Encrytion Started ..."
  before_time = datetime.now()
  #print "Time before AES Encryption Starts :", before_time
  with open ('testfile.txt', 'rb') as file:
      data = file.read()
  k = des("DESCRYPT", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
  e = k.encrypt(data)
  print "Encrypted data is: ", e
  #print "Time after AES Encryption completes :", after_time
  after_time = datetime.now()
  total_time = after_time - before_time
  print "Total Time conceeded by DES for Encryption ", total_time
  print "Decryption Started..."
  before_time = datetime.now()
  d = k.decrypt(data)
  after_time = datetime.now()
  total_time = after_time - before_time
  print "Decrypted result: ", d
  print "Total Time conceeded by DES for Decryption ", total_time



enc_des()
