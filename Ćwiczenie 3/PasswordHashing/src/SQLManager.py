# -*- coding: utf-8 -*-

import mysql.connector

class SQLManager:
    
    """ Klasa statyczna zarzadzająca połączeniem z bazą danych """
    
    # notka dla mnie - pola statyczne, deklarowane wewnątrz klasy (niestatyczne wewnątrz metod)
    __connection_host = "localhost"
    __connection_user = "root"
    __connection_password = ""
    __connection_database = "service"
    
    @staticmethod
    def insertUser(self, login, password_hash, password_salt):
        
        """ Zapisuje dane użytkownika przy rejestracji """
        
        connection = mysql.connector.connect(
            host = self.__connection_host,    
            user = self.__connection_user,
            password = self.__connection_password,
            database = self.__connection_database
        )
        
        if connection == False:
            connection.close()
            return False
        
        cursor = connection.cursor()
        sql = "insert into users values(%s, %s, %s)"
        params = (login, password_hash, password_salt)
        cursor.execute(sql, params)
        
        if cursor == False:
            cursor.close()
            connection.close()
            return False
        else:
            cursor.close()
            connection.close()
            return True
        
    @staticmethod
    def selectPassword(self, login):
        
        """ Odczytuje hasz hasła oraz sól przy logowaniu """
        
        connection = mysql.connector.connect(
            host = self.__connection_host,    
            user = self.__connection_user,
            password = self.__connection_password,
            database = self.__connection_database
        )
        
        if connection == False:
            connection.close()
            return False
        
        cursor = connection.cursor()
        sql = "select passwordHash, passwordSalt from users, where login like %s"
        params = (login)
        cursor.execute(sql, params)
        
        if cursor == False:
            cursor.close()
            connection.close()
            return False
        else:
            result  = cursor.fetchone()
            password_hash = result[0]
            password_salt = result[1]
            
            cursor.close()
            connection.close()
            
            return password_hash, password_salt
        
'''

Notka dla Tomka:
    
Wiem, że klasy statyczne są mało "Pythonowe", ale SQLManager od razu skojarzył
mi się z "NetworkingManager'em" z projektu z ING i nie mogłem odpuscic :)

'''