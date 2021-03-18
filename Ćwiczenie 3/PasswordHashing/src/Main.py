# -*- coding: utf-8 -*-

""" Moduł główny, podzielony na sekcje dla rejestracji oraz logowania (oddzielne funkcjonalnosci) """

#%% Rejestracja

from src.User import User

login = input("Login: ")
password = input("Password: ")

user = User(login, password)
user.register()

#%% Logowanie

from src.User import User

login = input("Login: ")
password = input("Password: ")

user = User(login, password)
user.logIn()