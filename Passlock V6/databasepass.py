# -*- coding: utf-8 -*-
"""
Created on Sat May  6 13:01:24 2023

@author: ryzel
"""

import sqlite3

class Databasepass:
    def __init__(self, db):
        # create data base
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        
        #creating tables 
        passtable = """
            CREATE TABLE IF NOT EXISTS passwordlist (
                passwordID Integer PRIMARY KEY,
                username text,
                website,
                password
                )
            """
        # cursor execution
        self.cur.execute(passtable)
        self.con.commit()
        
# =============================================================================
#     # local method to hold values for drop downsthat used across the systems (wip)
#     def dropdownmenu(self):
#         menuvalues = ("opt1", "opt2", "opt3")
#         return menuvalues 
# =============================================================================
        
    """ CRUD controls """
    
    # Add website, name and password
    def insertpassword(self, username, website, password):
        self.cur.execute("INSERT INTO passwordlist VALUES (NULL,?,?,?)",
                         (username, website, password))
        self.con.commit ()
        
    # display pass list from table
    def viewpassword(self):
        self.cur.execute("SELECT * FROM passwordlist")
        rows = self.cur.fetchall()
        return rows
    
    # Delete password entry from table
    def removepassword(self,passIDvar):
        self.cur.execute("DELETE FROM passwordlist WHERE passwordID=?", (passIDvar,))
        self.con.commit()
    
    # edit password details in the table
    def editpassword(self, passIDvar, username, website, password):
        sql_insert_query = """UPDATE passwordlist SET username=?, website=?, password=? WHERE passwordID=?"""
        self.cur.execute(sql_insert_query, (username, website, password, passIDvar))
        self.con.commit()
     
# =============================================================================
#     # return suitable password list to set the combobox values (wip)
#     def selectpassword(self, username, website, password):
#         sql_select_query = "SELECT name from passwordlist WHERE username=? AND "
#         
# =============================================================================
    # retrieve password details from table to display when assigning
    def getpassword(self, insName):
        if insName == " ":
            return " "
        else:
            self.cur.execute(
                "SELECT username, password, website FROM passwordlist WHERE username=?", (insName,))
 
            result = self.cur.fetchone()
            return result
        
   