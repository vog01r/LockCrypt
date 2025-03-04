import os
from cryptography.fernet import Fernet

class StandaloneDecryptor:
    def __init__(self, key):
        self.fernet = Fernet(key)

    def decrypt_file(self, filepath):
        if not filepath.endswith('.zooky'):
            print(f"File {filepath} is not encrypted with .zooky extension.")
            return

        with open(filepath, 'rb') as enc_file:
            encrypted = enc_file.read(2048)
            rest_of_file = enc_file.read()
        decrypted = self.fernet.decrypt(encrypted)
        with open(filepath.replace('.zooky', ''), 'wb') as dec_file:
            dec_file.write(decrypted + rest_of_file)
        os.remove(filepath)
        print(f"Decrypted {filepath}")

def main():
    key = load_key()
    decryptor = StandaloneDecryptor(key)
    document_path = './standard_alone/document.zooky'  # Change this path as needed
    decryptor.decrypt_file(document_path)

def load_key(file_path='filekey.key'):
    with open(file_path, 'rb') as filekey:
        return filekey.read()

if __name__ == "__main__":
    main() 