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
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users(
                            user_uuid TEXT,
                            name TEXT,
                            password TEXT
                            )''')
        self.conn.commit()

    def create_new_pass(self):
        name = ""
        password = ""
        while name == "" or password == "":
            name = input("Name: ")
            password = input("Password: ")
            user_uuid = str(uuid.uuid4())
            self.cursor.execute(f"INSERT INTO users (user_uuid, name, password) VALUES (?, ?, ?)",
                                (user_uuid, name, password))
            self.conn.commit()
            if name and password:
                print("Account creation successfully executed")
                break
            else:
                print("Must include name and password")

    def display_users(self):
        try:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("|UUID| |NAME| |PASSWORD|")
            self.cursor.execute("SELECT * FROM users")
            for record in self.cursor:
                print(record)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        except sqlite3.Error as e:
            print("Data error.", e)
#Not working code
# =============================================================================
# 
#     def delete_pass(self, uuid_account_deletion):
#         self.cursor.execute("DELETE FROM users WHERE user_uuid = ?", (uuid_account_deletion,))
#         self.conn.commit()
#         print(f"Account {uuid_account_deletion} deleted successfully!")
# 
#     def update_pass(self, user_id, updating_loc, updated_var):
#         self.cursor.execute("UPDATE users SET {} = ? WHERE user_uuid = ?".format(updating_loc),
#                             (updated_var, user_id))
#         self.conn.commit()
#         print(f"Total number of rows updated: {self.conn.total_changes}")
#         table = self.cursor.execute('SELECT * from users')
#         for record in table:
#             print(record)
# 
# =============================================================================
    def close_connection(self):
        self.conn.close()



