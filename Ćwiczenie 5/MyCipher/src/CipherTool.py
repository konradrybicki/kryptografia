# -*- coding: utf-8 -*-

import random

class CipherTool:
    
    """ Klasa, odpowiadająca za operacje kryptograficzne """
    
    def __init__(self):
        
        """ Inicjuje obiekt, deklarując pole z kluczem """
        
        self.key: dict
        
    def generateKey(self):
        
        """ Generuje klucz, inicjalizując pole 'key' """
        
        cryptogramAlphabet = [
            
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
            "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
            "u", "v", "w", "x", "y", "z",
                              
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
            "K", "K", "M", "N", "O", "P", "Q", "R", "S", "T",
            "U", "V", "W", "X", "Y", "Z",
                              
            "0", "1"
            
        ]
        
        cipherKey = {}
        
        for i in range(27):
            
            cipherKey_letter = ""
            cipherKey_substitutions = []
            
            if i < 26:
                cipherKey_letter = chr(97+i) # małe litery alfabetu angielskiego (ASCII)
            else:
                cipherKey_letter = " "
            
            for j in range(2):
                substitution = random.choice(cryptogramAlphabet)
                cipherKey_substitutions.append(substitution)
                cryptogramAlphabet.remove(substitution)
                
            cipherKey.update({cipherKey_letter: cipherKey_substitutions})
            
        self.key = cipherKey
    
    def encrypt(self, plainText: [str]) -> [str]:
        
        """ Szyfruje tekst jawny, z wykorzystaniem wygenerowanego klucza """
        
        pass
    
    def decrypt(self, cipherText: [str]) -> [str]:
        
        """ Odszyfrowuje kryptogram z użyciem klucza, wykorzystanego do jego zaszyfrowania """
        
        pass
    
    def transposeRows(self, cipherText : [str]) -> [str]:
        
        """ Zamienia miejscami wiersze kryptogramu, para po parze """
    
        pass
    
    def transposeCols(self, cipherText: [str]) -> [str]:
        
        """ Zamienia miejscami każdą parę liter w każdym wierszu kryptogramu """
        
        pass