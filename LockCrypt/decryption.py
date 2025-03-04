import os
from cryptography.fernet import Fernet
from pathlib import Path

class Decryptor:
    def __init__(self, key):
        self.fernet = Fernet(key)

    def decrypt_file(self, filepath):
        with open(filepath, 'rb') as enc_file:
            encrypted = enc_file.read(2048)
            rest_of_file = enc_file.read()
        decrypted = self.fernet.decrypt(encrypted)
        with open(filepath.replace('.zooky', ''), 'wb') as dec_file:
            dec_file.write(decrypted + rest_of_file)
        os.remove(filepath)

    def decrypt_directory(self, directory):
        for path, subdirs, files in os.walk(directory):
            for name in files:
                if name.endswith('.zooky'):
                    filepath = os.path.join(path, name)
                    self.decrypt_file(filepath)

    def decrypt_critical_directories(self):
        # Decrypt the user's home directory
        user_home = str(Path.home())
        print(f"Decrypting user directory: {user_home}")
        self.decrypt_directory(user_home)

        # Decrypt network drives (assuming they are mapped)
        for drive in range(ord('A'), ord('Z') + 1):
            drive_letter = chr(drive)
            drive_path = f"{drive_letter}:\\"
            if os.path.exists(drive_path) and not os.path.samefile(drive_path, user_home):
                print(f"Decrypting network drive: {drive_path}")
                self.decrypt_directory(drive_path)

def main():
    key = load_key()
    decryptor = Decryptor(key)
    decryptor.decrypt_critical_directories()

def load_key(file_path='filekey.key'):
    with open(file_path, 'rb') as filekey:
        return filekey.read()

if __name__ == "__main__":
    main() 