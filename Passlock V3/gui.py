import tkinter as tk
from tkinter import ttk
import random
import pyperclip
import tkinter.messagebox as mbox


class PasswordGeneratorApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Password Generator')
        self.window.config(bg='blue')
        self.windoww = 500
        self.windowh = 500
        self.scw = self.window.winfo_screenwidth()
        self.sch = self.window.winfo_screenheight()
        self.cx = (self.scw // 2 - self.windoww // 2)
        self.cy = (self.sch // 2 - self.windowh // 2)
        self.window.geometry(f'{self.windoww}x{self.windowh}+{self.cx}+{self.cy}')
        self.passin = tk.StringVar()
        self.passgen = tk.Label(self.window, name="password generator", font=('Bold', 10), bg='blue', fg='#FFFFFF')
        self.passgen.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        self.passen = tk.Entry(self.window, textvariable=self.passin)
        self.passen.focus()
        self.passen.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
        self.passen.bind('<Return>', self.generate_password)
        self.copy_button = ttk.Button(self.window, text="Copy", command=self.copy_password)
        self.copy_button.pack(pady=10)
        self.result = ""
        
    def generate_password(self, event=None):
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
        modified_text = ttk.Label(self.window)
        modified_text.config(text=self.result)
        modified_text.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        
    def copy_password(self):
        if self.result:
            pyperclip.copy(self.result)
            mbox.showinfo("Success", "Text has been copied to the clipboard.")
        
    def run(self):
        self.window.mainloop()

app = PasswordGeneratorApp()
app.run()