# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 05:37:51 2023

@author: ryzel
"""
import sqlite3

#connecting the file database
conn = sqlite3.connect('PASSDB.db')

cursor = conn.cursor()

# Create the "users" table if it doesn't exist
password_table = """CREATE TABLE IF NOT EXISTS users (
    name TEXT NOT NULL,
    password TEXT NOT NULL
);"""

cursor.execute(password_table)
def Create_new_pass():
    name = ""
    password = ""    
    while name or not password:
        #inputs
        name = input("Name: ")
        password = input("Password: ")
        
        # Insert the user's name and password into the "users" table
        password_table = """INSERT INTO users
            (name, password)
            VALUES ('{}','{}');""".format(
                name, password)
        cursor.execute(password_table)
        #saves to the database
        conn.commit()
        print("\n New pass sucessfully created \n")
        if name and password:
             break
        else:
             print("Must include name or password")
def display_users():
    try:
        
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print("Data error.", e)
