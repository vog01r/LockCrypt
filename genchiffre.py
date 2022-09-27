from cryptography.fernet import Fernet

key = Fernet.generate_key() 
  
with open('filekey.key', 'wb') as filekey: 
   filekey.write(key)
