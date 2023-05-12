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
import LoginWindow_V9
from databasepass import Databasepass
from PIL import Image


# creating a database object
db = Databasepass("mainDatabase.db")


ctk.set_default_color_theme(r"\Users\ryzel\OneDrive\Desktop\Password_Manager\Passlock V7\purple.json")  # Themes: "blue" (standard), "green", "dark-blue"



class PasswordControls:
    def __init__(self, root):
        self.root = root

        # local variables
        self.website = tk.StringVar()
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.title = tk.StringVar()
        
        # Call the tkinter frames to the window
        self.passentries()
        self.passwordframebuttons()
        self.tableoutputframe()
        self.imagebg()
        
        self.change_appearance()
    """ Entries """

    def passentries(self):
        padyvar = 5
        padxvar = 10
        # passentries frame configuration
        self.entriesframe = ctk.CTkFrame(self.root, width = 600, height = 600)
        self.entriesframe.place(x=250, y=10)

        
        #header
        self.passlock_frame_title = ctk.CTkLabel(self.entriesframe, 
                                                 text="Details", 
                                                 font=("Times New Roman",20))
        self.passlock_frame_title.grid(row = 0, column = 0, 
                                       padx=padxvar, pady=padyvar, 
                                       sticky="w")
        #title
        self.passtitle_label = ctk.CTkLabel(self.entriesframe,
                                            text = "Title: ")
        self.passtitle_label.grid(row = 1, column = 0, sticky="w")
        self.passtitle_entry = ctk.CTkEntry(self.passtitle_label, 
                                            textvariable=self.title)
        self.passtitle_entry.grid(row = 0, column = 1, sticky="e", 
                                  padx = 35)
        
        #website
        self.websitename_label = ctk.CTkLabel(self.entriesframe,
                                            text = "Website:")
        self.websitename_label.grid(row = 2, column = 0, sticky="w")
        self.websitename_entry = ctk.CTkEntry(self.websitename_label, 
                                              textvariable=self.website)
        self.websitename_entry.grid(row = 0, column = 1, 
                                    padx=20, pady=padyvar, sticky="e")
        
        #username
        self.username_label = ctk.CTkLabel(self.entriesframe,
                                            text = "Username:")
        self.username_label.grid(row = 3, column = 0, sticky="w")
        self.username_entry = ctk.CTkEntry(self.username_label, 
                                           textvariable=self.username, 
                                           placeholder_text = "username")
        self.username_entry.grid(row = 0, column = 1, 
                                 padx=padxvar, pady=padyvar, sticky="e")

        #reselt all entry inputs
        self.reset_button = ctk.CTkButton(self.entriesframe, text="Reset", 
                                          command=self.resetform, 
                                          width = 30)
        self.reset_button.grid(row = 9, column = 0, 
                               padx=padxvar, pady=padyvar, sticky = "w")

        #password
        self.password_label = ctk.CTkLabel(self.entriesframe,
                                            text = "Password:")
        self.password_label.grid(row = 4, column = 0, sticky="w")
        self.password_entry = ctk.CTkEntry(self.password_label, 
                                           textvariable=self.password, 
                                           placeholder_text = "password",
                                           show="*")
        self.password_entry.grid(row = 0, column = 1, 
                                 padx=padxvar, pady=padyvar, sticky="e")

        #password reveal
        self.passwordreveal_button = ctk.CTkButton(self.password_label, 
                                                   text="🔒", 
                                                   width = 10,
                                                   fg_color= "transparent",
                                                   command = self.censhorship_toggle_button)
        self.passwordreveal_button.grid(row = 0, column = 2)
        self.censored = False
        #password generate
        self.copypass_button = ctk.CTkButton(self.password_label, 
                                             text="📋", 
                                             width = 10,
                                             fg_color= "transparent")
        self.copypass_button.grid(row = 0, column = 3)
        #password generate
        self.passwordgenerate_button = ctk.CTkButton(self.password_label, 
                                                     text="generate password", 
                                                     command = self.generatepassword,
                                                     fg_color = "transparent",
                                                     text_color = "#a99a89")
        self.passwordgenerate_button.grid(row = 2, column = 1, 
                                          padx=padxvar, pady=padyvar)
        
        
