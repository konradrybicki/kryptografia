# -*- coding: utf-8 -*-

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

class Asymetric:
    
    """ Klasa statyczna odpowiadająca za operacje kryptografii asymetrycznej """
    
    @staticmethod
    def generatePrivateKey(): # -> _RSAPrivateKey
        
        """ Generuje klucz prywatny """
        
        privateKey = rsa.generate_private_key(
            public_exponent = 65537,
            key_size = 4096
        )
        
        return privateKey
    
    @staticmethod 
    def createPublicKey(privateKey): # -> _RSAPublicKey
        
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
        
    @staticmethod
    def signMessage(message: bytes, privateKey) -> bytes:
        
        """ Podpisuje wiadomosc z wykorzystaniem aktualnie ustawionego klucza prywatnego """
        
        signature = privateKey.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
                ),
            hashes.SHA256()
        )
        
        return signature
    
    @staticmethod
    def verifyMessage(publicKey, signature: bytes, message: bytes) -> None:
        
        """ Weryfikuje wiadomosc z wykorzystaniem klucza publicznego """
        
        try:
            publicKey.verify(
                signature,
                message,
                padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
        except:
            return "Message verification failed"
        else:
            return "Message verified"
            
    @staticmethod
    def encode(message: bytes, publicKey) -> bytes:
        
        """ Szyfruje wiadomosc z wykorzystaniem klucza publicznego """
        
        sipher = publicKey.encrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        
        return sipher
    
    @staticmethod
    def decode(sipher: bytes, privateKey) -> bytes:
        
        """ Deszyfruje wiadomosc z wykorzystaniem klucza prywatnego """
        
        message = privateKey.decrypt(
            sipher,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        
        return message

    

if __name__=="__main__":
    
    # 'test' - generowanie kluczy
    
    privateKey = Asymetric.generatePrivateKey()
    publicKey = Asymetric.createPublicKey(privateKey)
    
    # 'test' - serializacja
    
    serializedKey_private = Asymetric.serializeKey_private(privateKey)
    serializedKey_public = Asymetric.serializeKey_public(publicKey)
    
    # 'test' - podpisanie wiadomosci, weryfikacja
    
    message = b"message content"
    signature = Asymetric.signMessage(message, privateKey)
    print(Asymetric.verifyMessage(publicKey, signature, message))
    
    # 'test' - encode/decode
    
    sipher = Asymetric.encode(message, publicKey)
    message = Asymetric.decode(sipher, privateKey)