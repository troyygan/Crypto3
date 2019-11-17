import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

def passphrase(password_provided): #  Takes in password from user
	password = password_provided.encode() # Convert to type bytes
	salt = b'salt_' # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
	kdf = PBKDF2HMAC(
	    algorithm=hashes.SHA256(),
	    length=32,
	    salt=salt,
	    iterations=100000,
	    backend=default_backend()
	)
	key = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once
	return key

def encrypt(key, input_file): # Takes in password and file name from user
	output_file = 'encrypted_' + input_file # Adds 'encrypted_' before name of file upon completion
	

	with open(input_file, 'rb') as f: # Opens file to be read
	    data = f.read() #  Assigns file to veriable 'data'

	fernet = Fernet(key) # Applies key
	encrypted = fernet.encrypt(data) # Encrypts data with key

	with open(output_file, 'wb') as f: # Creates file
	    f.write(encrypted) # Writes encryted data to file


def decrypt(key, input_file): # Takes in password and file name from user
	output_file = 'decrypted_' + input_file # Adds 'decrypted_' before name of file upon completion

	with open(input_file, 'rb') as f: # Opens file to be read
	    data = f.read() #  Assigns file to veriable 'data'

	fernet = Fernet(key) # Applies key
	encrypted = fernet.decrypt(data) # Decrypts data with key

	with open(output_file, 'wb') as f: # Creates file
	    f.write(encrypted) # Writes decryted data to file

def binary_encode(input_file): # Takes file name from user
        output_file = 'binary_' + input_file # Adds 'binary_' before name of file upon completion

        with open(input_file, 'r') as f: # Opens file to be read
                data = f.read() #  Assigns file to veriable 'data'
        binary = ''.join([bin(ord(c))[2:].rjust(8,'0') for c in data]) # converts 'data' to binary

        with open(output_file, 'w') as f: # Creates file
                f.write(binary) # Writes binary data to file

def binary_decode(input_file): # Takes file name from user
        output_file = 'debinary_' + input_file # Adds 'binary_' before name of file upon completion

        with open(input_file, 'r') as f: # Opens file to be read
                data = f.read() #  Assigns file to veriable 'data'
        n = int(data, 2) # Converts String 'data' to an integer variable and assigns it to 'n'
        debinary = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode() # Converts 'n' to a text String
        
        with open(output_file, 'w') as f: # Creates file
                f.write(debinary) # Writes debinary data to file


option = input("\n'1' Encrypt a file \n'2' Decrypt a file\n'3' Convert to binary\n'4' Convert from binary\n>> ") # Displays option and promps user for input

if option == '1':
	password = input("Enter password >> ") 
	name = input("\nEnter file name in current directory >> ")
	encrypt(passphrase(password), name)

elif option == '2':
	password = input("Enter password >> ")
	name = input("\nEnter file name in current directory >> ")
	decrypt(passphrase(password), name)
	
elif option == '3':
	name = input("\nEnter file name in current directory >> ")
	binary_encode(name)

elif option == '4':
	name = input("\nEnter file name in current directory >> ")
	binary_decode(name)
else: # If invalid entry program will exit
	print("Sorry...")