#==================================================================================
#==================================================================================    
    # create new password
    def addpassword(self):
        #prevents blank spaces accepting into database
        if self.username_entry.get() == "" or self.websitename_entry.get() == "" or self.password_entry.get() == "" or self.passtitle_entry.get() == "":
            messagebox.showerror("Error!", "Pls bloody fill all the fields!")
            return
        db.insertpassword(self.passtitle_entry.get(), self.username_entry.get(), self.websitename_entry.get(), self.password_entry.get())
        messagebox.showinfo("Success!", "Record Successfully Inserted! ")
        #resets the entries from the details
        self.resetform()
        #automatically open the treeview
        self.viewpassword()
        
    # update selected password details
    def updatepassword(self):
        if self.username_entry.get() == "" or self.websitename_entry.get() == "" or self.password_entry.get() == "" or self.passtitle_entry.get() == "":
            messagebox.showerror("Error!", "Pls bloody choose a password to update details!")
            return
        try:
            db.editpassword(self.chosenRow[0], self.passtitle_entry.get(), self.username_entry.get(), self.websitename_entry.get(), self.password_entry.get())
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
#==================================================================================
#==================================================================================
    # event trigger Method to display the chosen data from the TreeView back in respective fields (idk what im doing T_T)
    def getdata(self, event):
        try:
            self.selectedRow = self.out.focus()
            self.selectedData = self.out.item(self.selectedRow)
            self.chosenRow = self.selectedData["values"]
            self.title.set(self.chosenRow[1])
            self.username.set(self.chosenRow[2])
            self.website.set(self.chosenRow[3])
            self.password.set(self.chosenRow[4])
        #pass 💀
        except IndexError as error:
            pass
        
    def censhorship_toggle_button(self):
        if self.censored:
            self.password_entry.configure(show="*")
            self.censored = False
            self.passwordreveal_button.configure(text="🔒")
        else:
            self.passwordreveal_button.configure(text="🔓")
            self.password_entry.configure(show="")
            self.censored = True
#==================================================================================
#==================================================================================   
    # reset all input from the entries frame
    def resetform(self):
        self.password.set("")
        self.website.set("")
        self.username.set("")
        self.title.set("")
    # destroys all frames and outputs the login page
    def logout(self):
        self.entriesframe.destroy()
        self.buttonframe.destroy()
        self.tableframe.destroy()
        self.imgframe.destroy()
        self.appearanceframe.destroy()
        LoginWindow_V9.Login(self.root)
#==================================================================================  
    """ Buttons for the entries """
    
    def passwordframebuttons(self):
        widthvar = 200
        heightvar = 30
        # button frame configurations
        self.buttonframe = ctk.CTkFrame(self.root)
        self.buttonframe.place(x=10,y=10)
        # title label
        self.passlocklabel = ctk.CTkLabel(self.buttonframe, text="PassLock", font=("Times New Roman",20))
        self.passlocklabel.grid(row=0, column=0, pady=10, padx=10)
        # Display List
        self.viewpassword_button = ctk.CTkButton(self.buttonframe, 
                                                 command=self.viewpassword, 
                                                 text="Password List", 
                                                 width = widthvar, 
                                                 height = heightvar)
        self.viewpassword_button.grid(row=1, column=0, pady=10, padx=10)
        # add record to database 
        self.add_button = ctk.CTkButton(self.buttonframe, 
                                        command = self.addpassword, 
                                        text="Add password", 
                                        width = widthvar, 
                                        height = heightvar)
        self.add_button.grid(row=2, column=0, pady=10, padx=10)
        # update record to database 
        self.update_button = ctk.CTkButton(self.buttonframe, 
                                           command=self.updatepassword, 
                                           text="Update password", 
                                           width = widthvar, 
                                           height = heightvar)
        self.update_button.grid(row=3, column=0, pady=10, padx=10)
        # delete record to database
        self.delete_button = ctk.CTkButton(self.buttonframe, 
                                           command=self.deletepassword, 
                                           text="Delete password", 
                                           width = widthvar, 
                                           height = heightvar)
        self.delete_button.grid(row=4, column=0, pady=10, padx=10)
        # account
        self.account_button = ctk.CTkButton(self.buttonframe, text="Account", 
                                           command=self.accountinfo, 
                                           cursor="hand2", 
                                           width = widthvar, 
                                           height = heightvar)
        self.account_button.grid(row=5, column=0, pady=10, padx=10)
        # logout 
        self.logout_button = ctk.CTkButton(self.buttonframe, text="Log Out", 
                                           command=self.logout, 
                                           cursor="hand2", 
                                           width = widthvar, 
                                           height = heightvar)
        self.logout_button.grid(row=6, column=0, pady=10, padx=10)
        
