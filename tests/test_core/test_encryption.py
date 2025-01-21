import pytest
from dvpn.core.encryption import EncryptionService

def test_encryption_decryption():
    service = EncryptionService()
    message = b"Test message"
    encrypted = service.encrypt_message(message)
    decrypted = service.decrypt_message(encrypted)
    assert decrypted == message