# -*- coding: utf-8 -*-

import hashlib
import json
from time import time

import random

class Blockchain(object): 
     
    """ Klasa definiująca strukturę oraz zachowania sieci blockchain, przechowującej informacje o transakcjach 'własnego budżetu' """
    
    def __init__(self):
        
        """ Inicjuje pola dla łańcucha bloków oraz transakcji, oczekujących na dodanie do sieci """
        
        self.__chain = []
        self.__pendingTransactions = []
        
    def addTransaction(self, sender, recipient, amount, title):
        
        """ Dodaje nową transakcję do listy transakcji oczekujących """
        
        newTransaction = { 
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
            'title': title
        }
        
        self.__pendingTransactions.append(newTransaction)
        
        if len(self.__pendingTransactions) == 3:
            self.__addBlock()
    
    def __addBlock(self):
        
        """ Dodaje do sieci nowy blok, przechowujący informacje o dokładnie trzech transakcjach """
        
        previousBlockHash = ""
        
        if len(self.__chain) == 0:
            previousBlockHash = "-"
        else:
            previousBlockHash = self.__hashLastBlock()
        
        newBlock = {
            "block index": len(self.__chain) + 1,
            "timestamp": time(),
            "stored transactions": self.__pendingTransactions,
            "proof of work": random.randint(10000, 99999),
            "previous block hash": previousBlockHash
        }
        
        self.__chain.append(newBlock)
        self.__pendingTransactions = []
        
    def __hashLastBlock(self):
        
        """ Hashuje ostatni blok w sieci """
        
        lastBlock = self.__chain[-1]
        lastBlock_stringFormat = json.dumps(lastBlock, sort_keys=True)
        
        lastBlock_hashed = hashlib.sha256(lastBlock_stringFormat.encode())
        lastBlock_hashed_hex = lastBlock_hashed.hexdigest()
    
        return lastBlock_hashed_hex
    
    def displayChain(self):
        
        """ Wyswietla łańcuch w konsoli """
        
        if len(self.__chain) == 0:
            print("Chain empty.")
        else:
            for block in self.__chain:
                print(json.dumps(block, indent=4, separators=(',', ': ')))
    
    def saveData(self):
        
        """ Zapisuje sieć oraz transakcje 'oczekujące' do plików z danymi """
        
        # 'wrap'
        
        chain_dictFormat = {}
        chain_dictFormat['data'] = self.__chain
        
        transactions_dictFormat = {}
        transactions_dictFormat['data'] = self.__pendingTransactions
        
        # zapis
        
        blockchainFile = open('Blockchain.txt', 'w')
        transactionsFile = open('PendingTransactions.txt', 'w')
        
        json.dump(chain_dictFormat, blockchainFile)
        json.dump(transactions_dictFormat, transactionsFile)
        
        blockchainFile.close()
        transactionsFile.close()
    
    def loadData(self):
        
        """ Odczytuje sieć oraz transakcje 'oczekujące' z plików z danymi """
        
        # odczyt
        
        blockchainFile = open('Blockchain.txt')
        transactionsFile = open('PendingTransactions.txt')
        
        chain_dictFormat = json.load(blockchainFile)
        transactions_dictFormat = json.load(transactionsFile)
        
        # 'unwrap'
        
        self.__chain = chain_dictFormat['data']
        self.__pendingTransactions = transactions_dictFormat['data']
        
        blockchainFile.close()
        transactionsFile.close()