#==================================================================================
#================================================================================== 
    #a frame to generate some random characters for out password  
    def generatepassword(self): 
        self.genpassframe = ctk.CTkFrame(self.root)
        self.genpassframe.place(x = 500, y =300)
        
        #destroys the frame
        self.exitpassgen = ctk.CTkButton(self.genpassframe, text = "❌", 
                                         width = 20, height = 20, 
                                         corner_radius=1000, 
                                         command = self.exitpassgen)
        self.exitpassgen.grid(row = 0, column = 0, padx = 10)
        
        self.genpass_header = ctk.CTkLabel(self.genpassframe, 
                                           text = "Password Generator")
        self.genpass_header.grid(row = 0, column = 1, 
                                 padx = 10)
        
        #this is where the output of the generated password
        passwordoutputtext = "<password generated>"
        self.passwordoutput = ctk.CTkLabel(self.genpassframe, 
                                           text = passwordoutputtext)
        self.passwordoutput.grid(row = 1, column = 1, 
                                 padx = 10)
        
        """frame within a frame"""
#===============================================================================
        self.genpassframestatus = ctk.CTkFrame(self.genpassframe)
        self.genpassframestatus.grid(row = 2, column = 1, 
                                     padx = 10)
        
        #the output of the pass strength
        self.passstatus_label = ctk.CTkLabel(self.genpassframestatus, 
                                             text = "🦾stronk pass \n 👺 weak pass")
        self.passstatus_label.grid(row = 0, column = 0, 
                                   padx = 10)
        #makes a new one 
        self.newranoutput_button = ctk.CTkButton(self.genpassframestatus, 
                                                 text = "redo", 
                                                 command = self.redopassgenerated,
                                                 width = 10)
        self.newranoutput_button.grid(row = 0, column = 1, 
                                      padx = 10)
        #clipboard
        self.copypassword_button = ctk.CTkButton(self.genpassframestatus, 
                                                 text = "copy", 
                                                 command = self.copypasswordtoentry,
                                                 width = 1)
        self.copypassword_button.grid(row = 0, column = 2, 
                                      padx = 10)
        
#===============================================================================
        #fill button 
        self.fillpassword_button = ctk.CTkButton(self.genpassframe, 
                                                 text = "fill password",
                                                 command = self.fillpassword)
        self.fillpassword_button.grid(row = 3, column = 1, padx = 10)
        
        #a parameter to change the number of the password characters
        self.passwordlength_label = ctk.CTkLabel(self.genpassframe, 
                                                 text = "Length: ")
        self.passwordlength_label.grid(row = 4, column = 1)
        
        self.passwordlength_slider = ctk.CTkSlider(self.passwordlength_label, 
                                                   from_=8, to=100)
        self.passwordlength_slider.grid(row = 0, column = 1)
#===============================================================================

#===============================================================================
    #all the methods from the button must go here
    def redopassgenerated(self):
        #add redo button
        pass
    def copypasswordtoentry(self):
        #copy password t oentry
        pass
    def fillpassword(self):
        #fill pass method here
        pass
    def exitpassgen(self):
        self.genpassframe.destroy()
        self.passwordlength_label.destroy()
    
