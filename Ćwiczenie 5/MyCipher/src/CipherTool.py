# -*- coding: utf-8 -*-

class CipherTool:
    
    """ Klasa, odpowiadająca za operacje kryptograficzne """
    
    def __init__(self):
        
        """ Inicjuje obiekt, deklarując pole z kluczem """
        
        self.key: dict
        
    def generateKey(self):
        
        """ Generuje klucz, inicjalizując pole 'key' """
        
        pass
    
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