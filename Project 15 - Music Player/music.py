# import packages

from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os

root=Tk()
root.title("Music Magic")
root.geometry("920x670+290+85")
root.configure(bg="#0f1a2b")
root.resizable(False,False)

mixer.init()

#icon
image_icon = PhotoImage(file="Project 15 - Music Player/logo.png")
root.iconphoto(False,image_icon)

Top=PhotoImage(file="Project 15 - Music Player\top1.jpg")
Label(root,image=Top,bg="#0f1a2b").pack()


#logo
Logo=PhotoImage(file="Project 15 - Music Player/logo.png")
Label(root,image=Logo,bg="#0f1a2b").place(x=65,y=115)

root.mainloop()