# -*- coding: utf-8 -*-

'''

Notki dla Tomka:

1) Wiem, że klasy statyczne są mało "Pythonowe", ale SQLManager od razu skojarzył
   mi się z "NetworkingManager'em" z projektu z ING i nie mogłem odpuscic :)

2) Komentarz odnosnie pól statycznych jest dla mnie
    
'''

import mysql.connector

class SQLManager:
    
    """ Klasa zarządzająca połączeniem z bazą danych """
    
    # pola statyczne - deklarowane wewnątrz klasy (niestatyczne wewnątrz metod)
    __connection_hostName = "localhost"
    __connection_userName = "root"
    __connection_password = ""
    __connection_database = "service"
    
    @staticmethod
    def insertUser(self, login, password_hash, password_salt):
        
        """ Zapisuje dane użytkownika przy rejestracji """
        
        connection = SQLManager.initializeConnection()
        
        cursor = connection.cursor()
        sql = "insert into users values(%s, %s, %s)"
        params = (login, password_hash, password_salt)
        cursor.execute(sql, params)
        
        if cursor == False:
            self.closeConnection(cursor, connection)
            return False
        else:
            self.closeConnection(cursor, connection)
            return True
        
    @staticmethod
    def selectPassword(self, login):
        
        """ Odczytuje hasz hasła oraz sól przy logowaniu """
        
        connection = SQLManager.initializeConnection()
        
        cursor = connection.cursor()
        sql = "select passwordHash, passwordSalt from users, where login like %s"
        params = (login)
        cursor.execute(sql, params)
        
        if cursor == False:
            self.closeConnection(cursor, connection)
            return False
        else:
            result  = cursor.fetchone()
            password_hash = result[0]
            password_salt = result[1]
            
            self.closeConnection(cursor, connection)
            
            return password_hash, password_salt
        
    @staticmethod
    def initializeConnection(self):
        
        """ Inicjuje połączenie z bazą, zarówno przy rejestracji jak i logowaniu """
        
        connection = mysql.connector.connect(
            host = self.__connection_hostName,    
            user = self.__connection_userName,
            password = self.__connection_password,
            database = self.__connection_database
        )
        
        # TODO - scenariusz negatywny
        if connection == False:
            print("Database connection error. Program will exit now")
            exit()
        else:
            return connection
    
    @staticmethod
    def closeConnection(cursor, connection):
        
        """ Zamyka połączenie z bazą """
        
        cursor.close()
        connection.close()
        
        return