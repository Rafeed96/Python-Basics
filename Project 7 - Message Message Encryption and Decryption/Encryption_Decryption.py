# Install packages pybase64

from tkinter import *
from tkinter import messagebox
import base64
import os

def main_screen():

    screen = Tk()
    screen.geometry("375x398")

    #icon
    image_icon = PhotoImage(file="E:\Projects\Repositories\Python\Python-Basics\Project 7 - Message Message Encryption and Decryption\ico.jpg")
    screen.iconphoto(False, image_icon)

    Label(text="Enter text for encryption and decryption", fg="black", font=("calibri",13)).place(x=10,y=10)
    text1 = Text(font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD.bd=0)
    text1.place(x=10,y=50,width=355,height=100)

    screen.title("PctApp")

    screen.mainloop()

main_screen()


