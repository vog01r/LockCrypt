import os
from cryptography.fernet import Fernet

with open('filekey.key', 'rb') as filekey: 
    key = filekey.read()

fernet = Fernet(key) 

for path, subdirs, files in os.walk('./test'):
    for name in files:
        print(os.path.join(path, name))
        filepath = os.path.join(path, name)
        with open(filepath, 'rb') as enc_file: 
            encrypted = enc_file.read() 
      
        decrypted = fernet.decrypt(encrypted) 
  
        with open(filepath, 'wb') as dec_file:
            dec_file.write(decrypted)
        filepath2=filepath.replace('.zooky','')
        os.rename(filepath, filepath2)
    

