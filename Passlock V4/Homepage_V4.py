# -*- coding: utf-8 -*-
"""
Created on Sat May  6 20:10:08 2023

@author: ryzel
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
import tkinter as tk
import LoginWindow_V7
from databasepass import Databasepass


# creating a database object
db = Databasepass("mainDatabase.db")

class PasswordControls:
    def __init__(self, root):
        self.root = root

        # local variables
        self.website = tk.StringVar()
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        # Call the tkinter frames to the window
        self.passentries()
        self.passwordframebuttons()
        self.tableoutputframe()
        self.imagebg()
    """ Entries """

    def passentries(self):
        padyvar = 5
        padxvar = 10
        # passentries frame configuration
        self.entriesframe = ctk.CTkFrame(self.root)
        self.entriesframe.place(x=500, y=500)
        self.passlock_frame_title = ctk.CTkLabel(self.entriesframe, text="Details", font=("Times New Roman",20))
        self.passlock_frame_title.grid(row = 0, column = 0, padx=padxvar, pady=padyvar, sticky="w")
        #username)
        #website
        self.websitename_entry = ctk.CTkEntry(self.entriesframe, textvariable=self.website, placeholder_text= "website", placeholder_text_color = "dark_color")
        self.websitename_entry.grid(row = 1, column = 0, padx=padxvar, pady=padyvar)
        #username
        self.username_entry = ctk.CTkEntry(self.entriesframe, textvariable=self.username, placeholder_text = "username")
        self.username_entry.grid(row = 2, column = 0, padx=padxvar, pady=padyvar)

        #reselt all entry inputs
        self.reset_button = ctk.CTkButton(self.entriesframe, text="Reset", command=self.resetform)
        self.reset_button.grid(row = 3, column = 0, padx=padxvar, pady=padyvar)

        #password
        self.password_entry = ctk.CTkEntry(self.entriesframe, textvariable=self.password, placeholder_text = "password")
        self.password_entry.grid(row = 1, column = 1, padx=padxvar, pady=padyvar)

        #password reveal
        self.passwordreveal_button = ctk.CTkButton(self.entriesframe, text="reveal")
        self.passwordreveal_button.grid(row = 1, column = 2, padx=padxvar, pady=padyvar)

        #password generate
        self.passwordgenerate_button = ctk.CTkButton(self.entriesframe, text="generate password")
        self.passwordgenerate_button.grid(row = 2, column = 1, padx=padxvar, pady=padyvar)
        
        #password generate
        self.copypass_button = ctk.CTkButton(self.entriesframe, text="copy password")
        self.copypass_button.grid(row = 2, column = 2, padx=padxvar, pady=padyvar)
        
     # event trigger Method to display the chosen data from the TreeView back in respective fields (idk what im doing T_T)
    def getData(self, event):
        try:
            self.selectedRow = self.out.focus()
            self.selectedData = self.out.item(self.selectedRow)
            self.chosenRow = self.selectedData["values"]
            self.username.set(self.chosenRow[1])
            self.website.set(self.chosenRow[2])
            self.password.set(self.chosenRow[3])
        except IndexError as error:
            pass
         
    # create new password
    def addpassword(self):
        if self.username_entry.get() == " " or self.websitename_entry.get() == " " or self.password_entry.get() == " ":
            messagebox.showerror("Error!", "Pls bloody fill all the fields!")
            return
        db.insertpassword(self.username_entry.get(), self.websitename_entry.get(), self.password_entry.get())
        messagebox.showinfo("Success!", "Record Successfully Inserted! ")
        self.resetform()
        self.viewpassword()
        
    # update selected password details
    def updatepassword(self):
        if self.username_entry.get() == " " or self.websitename_entry.get() == " " or self.password_entry.get() == " ":
            messagebox.showerror("Error!", "Pls bloody choose a password to update details!")
            return
        try:
            db.editpassword(self.chosenRow[0], self.username_entry.get(), self.websitename_entry.get(), self.password_entry.get())
            messagebox.showinfo("Success!", "Record successfully updated!")
            self.resetform()
            self.viewpassword()
        except AttributeError as error:
            messagebox.showerror("Error!", "Choose an existing password to Update Details")
    
    # remove selected password from database
    def deletepassword(self):
        try:
            db.removepassword(self.chosenRow[0])
            self.resetform()
            self.viewpassword()
        except AttributeError as error:
            messagebox.showerror("Error!", "Choose an existing password to remove Details")
    # display all password in the treeview frame
    def viewpassword(self):
        self.out.delete(*self.out.get_children())  # emptying the table before reloading
        for row in db.viewpassword():
            self.out.insert("", END, values=row)
    
    # reset all input from the entries frame
    def resetform(self):
        self.password.set("")
        self.website.set("")
        self.username.set("")
    # destroys all frames and outputs the login page
    def logout(self):
        self.entriesframe.destroy()
        LoginWindow_V7.Login(self.root)
    
    """ Buttons for the entries """
    
    def passwordframebuttons(self):
        # button frame configurations
        self.buttonframe = ctk.CTkFrame(self.root)
        self.buttonframe.place(x=0,y=0)
        # title label
        self.passlocklabel = ctk.CTkLabel(self.buttonframe, text="PassLock", font=("Times New Roman",20))
        self.passlocklabel.grid(row=0, column=0, pady=10, padx=10)
        # Display List
        self.viewpassword_button = ctk.CTkButton(self.buttonframe, command=self.viewpassword, text="Password List")
        self.viewpassword_button.grid(row=1, column=0, pady=10, padx=10)
        # add record to database 
        self.add_button = ctk.CTkButton(self.buttonframe, command = self.addpassword, text="Add password")
        self.add_button.grid(row=2, column=0, pady=10, padx=10)
        # update record to database 
        self.update_button = ctk.CTkButton(self.buttonframe, command=self.updatepassword, text="Update password")
        self.update_button.grid(row=3, column=0, pady=10, padx=10)
        # delete record to database
        self.delete_button = ctk.CTkButton(self.buttonframe, command=self.deletepassword, text="Delete password")
        self.delete_button.grid(row=4, column=0, pady=10, padx=10)
        # logout 
        self.logout_button = ctk.CTkButton(self.buttonframe, command=self.logout, cursor="hand2")
        self.logout_button.grid(row=5, column=0, pady=10, padx=10)
    
        
    def tableoutputframe(self):
        # treeview frame config
        self.tableframe = Frame(self.root, bg="#DADDE6")
        self.tableframe.place(x=699, y=0, width=500, height=300)
        self.yscroll = Scrollbar(self.tableframe)
        self.yscroll.pack(side=RIGHT, fill=Y )
        
        #ttk style object to add configurations (will add ctk soon)
        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", font=('Calibri', 12), rowheight=50)
        self.style.configure("mystyle.Treeview.Heading", font=('Times New Roman', 14, "bold"), sticky="w")
        # Formatting the output table view
        self.out = ttk.Treeview(self.tableframe, yscrollcommand=self.yscroll.set,
                                columns=(1, 2, 3, 4), style="mystyle.Treeview")
        self.out.heading("1", text="PasswordID")
        self.out.column("1", width=10)
        self.out.heading("2", text="Username")
        self.out.column("2", width=30)
        self.out.heading("3", text="Website")
        self.out.column("3", width=5)
        self.out.heading("4", text="Password")
        self.out.column("4", width=8)
        self.out['show'] = 'headings'
        
        # Virtual Events to trigger methods
        self.out.bind("<ButtonRelease-1>", self.getData)
        # TreeView output layout configurations
        self.out.pack(fill=X)
        self.yscroll.config(command=self.out.yview)

    def imagebg(self):
        self.imgframe = ctk.CTkFrame(self.root)
        self.imgframe.place(x=200, y=200)
        
        self.photo = tk.PhotoImage(file=r"image.gif")
        self.photo = self.photo.subsample(2,2)
        self.photo_label = ctk.CTkLabel(self.imgframe, image=self.photo, fg_color="transparent", text=" ")
        self.photo_label.grid(row=0, column=0, padx=10, pady=10)
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
    PasswordControls(root)

    root.mainloop()

if __name__ == '__main__':
    main()        
        
        
        
        
        
        
            
            
            
            