#=================================================================================
#===============================================================================
    def accountinfo(self):
        self.account_info = ctk.CTkFrame(self.root)
        self.account_info.place(x=250, y=400)
        
        self.exit_button = ctk.CTkButton(self.account_info, text = "❌", 
                                         command = self.exitaccountinfo, 
                                         width = 20, height = 20,)
        self.exit_button.grid(row = 0, column = 0, padx = 9, pady = 9)
        
        self.masteraccount_title = ctk.CTkLabel(self.account_info,
                                                text = "Account Details"
                                                , anchor = "center")
        self.masteraccount_title.grid(row = 0, column = 1)
        
        self.masteremail_label = ctk.CTkLabel(self.account_info, text = "sample@email.com")
        self.masteremail_label.grid(row = 1, column = 1)
        
        self.masteraccounteditframe = ctk.CTkFrame(self.account_info)
        self.masteraccounteditframe.grid(row = 2, column = 1)
        
        self.masterusernameentry_label = ctk.CTkLabel(self.masteraccounteditframe, text = "Username: ")
        self.masterusernameentry_label.grid(row = 2, column = 1)
        self.masterusername_entry = ctk.CTkLabel(self.masteraccounteditframe, text = "<username_placeholder>")
        self.masterusername_entry.grid(row = 2, column = 2)
        
        self.masterpasswordentry_label = ctk.CTkLabel(self.masteraccounteditframe, text = "Password: ")
        self.masterpasswordentry_label.grid(row = 3, column = 1)
        self.masterpassword_entry = ctk.CTkLabel(self.masteraccounteditframe, text = "<password_placeholder>")
        self.masterpassword_entry.grid(row = 3, column = 2)
        
        self.masteremailentry_label = ctk.CTkLabel(self.masteraccounteditframe, text = "EMail: ")
        self.masteremailentry_label.grid(row = 4, column = 1)
        self.masteremail_entry = ctk.CTkLabel(self.masteraccounteditframe, text = "email_placeholder")
        self.masteremail_entry.grid(row = 4, column = 2)
        
        self.forgotkeyentry_label = ctk.CTkLabel(self.masteraccounteditframe, text = "ForgotKey: ")
        self.forgotkeyentry_label.grid(row = 5, column = 1)
        self.forgotkey_entry = ctk.CTkLabel(self.masteraccounteditframe, text = "forgotkey_placeholder")
        self.forgotkey_entry.grid(row = 5, column = 2)
        
        self.updatemasterusername_button = ctk.CTkButton(self.account_info, text = "Update Master Username",
                                                         command = self.updatemasterusername_frame)
        self.updatemasterusername_button.grid(row = 3, column = 1)
        
        self.updatemasterpassword_button = ctk.CTkButton(self.account_info, text = "Update Master Password",
                                                         command = self.updatemasterpassword_frame)
        self.updatemasterpassword_button.grid(row = 4, column = 1)
        
        self.delete_button = ctk.CTkButton(self.account_info, text = "Delete")
        self.delete_button.grid(row = 5, column = 1)
        
        self.filler = ctk.CTkLabel(self.account_info, text= " ", width = 315)
        self.filler.grid(row = 10, column = 1)
        
    def exitaccountinfo(self):
        self.account_info.destroy()
    def updatemasterusername_frame(self):
        self.updt_masterusername_frame = ctk.CTkFrame(self.root)
        self.updt_masterusername_frame.place(x = 500, y = 500)
        
        self.updateusername_label = ctk.CTkLabel(self.updt_masterusername_frame, text = "Username:")
        self.updateusername_label.grid(row = 0, column = 1)
        
        self.updateusername_entry = ctk.CTkEntry(self.updt_masterusername_frame)
        self.updateusername_entry.grid(row = 1, column = 1)
        
        self.confirm_button = ctk.CTkButton(self.updt_masterusername_frame, text = "Confirm",
                                            command = self.confirm_updatemasterusername)
        self.confirm_button.grid(row = 2, column = 1)
        
        self.updtmasterusername_exit_button = ctk.CTkButton(self.updt_masterusername_frame, text = "❌",
                                                            command = self.exitupdatemasterusername_frame)
        self.updtmasterusername_exit_button.grid(row = 0, column = 0)
    def exitupdatemasterusername_frame(self):
        self.updt_masterusername_frame.destroy()
    def confirm_updatemasterusername(self):
        messagebox.showinfo("Success!", "Master Record Successfully Inserted! ")
        self.updt_masterusername_frame.destroy()
        
    def updatemasterpassword_frame(self):
        self.updt_masterpassword_frame = ctk.CTkFrame(self.root)
        self.updt_masterpassword_frame.place(x = 500, y = 500)
        
        self.updatepassword_label = ctk.CTkLabel(self.updt_masterpassword_frame, text = "Password:")
        self.updatepassword_label.grid(row = 0, column = 1)
        
        self.updatepassword_entry = ctk.CTkEntry(self.updt_masterpassword_frame)
        self.updatepassword_entry.grid(row = 1, column = 1)
        
        self.confirm_button = ctk.CTkButton(self.updt_masterpassword_frame, text = "Confirm",
                                            command = self.confirm_updatemasterpassword)
        self.confirm_button.grid(row = 2, column = 1)
        
        self.updtmasterpassword_exit_button = ctk.CTkButton(self.updt_masterpassword_frame, text = "❌",
                                                            command = self.exitupdatemasterpassword_frame)
        self.updtmasterpassword_exit_button.grid(row = 0, column = 0)
    def exitupdatemasterpassword_frame(self):
        self.updt_masterpassword_frame.destroy()
    def confirm_updatemasterpassword(self):
        messagebox.showinfo("Success!", "Master Record Successfully Inserted! ")
        self.updt_masterpassword_frame.destroy()
