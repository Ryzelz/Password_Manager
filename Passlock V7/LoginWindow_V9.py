# -*- coding: utf-8 -*-
"""
Created on Sat May  6 06:53:57 2023

@author: ryzel
"""
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
import Homepage_V6
from PIL import Image

# creating a database object
#db = Database("mainDatabase.db")

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme(r"\Users\ryzel\OneDrive\Desktop\Password_Manager\Passlock V7\purple.json")  # Themes: "blue" (standard), "green", "dark-blue"

class Login:
    def __init__(self, root):
        self.root = root
        
        #master password 
        self.insName = StringVar()
        self.username = StringVar()
        self.password = StringVar()
        
        #fogot password
        self.forgotpasskey = StringVar()
        #executing the frame
        self.loginControlFrame()
    
    #executed from the button 'buttonlogin'
    def loginFunc(self):
        #checks if the entry is correct 
        if self.txtusername.get() == 'admin' and self.txtpassword.get() == 'admin':
            self.loginFrame.destroy()
            self.rightFrame.destroy()
            print("works")
            Homepage_V6.PasswordControls(self.root)
            
        else:
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
        
        # password
        self.labelpassword = ctk.CTkLabel(self.loginFrame, text="Password", font=("Times New Roman", 16, "bold"))
        self.labelpassword.grid(row=2, column=0, padx=10, pady=5, sticky='w')
        self.txtpassword = ctk.CTkEntry(self.loginFrame, textvariable=self.password, font=("Times New Roman", 15), width=100,show="*")
        self.txtpassword.grid(row = 2, column=1, padx=10, pady=5, sticky="w")
        
        # ery add that reveal button
        self.revealbutton = ctk.CTkButton(self.loginFrame, text='reveal',command = self.censhorship_toggle_button, width = 30)
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
        self.labelDesc = ctk.CTkLabel(self.rightFrame, text="Never forgor yer password. \n (▀̿Ĺ̯▀̿ ̿)", font=("Times New Roman", 25, "italic"))
        self.labelDesc.grid(row=2, column=0, columnspan=2, padx=10, pady=6)
        
        
    def censhorship_toggle_button(self):
        if self.censored:
            self.txtpassword.configure(show="*")
            self.censored = False
            self.revealbutton.configure(text="reveal")
        else:
            self.revealbutton.configure(text="unreveal")
            self.txtpassword.configure(show="")
            self.censored = True
    def createaccount(self):
        print("working")
        self.loginFrame.destroy()
        self.rightFrame.destroy()
        
        self.acccreationframe = ctk.CTkFrame(self.root)
        self.acccreationframe.place(x=150, y=150)
        #filler cause the frame have no padding option
        self.fillerbottom = ctk.CTkLabel(self.acccreationframe, text = " ", width = 200)
        self.fillerbottom.grid(row = 20, column = 1)
        self.fillerbottom = ctk.CTkLabel(self.acccreationframe, text = " ", width = 200)
        self.fillerbottom.grid(row = 0, column = 1)
        
        self.titlecreate = ctk.CTkLabel(self.acccreationframe, text = "Create Account")
        self.titlecreate.grid(row = 1, column = 1)
        
        self.username_labelentry = ctk.CTkLabel(self.acccreationframe, text = "username")
        self.username_labelentry.grid(row = 2, column = 1)
        self.username_entry = ctk.CTkEntry(self.acccreationframe)
        self.username_entry.grid(row = 3, column = 1)
        
        self.password_labelentry = ctk.CTkLabel(self.acccreationframe, text = "password")
        self.password_labelentry.grid(row = 4, column = 1)
        self.password_entry = ctk.CTkEntry(self.acccreationframe)
        self.password_entry.grid(row = 5, column = 1)
        
        self.forgotkey_labelentry = ctk.CTkLabel(self.acccreationframe, text = "Forgot Pass keyword")
        self.forgotkey_labelentry.grid(row = 6, column = 1)
        self.forgotkey_entry = ctk.CTkEntry(self.acccreationframe)
        self.forgotkey_entry.grid(row = 7, column = 1)
        
        self.email_labelentry = ctk.CTkLabel(self.acccreationframe, text = "Enter email")
        self.email_labelentry.grid(row = 8, column = 1)
        self.email_entry = ctk.CTkEntry(self.acccreationframe)
        self.email_entry.grid(row = 9, column = 1)
        
        self.sendcodeemial_button = ctk.CTkButton(self.acccreationframe, text = "Send", width = 20)
        self.sendcodeemial_button.grid(row = 9, column = 2)
        
        self.emailcode_labelentry = ctk.CTkLabel(self.acccreationframe, text = "Enter code from email")
        self.emailcode_labelentry.grid(row = 10, column = 1)
        self.emailcode_entry = ctk.CTkEntry(self.acccreationframe)
        self.emailcode_entry.grid(row = 11, column = 1)
        
        self.donebutton = ctk.CTkButton(self.acccreationframe, text = "Done", command = self.raiseframeaccount)
        self.donebutton.grid(row = 12, column = 1)
    
    def forgotpass_confirmation(self):
        #checks if the entry is correct 
        if self.forgotpasskey_entry.get() == 'hakdog':
            print("works")
            self.showforgotpassframe()
            
        else:
            messagebox.showerror("Error!", "REMEMBER!!!")
            
    def showforgotpassframe(self):
        self.show_masterpassword = ctk.CTkLabel(self.forgotpassframe, text = "admin (this must connect from master pass sql)")
        self.show_masterpassword.grid(row = 7, column = 0)
        
        
    def forgotpass(self):
        print("workingforgot")
        self.loginFrame.destroy()
        self.rightFrame.destroy()
        
        self.forgotpassframe = ctk.CTkFrame(self.root)
        self.forgotpassframe.place(x=150, y=150)
        
        self.title_label = ctk.CTkLabel(self.forgotpassframe, text="Forgot Master Password")
        self.title_label.grid(row = 0, column = 0)
        
        self.forgotpasskey_label = ctk.CTkLabel(self.forgotpassframe, text = "Keyword: ")
        self.forgotpasskey_label.grid(row=1, column = 0)
        self.forgotpasskey_entry = ctk.CTkEntry(self.forgotpassframe, textvariable= self.forgotpasskey)
        self.forgotpasskey_entry.grid(row=2, column = 0)
        
        self.confirmforgotpasskey_button = ctk.CTkButton(self.forgotpassframe, text = "Confirm", command = self.forgotpass_confirmation)
        self.confirmforgotpasskey_button.grid(row=3, column = 0)
        
        self.returnloginpage_button = ctk.CTkButton(self.forgotpassframe, text = "exit", command = self.raiseframeforgot)
        self.returnloginpage_button.grid(row = 6, column = 0)
        
        
    def raiseframeaccount(self):
        self.acccreationframe.destroy()
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
        
        
        