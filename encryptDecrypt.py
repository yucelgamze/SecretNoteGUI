import random
import string
from tkinter import *

#global variables
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

key = chars.copy()
random.shuffle(key)

FONT = ("didot",15,"bold")


#Encryption
def encryption():
    text = text_input.get()
    ciphter_text = ""

    for character in text:
        i = chars.index(character)
        ciphter_text += key[i]
    
    encryption_file = open("secret.txt",mode='w')
    encryption_file.write(ciphter_text) 
    encryption_file.close()     
    

#Decryption
def decryption():
    ciphter_text = ciphter_text_input.get()
    text = ""

    for character in ciphter_text:
        i = key.index(character)
        text += chars[i]
    
    decryption_file = open("message.txt",mode='w')
    decryption_file.write(text)
    

window =Tk()
window.geometry("400x200")
window.title("🔐Encryption Decryption Secret Note GUI🔐")
window.config(background="#FF1C86")

text_label = Label(text="Please enter your message to encrypt: ", font=FONT)
text_label.config(background="dark blue",fg="#DEFE28")
text_label.pack(side="top")


text_input = Entry(textvariable=Text, font=FONT,width=20)
text_input.config(background="dark blue",fg="#C7FC00")
text_input.pack(side="top")

encryption_button = Button(text="Encryption",font=FONT,command=encryption,highlightbackground='#FA006E')
encryption_button.pack(side="top")

ciphter_text_label = Label(text="Please enter your message to decrypt: ", font=FONT)
ciphter_text_label.config(background="dark blue",fg="#DEFE28")
ciphter_text_label.pack(side="top")

ciphter_text_input = Entry(textvariable=Text, font=FONT,width=20)
ciphter_text_input.config(background="dark blue",fg="#DEFE28")
ciphter_text_input.pack(side="top")


decryption_button = Button(text="Decryption",font=FONT,command=decryption,highlightbackground='#FA006E')
decryption_button.pack(side="top")

window.mainloop()