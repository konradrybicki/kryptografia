# -*- coding: utf-8 -*-

import hashlib
import json
from time import time

class Blockchain(object):
    
    """ Klasa definiująca strukturę oraz zachowania sieci blockchain przechowującej informacje o transakcjach własnego budżetu """
    
    def __init__(self):
        
        """ Inicjuje pola dla łańcucha bloków oraz transakcji, oczekujących na dodanie do sieci """
        
        self.__chain = []
        self.__pendingTransactions = []
        
    def addTransaction(self, sender, recipient, amount):
        
        """ Dodaje nową transakcję do listy transakcji oczekujących """
        
        pass
    
    def addBlock(self):
        
        """ Dodaje do sieci nowy blok, przechowujący informacje o dokładnie trzech transakcjach """
        
        pass
        
    def hashLastBlock(self):
        
        """ Hashuje ostatni blok w sieci """
    
        pass