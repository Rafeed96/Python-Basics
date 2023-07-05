# Install Packages

import tkinter as tk
from tkinter import *
import pyttsx3

root = Tk()

textv = StringVar()

obj = LabelFrame(root,text="Text To Speech", font=20, bd=1)
obj.pack(fill="both", expand="yes", padx=10, pady=10)

lbl = Label(obj, text="Text", font=30)
lbl.pack(side=tk.LEFT, padx=5)

text=Entry(obj,textvariable=textv, font=30, width=25, bd=5)
text.pack(side=tk.LEFT,padx=10)


root.title("Text To Speech")
root.geometry("400x200")
root.resizable(False,False)
root.mainloop()