# -*- coding: utf-8 -*-
"""
Created on Sat May  6 06:53:57 2023

@author: ryzel
"""
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
import Homepage_V4

# creating a database object
#db = Database("mainDatabase.db")

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class Login:
    def __init__(self, root):
        self.root = root
        
        self.insName = StringVar()
        self.username = StringVar()
        self.password = StringVar()
        #executing the frame
        self.loginControlFrame()

    def loginFunc(self):
        if self.txtusername.get() == 'admin' and self.txtpassword.get() == 'admin':
            self.loginFrame.destroy()
            self.rightFrame.destroy()
            print("works")
            Homepage_V4.PasswordControls(self.root)
            
        else:
            messagebox.showerror("Error!", "Check your credentials or Pls contact system admin!")
            self.username.set("")
            self.password.set("")
            
    #Login Frame
    
    def loginControlFrame(self):
        self.loginFrame = ctk.CTkFrame(self.root)
        self.loginFrame.place(x=100, y=150)

        
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
        self.txtpassword = ctk.CTkEntry(self.loginFrame, textvariable=self.password, font=("Times New Roman", 15), width=100)
        self.txtpassword.grid(row = 2, column=1, padx=10, pady=5, sticky="w")
        
        # ery add that reveal button
        self.revealbutton = ctk.CTkButton(self.loginFrame, text = "add reveal button ery")
        self.revealbutton.grid(row = 2, column = 2, padx=10, pady=5, sticky="w")
        
        # login button
        self.buttonlogin = ctk.CTkButton(self.loginFrame, command=self.loginFunc, text="Login", cursor="hand2")
        self.buttonlogin.grid(row=3, column=0, padx=10, sticky="e")
        
        # empty label for spacing in grid
        self.emptylabel = ctk.CTkLabel(self.loginFrame, font =("Times New Roman", 16, "bold"))
        self.emptylabel.grid(row=4, column=1, padx=10, pady=5, sticky="w")
        
        # right side frame as welcome message
        self.rightFrame = ctk.CTkFrame(self.root)
        self.rightFrame.place(x=700, y=150)
        
        self.photo = tk.PhotoImage(file=r"Logo_banner(transparent).png")
        self.photo = self.photo.subsample(2,2)
        self.photo_label = ctk.CTkLabel(self.rightFrame, image=self.photo, fg_color="transparent", text=" ")
        self.photo_label.grid(row=0, column=0, padx=100, pady=10)
        
        self.labelCompanyName = ctk.CTkLabel(self.rightFrame, text="PASS LOCK", font=("Goudy Old Style", 55))
        self.labelCompanyName.grid(row=1, column=0, columnspan=2, padx=10)
        self.labelDesc = ctk.CTkLabel(self.rightFrame, text="Never forgor yer password. \n (▀̿Ĺ̯▀̿ ̿)", font=("Times New Roman", 25, "italic"))
        self.labelDesc.grid(row=2, column=0, columnspan=2, padx=10, pady=6)

        
        
        