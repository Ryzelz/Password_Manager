# -*- coding: utf-8 -*-
"""
Created on Sat May  6 08:38:33 2023

@author: ryzel
"""

from tkinter import *
import LoginWindow_V7
import customtkinter as ctk

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
    LoginWindow_V7.Login(root)

    root.mainloop()

if __name__ == '__main__':
    main()
