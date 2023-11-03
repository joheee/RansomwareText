from cryptography.fernet import Fernet
from controller.controller_text import ControllerText

class EncryptDecrypt:
    def __init__(self):
        key = Fernet.generate_key()
        self.cipher_suite = Fernet(key)
        handle_text = ControllerText('key.txt')
        handle_text.writeKey(key)

    def encrypt(self, text):
        return self.cipher_suite.encrypt(text.encode())

    def decrypt(self, key, encrypted_text):
        cipher_suite = Fernet(key)
        return cipher_suite.decrypt(encrypted_text).decode()
