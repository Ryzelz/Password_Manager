# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 05:37:51 2023

@author: ryzel
"""
#generate db
import sqlite3
#geenrate random id
import uuid
#connecting the file database
import sqlite3

class PasswordManager:
    def __init__(self, file_name="PASSDB.db"):
        self.conn = sqlite3.connect("PASSDB.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users(
                            name TEXT PRIMARY KEY,
                            password TEXT
                            )''')
        self.conn.commit()

    def create_new_pass(self):
        name = ""
        password = ""
        try:
            while name == "" or password == "":
                name = input("Name: ")
                password = input("Password: ")
                self.cursor.execute(f"INSERT INTO users (name, password) VALUES (?, ?)",
                                    (name, password))
                self.conn.commit()
                if name and password:
                    print("Account creation successfully executed")
                    break
        except:
            print('Name already in use')
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def display_users(self):
        try:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("|NAME| |PASSWORD|")
            self.cursor.execute("SELECT * FROM users")
            for record in self.cursor:
                print(record)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        except sqlite3.Error as e:
            print("Data error.", e)

    def search_users(self,name):
        try:
           print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
           print("|NAME| |PASSWORD|")
           self.cursor.execute("SELECT * FROM users WHERE name=(:name)",{'name':name})
           print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 
        except:
            print("No users.",)
    def delete_pass(self, name):
        try:
            self.cursor.execute(f"DELETE FROM users WHERE name = '{name}'")
            self.conn.commit()
            if name:
                print(f"Account {name} deleted successfully!")
        except:
            print("There is no such name as ", name)
    def update_pass(self, name, updating_loc, updated_var):
        self.cursor.execute("UPDATE users SET {} = (:updvar) WHERE name= (:name)".format(updating_loc),
                            {'updvar':updated_var,'name':name})
        self.conn.commit()
        print(f"Total number of rows updated: {self.conn.total_changes}")
        table = self.cursor.execute('SELECT * from users')
        for record in table:
            print(record)
    def close_connection(self):
        self.conn.close()



