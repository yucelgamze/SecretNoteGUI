from tkinter import *
import pybase64
from PIL import Image, ImageTk
from  tkinter import messagebox

FONT = ("didot",20,"bold")

#Encryption
def encryption():
    text = text_input.get("1.0", END)
    ciphter_text = ""
    text_input.delete("1.0", END)
    password_input.delete("1.0",END)
    
    if password_input.get() == "1234":
        
        text = text.encode("ascii")
        text = pybase64.b64encode(text)
        ciphter_text = text.decode("ascii")
        
        encryption_file = open("secret.txt", mode='w')
        encryption_file.write(ciphter_text) 
        encryption_file.close()     
        
    else:
        
        messagebox.showwarning("Invalid Value!", "Incorrect Password, Please Try Again!")
    

#Decryption
def decryption():
    ciphter_text = text_input.get("1.0", END)
    text = ""
    text_input.delete("1.0", END)
    password_input.delete("1.0", END)
    
    if password_input.get() == "1234":
        
        ciphter_text = ciphter_text.encode("ascii")
        ciphter_text = pybase64.b64decode(ciphter_text)
        text = ciphter_text.decode("ascii")
        
        decryption_file = open("message.txt", mode='w')
        decryption_file.write(text)
        decryption_file.close()
        
    else:
        
        messagebox.showwarning("Invalid Value!", "Incorrect Password, Please Try Again!")

def clear():
    text_input.delete(1.0, END)
    password_input.delete(0, END)

window =Tk()
window.geometry("700x800")
window.title("🔐Encryption Decryption Secret Note GUI🔐")
window.config(background="#02b9bf")

frame = Frame(window)
frame.pack(pady=20)

text_label = Label(text="Please enter your message to encrypt/decrypt: ", font=FONT)
text_label.config(fg="#DEFE28", bg='#09035e')
text_label.pack(side="top")


text_input = Text(font=FONT, width=30, height=15)
text_input.config(fg="#09035e")
text_input.pack(pady=10)

encryption_button = Button(frame, text="Encryption", font=FONT, command=encryption, fg='#09035e', highlightbackground='#faa5d4')
encryption_button.grid(row=0, column=1)

decryption_button = Button(frame, text="Decryption", font=FONT, command=decryption, fg='#09035e', highlightbackground='#faa5d4')
decryption_button.grid(row=0, column=2)

clear_button = Button(frame, text="Clear", font=FONT, command=clear, fg='#09035e', highlightbackground='#faa5d4')
clear_button.grid(row=0, column=3)

password_label = Label(text="Enter your password:", font=FONT, fg="#DEFE28", bg='#09035e')
password_label.pack(pady=10)

password_input = Entry(font=FONT, width=30, show="*")
password_input.pack(pady=10)


image = Image.open("output3.png")
image_resized = image.resize((150,150))

img = ImageTk.PhotoImage(image_resized)
img_label = Label(image=img, bg="#02b9bf")
img_label.pack(pady=10)

window.mainloop()