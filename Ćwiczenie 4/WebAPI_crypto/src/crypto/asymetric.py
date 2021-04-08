# -*- coding: utf-8 -*-

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

class Asymetric:
    
    """ Klasa statyczna odpowiadająca za operacje kryptografii asymetrycznej """
    
    @staticmethod
    def generatePrivateKey():
        
        """ Generuje klucz prywatny """
        
        privateKey = rsa.generate_private_key(
            public_exponent = 65537,
            key_size = 4096
        )
        
        return privateKey
    
    @staticmethod 
    def createPublicKey(privateKey):
        
        """ Tworzy klucz publiczny, z wykorzystaniem wygenerowanego klucza prywatnego """
        
        publicKey = privateKey.public_key()
        return publicKey
    
    @staticmethod
    def serializeKey_private(privateKey) -> str:
        
        """ Serializuje klucz prywatny do postaci tekstowej w formacie OpenSSH, zwracanej jako hex """
        
        pem = privateKey.private_bytes(
            encoding = serialization.Encoding.PEM,
            format = serialization.PrivateFormat.TraditionalOpenSSL, # TODO OpenSSL -> OpenSSH
            encryption_algorithm = serialization.NoEncryption()
        )
        
        return pem.hex()
    
    @staticmethod
    def serializeKey_public(publicKey) -> str:
        
        """ Serializuje klucz publiczny do postaci tekstowej w formacie OpenSSH, zwracanej jako hex """
        
        pem = publicKey.public_bytes(
            encoding = serialization.Encoding.PEM,
            format = serialization.PublicFormat.SubjectPublicKeyInfo # TODO OpenSSH
        )
        
        return pem.hex()
        
    # TODO verify, sign, encode, decode
    
    

if __name__=="__main__":
    
    # 'test'
    
    try:
        privateKey = Asymetric.generatePrivateKey()
        publicKey = Asymetric.createPublicKey(privateKey)
        Asymetric.serializeKey_private(privateKey)
        Asymetric.serializeKey_public(publicKey)
    except:
        print("Test failed.")
    else:
        print("Test passed.")