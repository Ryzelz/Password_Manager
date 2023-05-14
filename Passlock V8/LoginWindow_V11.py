# -*- coding: utf-8 -*-
"""
Created on Sat May  6 06:53:57 2023

@author: ryzel
"""
import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
from PIL import Image
import Homepage_V7
from masterfilev2 import MasterClass
from tkinter.messagebox import showinfo
from SendEmailCode import EmailSender
# creating a database object
#db = Database("mainDatabase.db")

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class Login:
    def __init__(self, root):
        self.con = sqlite3.connect('masterdb.db')
        self.c = self.con.cursor()
        
        self.root = root
        
        #master password 
        self.username = StringVar()
        self.password = StringVar()
        
        #self.LoadingImage()
        
        #fogot password
        self.forgotpasskey = StringVar()
        #executing the frame
        self.loginControlFrame()
        
        
    def LoadingImage(self):
        
        self.loading_image = ctk.CTkFrame(self.root, bg_color="red")
        self.loading_image.place(x=100, y=1)
        self.loading_image.lift()
        self.my_image = ctk.CTkImage(light_image=Image.open("Logo_banner(transparent).png"),
                                  dark_image=Image.open("Logo_banner(transparent).png"),
                                  size=(800, 700))
        self.photo_label = ctk.CTkLabel(self.loading_image, image=self.my_image, text = " ", anchor="center")
        self.photo_label.grid(row=0, column=0, padx=150, pady=25)
        
        self.root.after(2000, self.hide_label)

    def hide_label(self):
        self.photo_label.pack_forget()
        
    #executed from the button 'buttonlogin'
    def loginFunc(self):
        #checks if the entry is correct
        try:
            self.usernamee = self.txtusername.get()
            self.passwordd = self.txtpassword.get()
            self.c.execute("SELECT * FROM masteraccount WHERE username=(:usern) AND password=(:passw)",{'usern':self.usernamee,'passw':self.passwordd})
            result = self.c.fetchone()[0]
            print(result)
            if result > 0:      
                try:
                    print("works")
                    a = Homepage_V7.PasswordControls(self.root, self)
                    a.accountinfo()
                finally:
                    self.loginFrame.destroy()
                    self.rightFrame.destroy()
                self
            elif self.txtusername.get() == 'admin' and self.txtpassword.get() == 'admin':
                try:
                    print("works")
                    a = MasterClass(self)
                    a.updateaccount_username()
                    Homepage_V7.PasswordControls(self.root,self)
                finally:
                    self.loginFrame.destroy()
                    self.rightFrame.destroy()
            else:
                messagebox.showerror("Error!", "Check your credentials or Pls contact system admin!")
                self.username.set("")
                self.password.set("")
        except:
            messagebox.showerror("Error!", "Check your credentials or Pls contact system admin!")
            self.username.set("")
            self.password.set("")
            
    #Login Frame
    def loginControlFrame(self):
        self.loginFrame = ctk.CTkFrame(self.root)
        self.loginFrame.place(x=200, y=150)

        #the title from the login entry frame
        self.login_frame_title = ctk.CTkLabel(self.loginFrame, text="Login Here", 
                                          font=("Impact", 35))
        self.login_frame_title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")
        
        # username
        
        self.labelusername = ctk.CTkLabel(self.loginFrame, text="Username", font=("Times New Roman", 16, "bold"))
        self.labelusername.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.txtusername = ctk.CTkEntry(self.loginFrame, textvariable=self.username, font=("Times New Roman", 15), width=100)
        self.txtusername.grid(row = 1, column=1, padx=10, pady=5, sticky="w")
        
        self.txtusername.focus_set()
        self.txtusername.bind('<Return>', lambda event: self.txtpassword.focus_set())
        
        # password
        self.labelpassword = ctk.CTkLabel(self.loginFrame, text="Password", font=("Times New Roman", 16, "bold"))
        self.labelpassword.grid(row=2, column=0, padx=10, pady=5, sticky='w')
        self.txtpassword = ctk.CTkEntry(self.loginFrame, textvariable=self.password, font=("Times New Roman", 15), width=100,show="*")
        self.txtpassword.grid(row = 2, column=1, padx=10, pady=5, sticky="w")
        
        self.revealbutton = ctk.CTkButton(self.loginFrame, text='🔒',
                                          command = self.censhorship_toggle_button, 
                                          width = 30, fg_color = "transparent")
        self.revealbutton.grid(row = 2, column = 2, padx=10, pady=5, sticky="w")
        self.censored = False
        
        # login button
        self.buttonlogin = ctk.CTkButton(self.loginFrame, command=self.loginFunc, text="Login", cursor="hand2")
        self.buttonlogin.grid(row=3, column=0, padx=10, sticky="e")
        
        # empty label for spacing in grid
        self.emptylabel = ctk.CTkLabel(self.loginFrame, font =("Times New Roman", 16, "bold"), text = " ")
        self.emptylabel.grid(row=4, column=1, padx=10, pady=5, sticky="w")
        
        #button for account creation 
        self.buttoncreateaccount = ctk.CTkButton(self.loginFrame, text = "Create account", font =("Times New Roman", 16, "bold"), fg_color = "transparent", width = 30, command = self.createaccount)
        self.buttoncreateaccount.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        
        # forgot password button
        self.buttonforgot = ctk.CTkButton(self.loginFrame, text = "Forgot Passoword?", font =("Times New Roman", 16, "bold"), fg_color = "transparent", width = 30, command = self.forgotpass)
        self.buttonforgot.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        
        # right side frame as welcome message
        self.rightFrame = ctk.CTkFrame(self.root)
        self.rightFrame.place(x=700, y=150)
        
        self.my_image = ctk.CTkImage(light_image=Image.open("Logo_banner(transparent).png"),
                                  dark_image=Image.open("Logo_banner(transparent).png"),
                                  size=(200, 200))
        self.photo_label = ctk.CTkLabel(self.rightFrame, image=self.my_image, text = " ", anchor="center")
        self.photo_label.grid(row=0, column=0, padx=150, pady=25)

        self.labelCompanyName = ctk.CTkLabel(self.rightFrame, text="PASS LOCK", font=("Goudy Old Style", 55))
        self.labelCompanyName.grid(row=1, column=0, columnspan=2, padx=10)
        self.labelDesc = ctk.CTkLabel(self.rightFrame, 
                                      text="Never forgor yer password. \n (▀̿Ĺ̯▀̿ ̿)", 
                                      font=("Times New Roman", 25, "italic"))
        self.labelDesc.grid(row=2, column=0, columnspan=2, padx=10, pady=6)
        
        
    
    def censhorship_toggle_button(self):
        if self.censored:
            self.txtpassword.configure(show="*")
            self.censored = False
            self.revealbutton.configure(text="🔒")
        else:
            self.revealbutton.configure(text="🔓")
            self.txtpassword.configure(show="")
            self.censored = True
    def createaccount(self):
        print("working")
        self.loginFrame.destroy()
        self.rightFrame.destroy()
        
        width_entry = 250
        self.acc_creation_frame = ctk.CTkFrame(self.root)
        self.acc_creation_frame.place(x=500, y=150)
        #filler cause the frame have no padding option
        self.fillerbottom = ctk.CTkLabel(self.acc_creation_frame, text = " ", width = 200)
        self.fillerbottom.grid(row = 20, column = 1)
        self.fillerbottom = ctk.CTkLabel(self.acc_creation_frame, text = " ", width = 200)
        self.fillerbottom.grid(row = 0, column = 1)
        
        self.exit_account_creation = ctk.CTkButton(self.acc_creation_frame, text = "X", 
                                                   command = self.cls_exit_acc_creation,
                                                   fg_color = "transparent", 
                                                   font = ("Calibari", 20),
                                                   width = 10)
        self.exit_account_creation.grid(row = 0, column = 0)
        
        self.titlecreate = ctk.CTkLabel(self.acc_creation_frame, text = "Create Account",
                                        font = ("times new roman", 25))
        self.titlecreate.grid(row = 1, column = 1)
        
        self.username_labelentry = ctk.CTkLabel(self.acc_creation_frame, text = "Username:")
        self.username_labelentry.grid(row = 2, column = 1)
        self.username_entry = ctk.CTkEntry(self.acc_creation_frame, width=width_entry)
        self.username_entry.grid(row = 3, column = 1)
        
        self.username_entry.bind('<Return>', lambda event: self.password_entry.focus_set())
        
        self.password_labelentry = ctk.CTkLabel(self.acc_creation_frame, text = "Password:")
        self.password_labelentry.grid(row = 4, column = 1)
        self.password_entry = ctk.CTkEntry(self.acc_creation_frame, width=width_entry)
        self.password_entry.grid(row = 5, column = 1)
        
        self.password_entry.bind('<Return>', lambda event: self.forgotkey_entry.focus_set())
        
        self.forgotkey_labelentry = ctk.CTkLabel(self.acc_creation_frame, text = "Forgot Pass keyword:")
        self.forgotkey_labelentry.grid(row = 6, column = 1)
        self.forgotkey_entry = ctk.CTkEntry(self.acc_creation_frame, width=width_entry)
        self.forgotkey_entry.grid(row = 7, column = 1)
        
        self.forgotkey_entry.bind('<Return>', lambda event: self.email_entry.focus_set())
        
        self.email_labelentry = ctk.CTkLabel(self.acc_creation_frame, text = "Email:")
        self.email_labelentry.grid(row = 8, column = 1)
        self.email_entry = ctk.CTkEntry(self.acc_creation_frame, width=width_entry)
        self.email_entry.grid(row = 9, column = 1)
        
        self.sendcodeemial_button = ctk.CTkButton(self.acc_creation_frame, text = "Send", 
                                                  width = 20, command = self.send_email)
        self.sendcodeemial_button.grid(row = 9, column = 2)
        
        self.email_entry.bind('<Return>', lambda event: self.emailcode_entry.focus_set())
        
        self.emailcode_labelentry = ctk.CTkLabel(self.acc_creation_frame, text = "Enter code from email")
        self.emailcode_labelentry.grid(row = 10, column = 1)
        self.emailcode_entry = ctk.CTkEntry(self.acc_creation_frame, width=width_entry)
        self.emailcode_entry.grid(row = 11, column = 1)
        
        self.donebutton = ctk.CTkButton(self.acc_creation_frame, text = "Done", command = self.donefunction)
        self.donebutton.grid(row = 12, column = 1, pady=20)
    
    def cls_exit_acc_creation(self):
        self.acc_creation_frame.destroy()
        self.raiseframeaccount()
    def send_email(self):
        email_sender = 'passlock.ltd@gmail.com'
        email_password = 'svdpzvopezcrepnk'
        email_receiver = self.email_entry.get()
        
        email_sender = EmailSender(email_sender, email_password)
        email_sender.send_email(email_receiver)
        
        messagebox.showerror("Cool!", "Check your email account for the code!")
        
    
    def forgotpass_confirmation(self):
        #checks if the entry is correct 
           self.forgotkey = self.forgotpasskey_entry.get()
           if self.forgotkey == "":
               showinfo("ERROR!!!","Please input your forgot key")
           else:
               with self.con:
                   self.c.execute("SELECT password FROM masteraccount WHERE forgotkey = (:forgotk)",{'forgotk':self.forgotkey})
                   self.forgotpasslabel = ctk.CTkLabel(self.forgotpassframe, text = 'Password: {}'.format(self.c.fetchone()) )
                   self.forgotpasslabel.grid(row=3,column=0)
            
    def showforgotpassframe(self):
        self.show_masterpassword = ctk.CTkLabel(self.forgotpassframe, text = "admin (this must connect from master pass sql)")
        self.show_masterpassword.grid(row = 7, column = 0)
        
        
    def forgotpass(self):
        print("workingforgot")
        self.loginFrame.destroy()
        self.rightFrame.destroy()
        
        self.forgotpassframe = ctk.CTkFrame(self.root)
        self.forgotpassframe.place(x=500, y=150)
        pady_widgets=10
        self.title_label = ctk.CTkLabel(self.forgotpassframe, text="Forgot Master Password",
                                        font = ("times new roman", 25, "bold"))
        self.title_label.grid(row = 1, column = 0, pady=pady_widgets)
        
        self.forgotpasskey_label = ctk.CTkLabel(self.forgotpassframe, text = "Keyword: ")
        self.forgotpasskey_label.grid(row=2, column = 0)
        self.forgotpasskey_entry = ctk.CTkEntry(self.forgotpassframe, 
                                                textvariable= self.forgotpasskey)
        self.forgotpasskey_entry.grid(row=3, column = 0, pady=pady_widgets)
        
        self.confirmforgotpasskey_button = ctk.CTkButton(self.forgotpassframe, text = "Confirm", 
                                                         command = self.forgotpass_confirmation)
        self.confirmforgotpasskey_button.grid(row=4, column = 0, pady=pady_widgets)
        
        self.returnloginpage_button = ctk.CTkButton(self.forgotpassframe, text = "exit", 
                                                    command = self.raiseframeforgot)
        self.returnloginpage_button.grid(row = 6, column = 0, pady=pady_widgets)
        
        #filler cause the frame have no padding option
        self.fillerbottom = ctk.CTkLabel(self.forgotpassframe, text = " ", width = 200)
        self.fillerbottom.grid(row = 20, column = 0)
        self.fillerbottom = ctk.CTkLabel(self.forgotpassframe, text = " ", width = 300, fg_color = "transparent")
        self.fillerbottom.grid(row = 0, column = 0)
        
    def donefunction(self):
        if self.emailcode_entry.get() == "911420":
            try:
                self.a=MasterClass(self)
                self.a.createaccount()
            finally:
                self.raiseframeaccount()
        else:
            messagebox.showerror("Error", "Email code does not match ( ఠ ͟ʖ ఠ) " )
        
    def raiseframeaccount(self):
        self.acc_creation_frame.destroy()
        Login(self.root)
    def raiseframeforgot(self):
        self.forgotpassframe.destroy()
        Login(self.root)
#main method
def main():
    root = ctk.CTk()
    root.title("PASS LOCK")
# =============================================================================
#     root.geometry("1400x930+100+50")
#     root.resizable(False, True)
# =============================================================================
    width, height = 1280 , 720  
    #setting the window to center when launched (copy pasted)
    winx = (int(root.winfo_screenwidth() / 2)) - int(width / 2)
    winy = (int(root.winfo_screenheight() / 2)) - int(height / 2)
    root.geometry("{}x{}+{}+{}".format(width, height, winx, winy))

    root.resizable(False, False)
    
    #Initiating the System
    Login(root)

    root.mainloop()

if __name__ == '__main__':
    main() 
        
        
        