#from aes import *
import commands
import os
from datetime import datetime, date, time

@profile


def ava():
    print "Avalanche Result....."
    before_time = datetime.now()
    os.system("java DESTest")
    after_time = datetime.now()
    print "End Time of Encryption: ", after_time
    total_time = after_time - before_time
    print "Total of Avalanche Testing: ", total_time
   


ava()

