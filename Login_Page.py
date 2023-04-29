from PIL import Image, ImageTk
import tkinter as tk
from tkinter import *
from crudguiact import UserManagementSystem
from tkinter.messagebox import showinfo

#DAlena
class LoginSystem:
    def __init__(self):
        self.main = tk.Tk()
        self.main.title("PASSLOCK")
        width = 400
        height = 600

        self.winx = (int(self.main.winfo_screenwidth() / 2)) - int(width / 2)
        self.winy = (int(self.main.winfo_screenheight() / 2)) - int(height / 2)
        self.main.geometry("{}x{}+{}+{}".format(width, height, self.winx, self.winy))
        self.main.resizable(True, True)
        self.main.config(bg="#620054", borderwidth=0, relief='solid', highlightthickness=0, bd=0)
        self.main.resizable(False, False)
        #image logo
        self.bg_image = ImageTk.PhotoImage(file="logoimg.png")
        self.canvas = tk.Canvas(self.main, width=250, height=250, highlightthickness=0)
        self.canvas.pack(anchor="center")
        imgcanvas= self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
        
        
        self.username_label = Label(self.main, text="Username:", background="#8D047A", foreground="white")
        self.username_label.config(font=("Arial", 15), width=50)
        self.username_label.pack()
        self.username_entry = Entry(self.main,background="#8D047A", foreground="white" )
        self.username_entry.pack(pady=5)

        self.password_label = Label(self.main, text="Password:", background="#8D047A", foreground="white")
        self.password_label.config(font=("Arial", 15), width=50)
        self.password_label.pack()
        self.password_entry = Entry(self.main, show="*", background="#8D047A", foreground="white")
        self.password_entry.pack()

        self.login_button = Button(self.main, text="Login", command=self.login, background="#8D047A", foreground="white", borderwidth=1, relief="sunken")
        self.login_button.config(font=("Arial", 10), width=14, height=1)
        self.login_button.pack(pady=5)


        self.accounts = {"admin": "admin", "user": "user"}

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in self.accounts and self.accounts[username] == password:
            showinfo(title='Login', message='Login Successful!')
            self.call_main = UserManagementSystem()
            self.destroy()
        else:
            showinfo(title='Login', message='Login Error! Invalid username or password')
            
    def run(self):
        """Function to start the GUI application."""
        self.main.mainloop()

if __name__ == "__main__":
    app = LoginSystem()
    app.run()
