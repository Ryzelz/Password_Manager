import tkinter as tk
from tkinter import ttk
import random
import pyperclip
import tkinter.messagebox as mbox


def passwordgenerator(event):
   me = passin.get()
        # split text into words
   words = me.split()
        
        # loop through each word and modify it
   for i in range(len(words)):
            # randomly capitalize letters
            modified_word = ""
            for letter in words[i]:
                if random.random() < 0.5:
                    modified_word += letter.lower()
                else:
                    modified_word += letter.upper()
            
            # randomly add numbers to the end of the word
            if random.random() < 0.5:
                modified_word += str(random.randint(0, 9))
            
            words[i] = modified_word
        
        # join the modified words back into a text
            modified_text = ttk.Label(window)
            global result
            result = " ".join(words)
            modified_text.config(text=result)
            modified_text.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
def copy_text():
        # Get the text from the textbox
        text = result
        # Copy the text to the clipboard
        pyperclip.copy(text)
        mbox.showinfo("Success", "Text has been copied to the clipboard.")            
#setting up window size
window = tk.Tk()
window.title('Password Generator')
window.config(bg='blue')
windoww = 500
windowh = 500
scw = window.winfo_screenwidth()
sch = window.winfo_screenheight()
cx = (scw//2 - windoww//2)
cy = (sch//2 - windowh//2)
window.geometry(f'{windoww}x{windowh}+{cx}+{cy}')
passin = tk.StringVar()
#setting up for window labels
passgen = tk.Label(window, name="password generator", font=('Bold', 10), bg = 'blue',fg='#FFFFFF')
passgen.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
passen = tk.Entry(window, textvariable = passin )
passen.focus()
passen.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
passen.bind('<Return>', passwordgenerator)
copy_button = ttk.Button(window, text="Copy", command=copy_text)
copy_button.pack(pady=10)
window.mainloop()
