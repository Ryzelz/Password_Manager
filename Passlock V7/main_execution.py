# -*- coding: utf-8 -*-
"""
Created on Sat May  6 08:38:33 2023

@author: ryzel
"""

from tkinter import *
import LoginWindow_V9
import customtkinter as ctk


def main():
    """The main function of the program."""

    # Create the root window.
    root = ctk.CTk()
    root.title("PASS LOCK")

    # Set the window size.
    root.geometry("1280x720")

    # Center the window on the screen.
    winx = (int(root.winfo_screenwidth() / 2)) - int(root.winfo_width() / 2)
    winy = (int(root.winfo_screenheight() / 2)) - int(root.winfo_height() / 2)
    root.geometry("{}x{}+{}+{}".format(root.winfo_width(), root.winfo_height(), winx, winy))

    # Disable resizing the window.
    root.resizable(False, False)

    # Initialize the login window.
    LoginWindow_V9.Login(root)

    # Start the mainloop.
    root.mainloop()


if __name__ == "__main__":
    # Call the main function.
    main()
