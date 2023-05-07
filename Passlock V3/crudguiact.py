import tkinter as tk
import sqlite3
from tkinter.messagebox import showinfo
from tkinter import ttk 
import random
import pyperclip

class UserManagementSystem:
    def __init__(self):
        #setting window appearance
        self.root = tk.Tk()
        self.root.title('PASS LOCK')
        #background color
        self.bgframe_color = "#620054"
        #button colors
        self.bg_color = "#8D047A"
        self.fg_color = "white"
        width = 500
        height = 600
        #centers the screen 
        winx = (int(self.root.winfo_screenwidth() / 2)) - int(width / 2)
        winy = (int(self.root.winfo_screenheight() / 2)) - int(height / 2)
        self.root.geometry("{}x{}+{}+{}".format(width, height, winx, winy))
        self.root.resizable(True, True)
        self.root.config(bg=self.bgframe_color)
        self.connection = sqlite3.connect("user_data.db", timeout=10)
        self.create_user_table()
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Create frames
        self.frame1 = tk.Frame(self.root, bg=self.bgframe_color)
        self.frame1.place(relx=0.5, rely=0.5, anchor='center')

        # Create the user interface elements
        self.add_user_button = tk.Button(self.frame1, text="Add User", command=self.add_user_tab, bg=self.bg_color, fg=self.fg_color, font=("Arial", 14), width=20, height=2)
        self.add_user_button.grid(row=0, column=0, padx=5, pady=5)
        
        self.view_users_button = tk.Button(self.frame1, text="View Users", command=self.view_users_tab, bg=self.bg_color, fg=self.fg_color, font=("Arial", 14), width=20, height=2)
        self.view_users_button.grid(row=1, column=0, padx=5, pady=5)
        
        self.password_generator_button = tk.Button(self.frame1, text="Password Generator",command=self.password_generator_tab,bg=self.bg_color, fg=self.fg_color, font=("Arial", 14), width=20, height=2)
        self.password_generator_button.grid(row=2,column=0, padx=5, pady=5)
        #exit button
        self.exitbutton = tk.Button(self.frame1,text ='Exit',command=self.exitfunc, bg=self.bg_color, fg=self.fg_color, font=("Arial", 14), width=20, height=2)
        self.exitbutton.grid(row=3,column=0,padx=5,pady=5)
    
    #new function
    def exitfunc(self):
        self.root.destroy()
    def create_user_table(self):
        """Function to create the user data table."""
        query = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        );
        """
        self.connection.execute(query)

    def add_user_tab(self):
        #setting window appearance
        self.add_user_window = tk.Toplevel(self.root)
        #app title
        self.add_user_window.title('PASS LOCK')
        width = 500
        height = 600
        #centers the screen 
        winx = (int(self.add_user_window.winfo_screenwidth() / 2)) - int(width / 2)
        winy = (int(self.add_user_window.winfo_screenheight() / 2)) - int(height / 2)
        self.add_user_window.geometry("{}x{}+{}+{}".format(width, height, winx, winy))
        self.add_user_window.resizable(True, True)
        self.add_user_window.config(bg=self.bgframe_color)

        #setting frame
        self.frame2 = tk.Frame(self.add_user_window, bg=self.bgframe_color)
        self.frame2.place(relx=0.5, rely=0.5, anchor='center')
        #setting window labels
        self.username_label = tk.Label(self.frame2, text="Username:", font=("Arial", 14),bg=self.bg_color, fg=self.fg_color)
        self.username_label.grid(row=0, column=0, padx=5, pady=5)
        
        self.username_entry = tk.Entry(self.frame2, font=("Arial", 14), bg=self.bg_color, fg=self.fg_color)
        self.username_label.grid(row=0, column=0, padx=5, pady=5)
        self.username_entry.grid(row=1, column=0, padx=5, pady=5)
        
        self.password_label = tk.Label(self.frame2, text="Password:", font=("Arial", 14),bg=self.bg_color, fg=self.fg_color)
        self.password_label.grid(row=2, column=0, padx=5, pady=5)
        
        self.password_entry = tk.Entry(self.frame2, show="*", font=("Arial", 14),bg=self.bg_color, fg=self.fg_color)
        self.password_entry.grid(row=3, column=0, padx=5, pady=5)
        
        self.add_user_button = tk.Button(self.frame2, text="Add User", command=self.add_user,bg=self.bg_color, fg=self.fg_color, font=("Arial", 14), width=20, height=2)
        self.add_user_button.grid(row=4, column=0, padx=5, pady=5)
        self.add_user_button.config(height=1)
        
        self.result_label = tk.Label(self.frame2, text="", font=("Arial", 12),bg=self.bg_color, fg=self.fg_color, highlightthickness=0)
        self.result_label.grid(row=6, column=0, padx=5, pady=5)
        
        self.back_button = tk.Button(self.frame2,text="Back",command=self.close_window_add_user,bg=self.bg_color, fg=self.fg_color, font=("Arial", 14), width=20, height=2)
        self.back_button.config(height=1)
        self.back_button.grid(row=5,column=0,padx=5,pady=5)
        #new button
        self.photo_button = tk.PhotoImage(file='seebutton.png')
        self.censor_button = tk.Button(self.frame2, image=self.photo_button, command=self.censhorship_toggle_button, bg=self.bg_color, fg=self.fg_color)
        self.censor_button.grid(row=3, column=1,padx=5,pady=5)
        self.censored = False
        
    def censhorship_toggle_button(self):
        if self.censored:
            self.password_entry.configure(show="*")
            self.censored = False
            self.censor_button.config(image=self.photo_button)
        else:
            self.close_button = tk.PhotoImage(file='closebutton.png')
            self.censor_button.config(image=self.close_button)
            self.password_entry.configure(show="")
            self.censored = True
    def close_window_add_user(self):
        #function for exiting window
        self.add_user_window.destroy()
    
    def add_user(self):
        """Function to add a new user to the database."""
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username and password:
            self.add_user_to_database(username, password)
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.update_view_window()
        else:
            self.result_label.config(text="Username or password cannot be empty.")

    def update_view_window(self):
        """Function to update the contents of the view users window."""
        if hasattr(self, "view_window") and self.view_window is not None:
            self.view_window.destroy()
            self.view_window = None
            self.view_users_tab()
    
    def add_user_to_database(self, username, password):
        """function in adding the entry into the database"""
        select_query = "SELECT * FROM users WHERE username = ?"
        insert_query = "INSERT INTO users (username, password) VALUES (?, ?)"
        cursor = self.connection.cursor()
        cursor.execute(select_query, (username,))
        result = cursor.fetchone()
        if result is not None:
            self.result_label.config(text="Username already exists")
            return
        else:
            self.result_label.config(text="User added successfully")
        cursor.execute(insert_query, (username, password))
        self.connection.commit()
        
    def close_window_view_users(self):
        self.view_window.destroy()
         
    def view_users_tab(self):
        """Function to display the view users tab."""
        self.view_window = tk.Toplevel(self.root)
        #app title
        self.view_window.title('PASS LOCK')
        width = 500
        height = 600
        #centers the screen 
        winx = (int(self.view_window.winfo_screenwidth() / 2)) - int(width / 2)
        winy = (int(self.view_window.winfo_screenheight() / 2)) - int(height / 2)
        self.view_window.geometry("{}x{}+{}+{}".format(width, height, winx, winy))
        self.view_window.resizable(True, True)
        self.view_window.config(bg=self.bgframe_color)
        self.display_users()

    def display_users(self):
        """Function to display all users in the database."""
        query = "SELECT username FROM users;"
        result = self.connection.execute(query)
        users = result.fetchall()
        pass_query = "SELECT password FROM users"
        passs_result = self.connection.execute(pass_query)
        passs = passs_result.fetchall()
        
        if not users:
            no_user_label = tk.Label(self.view_window, text="No users found.", font=("Arial", 14), bg="white")
            no_user_label.pack(pady=10)
            self.back_button = tk.Button(self.view_window,text='back',command = self.close_window_view_users)
            self.back_button.pack(pady=10)
        # Create a Listbox to display users
        self.username = tk.Label(self.view_window,text="UserName",font=("Arial", 12),bg=self.bg_color, fg=self.fg_color)
        self.username.grid(row=0,column=0,padx=50,sticky="se")
        
        user_listbox = tk.Listbox(self.view_window, font=("Arial", 12), width= 20, bg=self.bg_color, fg=self.fg_color)
        user_listbox.grid(row=1, column=0,padx=10, sticky="ne")
        
        self.password = tk.Label(self.view_window,text="password",font=("Arial", 12),bg=self.bg_color, fg=self.fg_color)
        self.password.grid(row=0,column=1,padx=50,sticky="sw")
        
        pass_listbox = tk.Listbox(self.view_window, font=("Arial", 12), width= 20, bg=self.bg_color, fg=self.fg_color)
        pass_listbox.grid(row=1, column=1,padx=10, sticky="nw")
        # Populate Listbox with user data
        for passw in passs:
            pass_listbox.insert(tk.END,passw)
        for user in users:
            user_listbox.insert(tk.END, user)
    
        # Create and pack the password entry, edit and delete buttons
        self.back_button_viewusers = tk.Button(self.view_window,text="back",command=self.close_window_view_users, bg=self.bg_color, fg=self.fg_color)
        self.back_button_viewusers.grid(row=6, column=0, columnspan=2, pady=5)
        
        self.delete_user_button = tk.Button(self.view_window, text="Delete User", command=lambda: self.delete_user(self.user_edit_entry.get()), bg=self.bg_color, fg=self.fg_color , font=("Arial", 14))
        self.delete_user_button.grid(row=5, column=0, columnspan=2, pady=5)
        
        self.edit_password_button = tk.Button(self.view_window, text="Edit Password", command=lambda: self.edit_password(self.user_edit_entry.get(), self.edit_password_entry.get()), bg=self.bg_color, fg=self.fg_color , font=("Arial", 14))
        self.edit_password_button.grid(row=4, column=0, columnspan=2, pady=5)
        
        self.edit_password_label = tk.Label(self.view_window,text="Enter new password",font=("Arial",12), bg=self.bg_color, fg=self.fg_color)
        self.edit_password_label.grid(row=3,column=0,padx=2,sticky=tk.E)
        
        self.edit_password_entry = tk.Entry(self.view_window, font=("Arial", 12), show="*", bg=self.bg_color, fg=self.fg_color)
        self.edit_password_entry.grid(row=3, column=1, columnspan=2,padx=2, pady=5,sticky=tk.W)
        
        self.user_edit_label = tk.Label(self.view_window,text='Enter Username to edit:',font=("Arial",12), bg=self.bg_color, fg=self.fg_color)
        self.user_edit_label.grid(row=2,column=0,padx=2,sticky=tk.E)
        
        self.user_edit_entry = tk.Entry(self.view_window,font=("Arial", 12), bg=self.bg_color, fg=self.fg_color)
        self.user_edit_entry.grid(row=2,column=1,columnspan=2,pady=5,padx=2,sticky=tk.W)
        # Center the listboxes
        self.view_window.grid_columnconfigure(0, weight=1)
        self.view_window.grid_columnconfigure(1, weight=1)
        self.view_window.grid_rowconfigure(0, weight=1)
        
        
        
        
    def edit_password(self, username, password):
        """Function to edit the password of a user."""
        try:
            self.enty = self.edit_password_entry.get()
            if self.enty:
                cursor = self.connection.cursor()
                cursor.execute("UPDATE users SET password = (:password) WHERE username = (:name)",{"password":password,"name":username})
                self.connection.commit()
                self.update_view_window()
                showinfo("Success", "Password updated successfully")
                self.view_window.destroy()
            else:
                raise ValueError
        except ValueError:
            showinfo("error","please input an entry!")
            self.view_window.destroy()
        
    def delete_user(self, username):
        """Function to delete a user from the database."""
        try:
            if username:
                cursor = self.connection.cursor()
                cursor.execute("DELETE FROM users WHERE username = (:name)",{"name":username})
                self.connection.commit()
                self.update_view_window()
                showinfo("Success", "User deleted successfully")
                self.view_window.destroy()
            else:
                raise ValueError
        except:
            showinfo("error","please input an entry!")
            self.view_window.destroy
        
    def copy_password(self):
        #function for copyinh the password generated
        if self.result != "":
            pyperclip.copy(self.result)
            showinfo("Success", "Text has been copied to the clipboard.")
            self.passgen_window.destroy()
        else: 
            showinfo("error","please input an entry")
            
    def close_window_passgen(self):
        #closes window of passgen
        self.passgen_window.destroy()
            
    def password_generator_tab(self):
        """Function to display the password generator tab."""
        #setting window
        self.passgen_window = tk.Toplevel(self.root)
        self.passgen_window.title('PASS LOCK')
        width = 500
        height = 600
        #centers the screen 
        winx = (int(self.passgen_window.winfo_screenwidth() / 2)) - int(width / 2)
        winy = (int(self.passgen_window.winfo_screenheight() / 2)) - int(height / 2)
        self.passgen_window.geometry("{}x{}+{}+{}".format(width, height, winx, winy))
        self.passgen_window.resizable(True, True)
        self.passgen_window.config(bg=self.bgframe_color)
        #setting window frame
        self.frame4 = tk.Frame(self.passgen_window, bg=self.bgframe_color)
        self.frame4.pack(pady=10, anchor='center')
        #setting window label
        self.passin = tk.StringVar()
        self.passgen = tk.Label(self.frame4 , text="Password Generator", font=("Arial", 14), bg=self.bg_color, fg=self.fg_color, width=50)
        self.passgen.pack(pady=10, anchor=tk.CENTER)
        self.passen = tk.Entry(self.frame4 , textvariable=self.passin, font=("Arial", 14), bg=self.bg_color, fg=self.fg_color)
        self.passen.focus()
        self.passen.pack(pady=10, anchor=tk.CENTER)
        
        self.passgen_label = tk.Label(self.frame4 , text="Press Enter then press copy", bg=self.bg_color, fg=self.fg_color, font=("Arial", 10), width=90, height=1)
        self.passgen_label.pack()
        self.passen.bind('<Return>', self.password_generator)
        
        self.copy_button = tk.Button(self.frame4 , text="Copy", command= self.copy_password, bg=self.bg_color, fg=self.fg_color, font=("Arial", 14), width=20, height=2)
        self.copy_button.pack(pady=10)
        self.result = ""
        
        self.backbutton = tk.Button(self.frame4,text="back",command=self.close_window_passgen, bg=self.bg_color, fg=self.fg_color, font=("Arial", 14), width=20, height=2)
        self.backbutton.pack(side="bottom")
    def password_generator(self,event):
        #function for giving a password with more strength
        me = self.passin.get()
        words = me.split()
        for i in range(len(words)):
            modified_word = ""
            for letter in words[i]:
                if random.random() < 0.5:
                    modified_word += letter.lower()
                else:
                    modified_word += letter.upper()
            if random.random() < 0.5:
                modified_word += str(random.randint(0, 9))
            words[i] = modified_word
        self.result = " ".join(words)
        modified_text = tk.Label(self.frame4, font=("Arial", 14), background="#120410",fg="white")
        modified_text.config(text='result:' + self.result)
        modified_text.pack(pady=10, anchor=tk.CENTER)
        
        
if __name__ == "__main__":
    user_system = UserManagementSystem()
    user_system.root.mainloop()

