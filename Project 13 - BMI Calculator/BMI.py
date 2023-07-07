# Import packages

from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


# Create BMI window

root=Tk()
root.title("BMI Calculator")
root.geometry("470x580+300+200")
root.resizable(False,False)
root.configure(bg="#f0f1f5")

# icon
image_icon=PhotoImage(file="")
root.iconphoto(False,image_icon)

# Top

top= PhotoImage(file="")
top_image=Label(root,image=top,background="#f0f1f5")
top_image.place(x=-10, y=-10)            


root.mainloop()
