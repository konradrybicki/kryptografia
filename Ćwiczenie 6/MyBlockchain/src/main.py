# -*- coding: utf-8 -*-

""" Moduł główny, odpowiadający za interakcję z użytkownikiem """

from src.Blockchain import Blockchain

blockchain = Blockchain()
blockchain.loadData()

while(True):
    
    print()
    print("MyBlockchain 2021")
    print("-----------------")
    print("1. Show blockchain")
    print("2. Add new transaction")
    print("3. Exit")
    
    usersChoice = ""
    
    while(True):
        usersChoice = input()
        if (usersChoice == "1") or (usersChoice == "2") or (usersChoice == "3"):
            break
        else:
            print("Incorrect value, try again")
    
    if usersChoice == "1":
        
        blockchain.displayChain()
        
    elif usersChoice == "2":
        
        sender = input("Sender: ")
        recipient = input("Recipient: ")
        amount = input("Amount: ")
        title = input("Title: ")
        
        blockchain.addTransaction(sender, recipient, amount, title)
        blockchain.saveData()
        
        print("New transaction added sucessfully!")
    
    else:
        break