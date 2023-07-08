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



root.mainloop()