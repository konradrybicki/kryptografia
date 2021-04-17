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
            
        ] # TODO automatyzacja
        
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
    
    def encrypt(self, plainText: [str]) -> [str]: # TODO refaktoryzacja
        
        """ Szyfruje tekst jawny, z wykorzystaniem wygenerowanego klucza """
        
        cipherText = []
        
        for plainTextLine in plainText:
            
            cipherTextLine = ""
            
            for plainTextLetter in plainTextLine:
        
                cipherTextLetter = ''
                
                if plainTextLetter != '\n':
                    matchingSubstitutions = self.key.get(plainTextLetter)
                    cipherTextLetter = matchingSubstitutions[random.randint(0, 1)]
                else:
                    cipherTextLetter = '\n'
                
                cipherTextLine += cipherTextLetter
                    
            cipherText.append(cipherTextLine)
        
        return cipherText
    
    def decrypt(self, cipherText: [str]) -> [str]: # TODO refaktoryzacja
        
        """ Odszyfrowuje kryptogram z użyciem klucza, wykorzystanego do jego zaszyfrowania """
        
        plainText = []
        
        for cipherTextLine in cipherText:
            
            plainTextLine = ""
            
            for cipherTextLetter in cipherTextLine:
        
                plainTextLetter = ''
                
                if cipherTextLetter != '\n':
                    # przeszukujemy słownik
                    for plainAlphabetLetter in self.key:
                        if cipherTextLetter in self.key[plainAlphabetLetter]:
                            plainTextLetter = plainAlphabetLetter
                            break
                else:
                    plainTextLetter = '\n'
                
                plainTextLine += plainTextLetter
                    
            plainText.append(plainTextLine)
        
        return plainText
    
    def transposeRows(self, cipherText : [str]) -> [str]:
        
        """ Zamienia miejscami wiersze kryptogramu, para po parze """
    
        pass
    
    def transposeCols(self, cipherText: [str]) -> [str]:
        
        """ Zamienia miejscami każdą parę liter w każdym wierszu kryptogramu """
        
        pass