#===============================================================================
#==================================================================================   
    def change_appearance_mode_event(self, new_appearance_mode: str):

        if new_appearance_mode == "Light":
            colormode_value = 0
        elif new_appearance_mode == "Dark":
            colormode_value = 1
        elif new_appearance_mode == "System":
            colormode_value = 1
        ctk.set_appearance_mode(new_appearance_mode)

        return colormode_value 
    
        """ List from the main database """
    def tableoutputframe(self):
        # treeview frame config
        self.tableframe = Frame(self.root)
        self.tableframe.place(x=750, y=10, width=850, height=880)
        self.yscroll = Scrollbar(self.tableframe)
        self.yscroll.pack(side=RIGHT, fill=Y )
        
        colormode_value = 1

        #ttk style object to add configurations
        #changes the color of the environment
        self.style = ttk.Style()
        self.style.theme_use('default')
        self.style.configure("mystyle.Treeview", font=('Calibri', 12), rowheight=100)
        self.style.configure("mystyle.Treeview.Heading", font=('Times New Roman', 14, "bold"), sticky="w", 
                        background=ctk.ThemeManager.theme["CTkFrame"]["fg_color"][colormode_value], 
                        foreground=ctk.ThemeManager.theme["CTkLabel"]["text_color"][colormode_value],
                        fieldbackground=ctk.ThemeManager.theme["CTkFrame"]["fg_color"][colormode_value],
                        borderwidth=0)
        self.style.map("mystyle.Treeview.Heading",
                       background=[('hover', ctk.ThemeManager.theme["CTkFrame"]["fg_color"][colormode_value])],
                       highlightcolor=[('hover', ctk.ThemeManager.theme["CTkFrame"]["fg_color"][colormode_value])]
                       )
        # sets the color of the treeview to any color I set in appearance automatically by 1 dark, light 0
        self.style.configure("Treeview", sticky="w", font=('Times New Roman', 14),
                        background=ctk.ThemeManager.theme["CTkFrame"]["fg_color"][colormode_value], 
                        foreground=ctk.ThemeManager.theme["CTkLabel"]["text_color"][colormode_value],
                        fieldbackground=ctk.ThemeManager.theme["CTkFrame"]["fg_color"][colormode_value],
                        borderwidth=0)
        self.style.map('Treeview', background=[('selected', ctk.ThemeManager.theme["CTkFrame"]["fg_color"][colormode_value])],
              foreground=[('selected', ctk.ThemeManager.theme["CTkButton"]["fg_color"][colormode_value])] , anchor = "center")
        # Formatting the output table view
        self.out = ttk.Treeview(self.tableframe, yscrollcommand=self.yscroll.set,
                                columns=(1, 2, 3, 4), style="mystyle.Treeview")
        #configuring the columns 
        self.out.heading("1", text="PasswordID")
        self.out.column("1", width=8, anchor = "center")
        self.out.heading("2", text="Title")
        self.out.column("2", width=10, anchor = "center")
        self.out.heading("3", text="Username")
        self.out.column("3", width=30, anchor = "center")
        self.out.heading("4", text="Website")
        self.out.column("4", width=5, anchor = "center")
# =============================================================================
#         self.out.heading("5", text="Password")
#         self.out.column("5", width=8, anchor = "center")
# =============================================================================
        self.out['show'] = 'headings'
        
        # Virtual Events to trigger methods
        self.out.bind("<ButtonRelease-1>", self.getdata)
        # TreeView output layout configurations
        self.out.pack(fill=X)
        self.yscroll.config(command=self.out.yview)

#==================================================================================
    #meme image
    def imagebg(self):
        self.imgframe = ctk.CTkFrame(self.root)
        self.imgframe.place(x=600, y=400)
        
        self.photo = tk.PhotoImage(file=r"image.gif")
        self.photo = self.photo.subsample(2,2)
        self.photo_label = ctk.CTkLabel(self.imgframe, image=self.photo, fg_color="transparent", text=" ")
        self.photo_label.grid(row=0, column=0, padx=10, pady=10)
#==================================================================================
       
    def change_appearance(self):
        self.appearanceframe = ctk.CTkFrame(self.root)
        self.appearanceframe.place(x=50, y=500)
        
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.appearanceframe, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid()
        
    def change_appearance_mode_event(self, new_appearance_mode: str):
        print(new_appearance_mode)
        if new_appearance_mode == "Light":
            colormode_value = 0
        elif new_appearance_mode == "Dark":
            colormode_value = 1
        elif new_appearance_mode == "System":
            colormode_value = 1
        ctk.set_appearance_mode(new_appearance_mode)

        
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
        
        
        
        
        
        
            
            
            
            