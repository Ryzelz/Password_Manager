# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 09:11:14 2023

@author: ryzel
"""

import tkinter

import tkinter as ttk
from tkinter import *
import customtkinter
import os
from PasswordScrollbarRegion import ListFrame, TEST


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        #for automating the window to center
        self.win_width = 600
        self.win_height = 550
        #get the info of the user
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        #centers the window
        self.center_x = int(self.screen_width/2 - self.win_width / 2)
        self.center_y = int(self.screen_height/2 - self.win_height / 2)
        #ability to resize the window with more control
        self.minsize(600, 550)
        self.maxsize(600,550)
        
        
        #frame 1 on the left side
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        
        #adding image
        self.bg_image = tkinter.PhotoImage(file='logo_image.png')
        self.canvas = tkinter.Canvas (self.sidebar_frame, width=150, height=150)
        self.canvas.grid(row=0, column=0, rowspan=1, sticky="nsew", padx=20, pady=(20, 10))
        
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="PassManage", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=1, column=0, padx=20, pady=(20, 10))
        #buttons for the side tab
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Profile", command=self.sidebar_button_profile, fg_color='#D438C9')
        self.sidebar_button_1.grid(row=2, column=0, padx=20, pady=10)
        
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Password", command=self.sidebar_button_passwords, fg_color='#D438C9')
        self.sidebar_button_2.grid(row=3, column=0, padx=20, pady=10)
        
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame,text="History", command=self.sidebar_button_history, fg_color='#D438C9')
        self.sidebar_button_3.grid(row=4, column=0, padx=20, pady=10)
        #added logo
        self.iconbitmap('logo_pass.ico')
# =============================================================================
# no sanity to code
#         #label Categories > Accounts, Add, History
#         #name 
#         self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Categories:", anchor="w")
#         self.appearance_mode_label.grid(row=1, column=0, padx=20, pady=(10, 0))
#         self.appearance_mode_optionmenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Profile", "Add", "History"],
#                                                                        command=self.sidebar_button_event)
#         #the actual dropdown
#         self.appearance_mode_optionmenu.grid(row=2, column=0, padx=20, pady=(10, 10))
# =============================================================================
        
        #appearance
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Change Appearance:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionmenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], 
                                                                      fg_color='#D438C9',
                                                                      button_color='#85217e',
                                                                      command=self.change_appearance_mode_event)
        #the actual dropdown
        self.appearance_mode_optionmenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        #u.i scale
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionmenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"], 
                                                              fg_color='#D438C9', 
                                                              button_color='#85217e',
                                                              command=self.change_scaling_event)
        self.scaling_optionmenu.grid(row=8, column=0, padx=20, pady=(10, 20))
        
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
    def sidebar_button_profile(self):
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.textbox = customtkinter.CTkTextbox(master=self, width=400, corner_radius=0)
        self.textbox.grid(row=0, column=1,padx=20, pady=(10, 10), sticky="nsew")
        self.textbox.insert("0.0", "Some example passwords!\n" * 9)
        
    def sidebar_button_passwords(self):

        # create a root window
        root = tkinter.Tk()
        root.title("Password List")
        root.geometry("400x600")
        
        # create a ListFrame instance
        text_data = [("Item 1", "Pass 1"), ("Item 2", "Pass 2"), ("Item 3", "Pass 3")]  # replace with your actual data
        item_height = 30  # replace with desired item height
        list_frame = ListFrame(root, text_data, item_height)
        list_frame.pack(expand=True, fill='both')
        
        # start the tkinter event loop
        root.mainloop()

    def sidebar_button_history(self):
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.textbox = customtkinter.CTkTextbox(master=self, width=400, corner_radius=0)
        self.textbox.grid(row=0, column=1,padx=20, pady=(10), sticky="nsew")
        self.textbox.insert("0.0", "Some example history!\n")
        
        
app = App()
app.mainloop()

