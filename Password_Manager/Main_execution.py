# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 06:13:09 2023

@author: ryzel
"""

#Main execution menu
from CRUD_module import PasswordManager

# Create an instance of PasswordManager
password_manager = PasswordManager('PASSDB.db')

while True:
    print("Password manager CLI")
    menu_cursor = input("\n [a] Create new password \n [b] Display all passwords \n [c] Delete pass \n [d] Change pass(WIP) \n [e] Search for Password \n [f] Modify a Password(turns simple password to complex password) \n [z] Exit \n Input: ")
    menu_cursor = menu_cursor.lower()
    if menu_cursor == "a":
        password_manager.create_new_pass()
    elif menu_cursor == "b":
        password_manager.display_users()
    elif menu_cursor == "c":
        password_manager.display_users()
        name = str(input("Input the name of the pass: "))
        password_manager.delete_pass(name)
    elif menu_cursor == "d":
        # Implement the logic for changing password
        updloc = input('what do you need to update(name/pass)?')
        name = input('what is the name that you need to update?')
        upd = input('what is your desired update? ')
        password_manager.update_pass(name, updloc, upd)
    elif menu_cursor == "e":
        search_bar = input("Please Input the name of credential that you need: ")
        password_manager.search_users(search_bar)
    elif menu_cursor == "f":
        passwmod = input("Please input the password that you need to modify: ")
        password_manager.modify_text(passwmod)
    elif menu_cursor == "z":
        password_manager.close_connection()
        break
