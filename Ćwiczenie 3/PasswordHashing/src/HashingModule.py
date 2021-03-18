# -*- coding: utf-8 -*-

""" Moduł odpowiadający za hashowanie haseł """

import hashlib
import random

def hashPassword(password_plain, salt):
    
    """ Hashuje hasło z wykorzystaniem wygenerowanej soli """
    
    concatenationResult = salt + password_plain
    _hash = hashlib.sha256(concatenationResult.encode())
    
    return _hash.hexdigest()

def generateSalt(saltLength):
    
    """ Generuje sól """
    
    salt = ""
    
    for i in range(saltLength):
        randomASCIIindex = random.randint(33, 126)
        randomChar = chr(randomASCIIindex)
        salt += randomChar
        
    return salt