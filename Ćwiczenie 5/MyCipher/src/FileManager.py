# -*- coding: utf-8 -*-

class FileManager:
    
    """ Klasa statyczna, odpowiedzialna za operacje na plikach (odczyt, zapis) """
    
    @staticmethod
    def readFile(filePath: str) -> [str]:
        
        """ Odczytuje zawartosc pliku tekstowego, zwracając listę wierszy """
        
        try:
            f = open(filePath, "r")
            fileContent = f.readlines()
            f.close()
        except:
            print("Something went wrong while attempting to read to a file. Try again")
            exit()
        
        return fileContent
        
    @staticmethod
    def saveFile(dataToPrepare: [str], filePath: str):
        
        """ Przygotowuje (konkatenacja) oraz zapisuje dane wyjsciowe do pliku tekstowego """
        
        preparedData = ""
        
        for row in dataToPrepare:
            preparedData += row
        
        try:
            f = open(filePath, "w")
            f.write(preparedData)
            f.close
        except:
            print("Something went wrong while attempting to save to a file. Try again")
            exit()
        
        return