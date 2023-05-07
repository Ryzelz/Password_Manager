# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 09:11:14 2023

@author: ryzel
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 08:14:36 2023

@author: ryzel
"""

import tkinter
import tkinter.messagebox
import customtkinter
import base64
import os
from PasswordScrollbarRegion import ListFrame, TEST

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="PassManage", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        #buttons for the side tab
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Profile", command=self.sidebar_button_profile)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Password", command=self.sidebar_button_passwords)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame,text="History", command=self.sidebar_button_history)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        
# =============================================================================
#no time to code
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
                                                                       command=self.change_appearance_mode_event)
        #the actual dropdown
        self.appearance_mode_optionmenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        #u.i scale
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionmenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
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
        
# =============================================================================
#         self.tabview = customtkinter.CTkTabview(self, width=250)
#         self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
#         self.tabview.add("Name: ")
#         self.tabview.add("Would be user name from variable")
#         self.tabview.add("")
#         self.tabview.tab("").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
#         self.tabview.tab("").grid_columnconfigure(0, weight=1)
#     
# =============================================================================
    def sidebar_button_passwords(self):
# =============================================================================
#         self.tabview = customtkinter.CTkTabview(self, width=250)
#         self.tabview.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
#         self.tabview.add("Add")
#         self.tabview.add("Edit")
#         self.tabview.add("Show")
#         self.tabview.tab("").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
#         self.tabview.tab("").grid_columnconfigure(0, weight=1)
# =============================================================================
        # create a root window
        root = tkinter.Tk()
        root.title("Password List")
        root.geometry("400x600")
        
        # create a ListFrame instance
        text_data = [("Item 1", "Value 1"), ("Item 2", "Value 2"), ("Item 3", "Value 3")]  # replace with your actual data
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

