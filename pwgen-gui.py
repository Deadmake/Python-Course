import customtkinter
import string
import random


# TKINTER SETTINGS
customtkinter.set_appearance_mode("dark") 
customtkinter.set_default_color_theme("dark-blue")
self = customtkinter.CTk()


# GUI SETTINGS
self.title("Password Generator")
self.geometry("500x500")
self.resizable(False, False)
self.iconbitmap("pwgen.ico")


# GENERATOR FUNCTION
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


    copybtn = customtkinter.CTkButton(master=frame, text="Copy to Clipboard", font=("Montserrat", 12), command=copy)
    copybtn.pack(pady=10, padx=10)


# GUI
frame = customtkinter.CTkFrame(self)
frame.pack(pady=20, padx=40, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Password Generator", font=("Montserrat", 16))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Size of Password?", font=("Montserrat", 12) )
entry1.pack(pady=20, padx=10)

generatebtn = customtkinter.CTkButton(master=frame, text="Generate Password", font=("Montserrat", 12), command=lambda: pwgen(sizei=int(entry1.get())))
generatebtn.pack(pady=10, padx=10)


checkbox1 = customtkinter.CTkCheckBox(master=frame, text="Uppercase", font=("Montserrat", 12), onvalue=1, offvalue=0)
checkbox1.pack(pady=10, padx=10)

checkbox2 = customtkinter.CTkCheckBox(master=frame, text="Lowercase", font=("Montserrat", 12))
checkbox2.pack(pady=10, padx=10)

checkbox3 = customtkinter.CTkCheckBox(master=frame, text="Numbers", font=("Montserrat", 12))
checkbox3.pack(pady=10, padx=10)

checkbox4 = customtkinter.CTkCheckBox(master=frame, text="Characters", font=("Montserrat", 12))
checkbox4.pack(pady=10, padx=10)




self.mainloop()
