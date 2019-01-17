import sys

import cryptography

from cryptography.fernet import Fernet,MultiFernet

string="String to be Encrypted"

# Fernet Cryptography

print("Fernet Cryptography")

key=Fernet.generate_key()

key_object=Fernet(key)

print("Original String: %s" %string)

encrypted_string=key_object.encrypt(string)

print("Encrypted String: %s" %encrypted_string)	

timestamp=key_object.extract_timestamp(encrypted_string)

print("Timestamp of the encrypted string: %s" %timestamp)

decrypted_string=key_object.decrypt(encrypted_string)

print("Decrypted String: %s" %decrypted_string)


# Multi-Fernet Cryptography

print("Multi-Fernet Cryptography")

first_key=Fernet(Fernet.generate_key())

second_key=Fernet(Fernet.generate_key())

key_object=MultiFernet([first_key,second_key])

print("Original String: %s" %string)

encrypted_string=key_object.encrypt(string)

print("Encrypted String: %s" %encrypted_string)	

timestamp=key_object.extract_timestamp(encrypted_string)

print("Timestamp of the encrypted string: %s" %timestamp)

decrypted_string=key_object.decrypt(encrypted_string)

print("Decrypted String: %s" %decrypted_string)

# Rotation

third_key=Fernet(Fernet.generate_key())

key_object_2=MultiFernet([third_key,first_key,second_key])

rotated=key_object_2.rotate(encrypted_string)

decrypted_string=key_object_2.decrypt(rotated)

print("Decrypted String: %s" %decrypted_string)


# Fernet Encryption using Passwords

import base64

import os

from cryptography.hazmat.backends import default_backend

from cryptography.hazmat.primitives import hashes

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password="Enter your password"

salt=os.urandom(16)

kdf=PBKDF2HMAC(algorithm=hashes.SHA256(),length=32,salt=salt,iterations=100000,backend=default_backend())

key=base64.urlsafe_b64encode(kdf.derive(password))

key_object=Fernet(key)

print("Original String: %s" %string)

encrypted_string=key_object.encrypt(string)

print("Encrypted String: %s" %encrypted_string)	

timestamp=key_object.extract_timestamp(encrypted_string)

print("Timestamp of the encrypted string: %s" %timestamp)

decrypted_string=key_object.decrypt(encrypted_string)

print("Decrypted String: %s" %decrypted_string)




