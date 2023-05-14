import sqlite3
from tkinter.messagebox import showinfo

class Error():
    pass

class PassNotEqualError(Error):
    pass

class MasterClass:
    def __init__(self,app):
        self.app = app
        self.con = sqlite3.connect('masterdb.db')
        self.c = self.con.cursor()
        self.c.execute("""CREATE TABLE IF NOT EXISTS masteraccount (
            accid integer PRIMARY KEY,
            username text,
            password text,
            forgotkey text,
            email text
            )""")
        
    #massterclass crud database
    def createaccount(self):
        # try:
            self.accusername= self.app.username_entry.get()
            self.password=self.app.password_entry.get()
            self.forgotkey = self.app.forgotkey_entry.get()
            self.email=self.app.email_entry.get()
            if self.accusername == "":
                showinfo("ERROR!","please input a username!!")
            elif self.password == "":
                showinfo("ERROR!","please input a password!!")
            elif self.forgotkey == "":
                showinfo("ERROR!","please input a forgot key!!")
            elif self.email == "":
                showinfo("ERROR!","please input an email!!")
            else:   
                with self.con:
                    self.c.execute("INSERT INTO masteraccount VALUES(NULL,?,?,?,?)",(self.accusername,self.password,self.forgotkey
                                                                                     ,self.email))
                    showinfo('sucess','account created sucessfully')
        # except PassNotEqualError:
        #     print("password and retake password is not equal")
    def viewaccounts(self):
        with self.con:
            self.c.execute("SELECT * FROM masteraccount")
            self.rows = self.c.fetchall()
            for x in self.rows:
                print(x)
    def updateaccount_username(self):
        with self.con:
            accid = input(" id that you will change: ")
            newusername = input("enter new username: ")
            self.c.execute("UPDATE masteraccount SET username = (:newusername) WHERE accid = (:id) ",
                           {'newusername':newusername,'id':accid})
    def updateaccount_password(self):
        with self.con:
            accid = input("what id that you will change: ")
            newpassword = input("enter new password: ")
            self.c.execute("UPDATE masteraccount SET password = (:newpassword) WHERE accid = (:id) ",
                           {'newusername':newpassword,'id':accid})
        
