from cryptography.fernet import Fernet

class EncryptDecrypt:
    def __init__(self):
        self.cipher_suite = Fernet(Fernet.generate_key())

    def encrypt(self, text):
        return self.cipher_suite.encrypt(text.encode())

    def decrypt(self, encrypted_text):
        return self.cipher_suite.decrypt(encrypted_text).decode()
