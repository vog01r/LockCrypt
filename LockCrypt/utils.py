import os

class KeyLoader:
    def __init__(self, file_path='filekey.key'):
        self.file_path = file_path

    def load_key(self):
        if not self._key_exists():
            raise FileNotFoundError(f"No key file found at {self.file_path}. Please ensure the key is generated.")
        with open(self.file_path, 'rb') as filekey:
            key = filekey.read()
            print(f"Key loaded from {self.file_path}")
            return key

    def _key_exists(self):
        exists = os.path.exists(self.file_path)
        if not exists:
            print(f"Key file does not exist at {self.file_path}")
        return exists

def main():
    key_loader = KeyLoader()
    try:
        key = key_loader.load_key()
        print(f"Successfully loaded key: {key}")
    except FileNotFoundError as e:
        print(e)

if __name__ == "__main__":
    main() 