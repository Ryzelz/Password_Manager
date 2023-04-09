# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 06:13:09 2023

@author: ryzel
"""
import sqlite3
from input_data import Create_new_pass, display_users

while True:
    print("Password manager CLI")
    menu_cursor = str(input("\n [a] Create new password \n [b] Display all passwords \n [c] Delete pass(WIP) \n [d] Change pass(WIP) \n [z] Exit \n Input: "))
    menu_cursor.lower()
    if menu_cursor == "a":
        Create_new_pass()
    elif menu_cursor == "b":
        display_users()
    elif menu_cursor == "z":
        break