# -*- coding: utf-8 -*-

""" Moduł główny wykorzystujący klasy FileManager oraz CipherTool do szyfrowania oraz odszyfrowywania danych wejsciowych """

from src.FileManager import FileManager
from src.CipherTool import CipherTool

# encrypt

plainText = FileManager.readFile("plaintext.txt")
    
cipherTool = CipherTool()
cipherTool.generateKey()
cipherText = cipherTool.encrypt(plainText)
    
FileManager.saveFile(cipherText, "ciphertext.txt")

# decrypt

cipherText = FileManager.readFile("ciphertext.txt")
cipherText_decrypted = cipherTool.decrypt(cipherText)
FileManager.saveFile(cipherText_decrypted, "ciphertext_decrypted.txt")