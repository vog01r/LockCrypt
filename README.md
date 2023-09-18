# crypt_rew

Information retrieval project at crypt_rew
I copied the framework of the readme from https://github.com/stasbel/articlix


## Installation
```
git https://github.com/vogeaux/crypt_rew.git
cd ./crypt_rew
pip install -r ./requirements.txt
```

## Usage

after generating your key with the **genchiffre.py** file
you have a file that has an encryption key filekey.key.

now you can encrypt your documents with **chriffrement_all.py**
and you can decrypt your documents with **dechiffrement_all.py**

to change the destination of the folder to be encrypted, it's directly in the code.

```
for path, subdirs, files in os.walk('./test'):
    for name in files:
```

change file extension after encryption

```
with open(filepath+'.zooky', 'wb') as encrypted_file: 
             encrypted_file.write(encrypted)
```

### explanation of its use

tool for performing encryption tests.


### Data

Data test is folder **./test**

### key

you must generate your encryption key with **genchiffre.py**

[MIT](LICENSE)