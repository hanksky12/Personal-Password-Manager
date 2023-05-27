import json
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class Encrypt:
    def __init__(self, _password, _salt):
        password = bytes(_password, 'utf-8')
        salt = bytes(_salt, 'utf-8')
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=480000,
        )
        self._password = base64.urlsafe_b64encode(kdf.derive(password))
        self._cipher_suite = Fernet(self._password)

    def decrypt(self, _data):
        byte_string = self._cipher_suite.decrypt(_data)
        json_string = byte_string.decode('utf-8')
        return json.loads(json_string)

    def encrypt(self, _data):
        json_str = json.dumps(_data)
        byte_string = self._cipher_suite.encrypt(bytes(json_str, 'utf-8'))
        return byte_string
