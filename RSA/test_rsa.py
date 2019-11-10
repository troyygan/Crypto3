from rsa_ob import *

@profile

def func_rsa():
  r = RSA()
  encrypt = r.encrypt
  decrypt = r.decrypt
  print "RSA Encrypter/ Decrypter"
  p = int(raw_input("Enter a prime number (17, 19, 23, etc): "))
  q = int(raw_input("Enter another prime number (Not one you entered above): "))
  print "Generating your public/private keypairs now . . ."
  public, private = r.generate_keypair(p, q)
  print "Your public key is ", public ," and your private key is ", private
  message = raw_input("Enter a message to encrypt with your private key: ")
  encrypted_msg = encrypt(private, message)
  print "Your encrypted message is: "
  print ''.join(map(lambda x: str(x), encrypted_msg))
  print "Decrypting message with public key ", public ," . . ."
  print "Your message is:"
  print decrypt(public, encrypted_msg)


func_rsa()

