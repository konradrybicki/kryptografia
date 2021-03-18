# -*- coding: utf-8 -*-

from src import HashingModule
from src.SQLManager import SQLManager

class User:
    
    """ Klasa definiująca strukturę oraz zachowania użytkownika """
    
    def __init__(self, login, password):
        self.login = login
        self.password = password
        
    def register(self):
        
        """ Wykorzystując moduł hashujący oraz klasę SQLManager zapisuje login, hash hasła oraz sól do bazy """
        
        password_salt = HashingModule.generateSalt(64) # 64 - długosc hasha wyjsciowego (minimalna rekomendowana dlugosc soli)
        password_hash = HashingModule.hashPassword(self.password, password_salt)
        
        registered = SQLManager.insertUser(self.login, password_hash, password_salt)
        
        if registered == False:
            print("Something went wrong. You might try to register again")
            exit()
        else:
            print("Registration succesful! You can log in now")
            exit()
            
    def logIn(self):
            
        """ Odczytuje hash hasła oraz sól dla danego login'u, celem przeprowadzenia weryfikacji hasła """
        
        loggedIn = SQLManager.selectPassword(self.login)
        
        if len(loggedIn) == 1: # błąd
            print("Something went wrong. You might try to log in again")
            exit()
        else:
            originalPassword_hash = loggedIn[0]
            originalPassword_salt = loggedIn[1]
            
            password_hash  = HashingModule.hashPassword(self.password, originalPassword_salt)
            
            if password_hash == originalPassword_hash:
                print("Login succesful!")
                exit()
            else:
                print("Incorrect password. Try again")
                exit()