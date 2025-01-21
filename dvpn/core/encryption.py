# dvpn/core/encryption.py
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.fernet import Fernet

class EncryptionService:
    def __init__(self):
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self.public_key = self.private_key.public_key()
        self.session_key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.session_key)
        
    def encrypt_message(self, message: bytes) -> bytes:
        return self.cipher_suite.encrypt(message)
    
    def decrypt_message(self, encrypted_message: bytes) -> bytes:
        return self.cipher_suite.decrypt(encrypted_message)
    
    def get_public_key(self):
        return self.public_key