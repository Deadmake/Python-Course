import customtkinter
import string
import random


#TKINTER SETTINGS ---------------------------------------------#
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
window = customtkinter.CTk()
#---------------------------------------------# 


# GUI SETTINGS ---------------------------------------------#
window.iconbitmap("pwgen.ico")
window.title("Password Generator")
window.geometry("500x500")
window.resizable(True, False)
#---------------------------------------------# 


# GENERATOR FUNCTION ---------------------------------------------#
def pwgen(size):
    chrachters = "" 
    
    if checkbox1.get() == 1:
        chrachters += string.ascii_uppercase
    if checkbox2.get() == 1:
        chrachters += string.ascii_lowercase
    if checkbox3.get() == 1:
        chrachters += string.digits
    if checkbox4.get() == 1:
        chrachters += "!§$%&/()=?#+'*_-"

    pas = "".join(
        random.choice(chrachters)
        for _ in range(size))
    
    label1 = customtkinter.CTkLabel(master=Frame, text=pas, font=("Montserrat", 16))
    label1.pack(pady=14, padx=10)

    def copy():
        window.clipboard_clear()  
        window.clipboard_append(pas)  
        window.update()
    
    copybtn = customtkinter.CTkButton(master=Frame, text="Copy to Clipboard", font=("Montserrat", 16), command=copy)
    copybtn.pack(pady=10, padx=10)
#---------------------------------------------# 


# GUI ---------------------------------------------#
Frame = customtkinter.CTkFrame(window)
Frame.pack(pady=20, padx=60, fill="both", expand=True)

Title = customtkinter.CTkLabel(master=Frame, text="Password Generator", font=("Montserrat", 20))
Title.pack(pady=14, padx=10)

entry1 = customtkinter.CTkEntry(master=Frame, placeholder_text="Choose Size?", font=("Montserrat", 14))
entry1.pack(pady=20, padx=10)

btn1 = customtkinter.CTkButton(master=Frame, text="Generate Password", font=("Montserrat", 16), command=lambda: pwgen(int(entry1.get())))
btn1.pack(pady=10, padx=10)
#---------------------------------------------#


#---------------------------------------------#
checkbox1 = customtkinter.CTkCheckBox(master=Frame, text="Uppercase", font=("Montserrat", 14), onvalue=1, offvalue=0)
checkbox1.pack(pady=10, padx=10)

checkbox2 = customtkinter.CTkCheckBox(master=Frame, text="Lowercase", font=("Montserrat", 14), onvalue=1, offvalue=0)
checkbox2.pack(pady=10, padx=10)

checkbox3 = customtkinter.CTkCheckBox(master=Frame, text="Numbers", font=("Montserrat", 14), onvalue=1, offvalue=0)
checkbox3.pack(pady=10, padx=10)

checkbox4 = customtkinter.CTkCheckBox(master=Frame, text="Characters", font=("Montserrat", 14), onvalue=1, offvalue=0)
checkbox4.pack(pady=10, padx=10)
#---------------------------------------------#

window.mainloop()