import tkinter as tk

class CopyText(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.withdraw()
        self.clipboard_clear()

    def copy_data(self, data):
        self.clipboard_append(data)
        self.update()
        self.deiconify()
        self.after(5000, self.withdraw)
        self.after(5000, self.clipboard_clear)
