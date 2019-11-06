import commands 
import os
from datetime import datetime, date, time
from pyDes import *
#from utils import profile


@profile

def aes():
#  os.system("clear")  
  print "AES Encrytion Started ..."
  before_time = datetime.now()
  #print "Time before AES Encryption Starts :", before_time
  os.system("python aes.py -d testfile_encrypted_AES.txt -o dec_result_aes.txt")
  after_time = datetime.now()
  #print "Time after AES Encryption completes :", after_time
  total_time = after_time - before_time
  print "Total Time conceeded by AES ", total_time


aes()
