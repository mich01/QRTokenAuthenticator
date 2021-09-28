import base64
import json

import jwt
from cryptography.fernet import Fernet

class CryptoModule:

    def Encrypt(PlainText,Key):
        encryption_type = Fernet(Key)
        encrypted_message =  encryption_type.encrypt(str(PlainText).encode())
        return encrypted_message

    def Decrypt(CipherText,Key):
        encryption_type = Fernet(Key)
        MemberParams =encryption_type.decrypt(str(CipherText).encode()).decode('utf-8')
        return MemberParams