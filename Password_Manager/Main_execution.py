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
    menu_cursor = input("\n [a] Create new password \n [b] Display all passwords \n [c] Delete pass \n [d] Change pass(WIP) \n [z] Exit \n Input: ")
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
        pass
    elif menu_cursor == "z":
        password_manager.close_connection()
        break
