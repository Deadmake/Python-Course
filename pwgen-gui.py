import customtkinter
import string
import random

customtkinter.set_appearance_mode("dark") 
customtkinter.set_default_color_theme("dark-blue")
self = customtkinter.CTk()

self.title("Password Generator")
self.geometry("500x500")
self.iconbitmap("pwgen.ico")

def pwgen(sizei):
    charachters = "!§$%&/()=?#+'*_-"
    sizei = int(entry1.get())
    pas = "".join(
        random.choice(charachters + string.ascii_uppercase + string.ascii_lowercase + string.digits)
        for _ in range(sizei)) 
    label1 = customtkinter.CTkLabel(master=frame, text=pas, font=("Montserrat", 12))
    label1.pack(pady=12, padx=10)

    def copy():
        self.clipboard_clear()  
        self.clipboard_append(pas)  
        self.update()  

    btn2 = customtkinter.CTkButton(master=frame, text="Copy to Clipboard", font=("Montserrat", 12), command=copy)
    btn2.pack(pady=10, padx=10)

frame = customtkinter.CTkFrame(self)
frame.pack(pady=20, padx=40, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Password Generator", font=("Montserrat", 16))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Size of Password?", font=("Montserrat", 12) )
entry1.pack(pady=20, padx=10)

btn1 = customtkinter.CTkButton(master=frame, text="Generate Password", font=("Montserrat", 12), command=lambda: pwgen(sizei=int(entry1.get())))
btn1.pack(pady=10, padx=10)

self.mainloop()
