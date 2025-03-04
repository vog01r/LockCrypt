from cryptography.fernet import Fernet
import os

class KeyManager:
    def __init__(self, file_path='filekey.key'):
        self.file_path = file_path

    def generate_key(self):
        key = Fernet.generate_key()
        self._save_key(key)
        print(f"Key generated and saved to {self.file_path}")

    def _save_key(self, key):
        with open(self.file_path, 'wb') as filekey:
            filekey.write(key)

    def key_exists(self):
        return os.path.exists(self.file_path)

    def load_key(self):
        if not self.key_exists():
            raise FileNotFoundError(f"No key file found at {self.file_path}. Please generate a key first.")
        with open(self.file_path, 'rb') as filekey:
            return filekey.read()

def main():
    key_manager = KeyManager()
    if not key_manager.key_exists():
        key_manager.generate_key()
    else:
        print("Key already exists. Loading existing key.")
        key = key_manager.load_key()
        print(f"Loaded key: {key}")

if __name__ == "__main__":
    main() 