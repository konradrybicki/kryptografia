# -*- coding: utf-8 -*-

from cryptography.fernet import Fernet

class Symetric:
    
    """ Klasa statyczna odpowiadająca za operacje kryptografii symetrycznej """
    
    @staticmethod
    def generateKey() -> bytes:
        
        """ Generuje pojedynczy klucz tajny """
        
        key = Fernet.generate_key()
        return key
    
    @staticmethod
    def encode(message: bytes, key: bytes) -> bytes:
        
        """ Szyfruje wiadomosc z wykorzystaniem wygenerowanego klucza """
        
        f = Fernet(key)
        token = f.encrypt(message)
        
        return token
    
    @staticmethod
    def decode(token: bytes, key: bytes) -> bytes:
        
        """ Deszyfruje wiadomosc z wykorzystaniem klucza, wykorzystanego do jej zaszyfrowania """
        
        f = Fernet(key)
        message = f.decrypt(token)
        
        return message



if __name__=="__main__":
    
    # 'test'
    
    message = b"message content"
    
    try:
        key = Symetric.generateKey()
        token = Symetric.encode(message, key)
        Symetric.decode(token, key)
    except:
        print("Test failed.")
    else:
        print("Test passed.")