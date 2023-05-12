import sqlite3

class Error():
    pass

class PassNotEqualError(Error):
    pass

class MasterClass:
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect('masterdb.db')
        self.c = self.con.cursor()
        self.c.execute("""CREATE TABLE IF NOT EXISTS masteraccount (
            accid integer PRIMARY KEY,
            username text,
            password text
            )""")
        
    #massterclass crud database
    def createaccount(self):
        # try:
            self.username = input("input username: ")
            self.password = input("input password: ")
            self.confirmpass = input("retype your password: ")
            if self.password != self.confirmpass:
                raise PassNotEqualError
            else:
                with self.con:
                    self.c.execute("INSERT INTO masteraccount VALUES(NULL,?,?)",(self.username,self.password))
                    print('account created sucessfully')
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
            accid = input("what id that you will change: ")
            newusername = input("enter new username: ")
            self.c.execute("UPDATE masteraccount SET username = (:newusername) WHERE accid = (:id) ",
                           {'newusername':newusername,'id':accid})
    def updateaccount_password(self):
        with self.con:
            accid = input("what id that you will change: ")
            newpassword = input("enter new password: ")
            self.c.execute("UPDATE masteraccount SET password = (:newpassword) WHERE accid = (:id) ",
                           {'newusername':newpassword,'id':accid})
        
        
            
    
            
a = MasterClass()
a.updateaccount_username()