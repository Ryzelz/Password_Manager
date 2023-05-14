import customtkinter as ctk
from LoginWindow_V11 import Login

def main():
    root = ctk.CTk()
    root.title("PASS LOCK")
    
    # Set the window icon
    root.iconbitmap("Icon_pass.ico")

    width, height = 1280 , 720  
    #setting the window to center when launched (copy pasted)
    winx = (int(root.winfo_screenwidth() / 2)) - int(width / 2)
    winy = (int(root.winfo_screenheight() / 2)) - int(height / 2)
    root.geometry("{}x{}+{}+{}".format(width, height, winx, winy))

    root.resizable(False, False)
    
    #Initiating the System
    Login(root)

    root.mainloop()

if __name__ == '__main__':
    main()
