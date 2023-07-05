# Install packages pybase64

from tkinter import *
from tkinter import messagebox
import base64
import os

def main_screen():

    screen = Tk()
    screen.geometry("375x398")

    #icon
    image_icon = PhotoImage(file="ico.img")
    screen.iconphoto(False, image_icon)

    Label(text="Enter text for encryption and decryption", fg="black", font=("calibri",13)).place(x=10,y=10)

    screen.title("PctApp")

    screen.mainloop()

main_screen()


