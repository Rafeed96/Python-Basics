# import packages
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from colorthief import ColorThief
import os

root = Tk()
root.title("Color picker from image")
root.geometry("800x470+100+100")
root.configure(bg="#e4e8eb")
root.resizable(False,False)

#icon 
#image_icon = PhotoImage(file="")
#root.iconphoto(False,image_icon)

Label(root,width=120,height=10,bg="#4272f9").pack()

#frame
frame = Frame(root,width=700,height=370,bg="#fff")
frame.place(x=50,y=50)

logo=PhotoImage(file="")
Label(frame,image=logo,bg="#fff").place(x=10,y=10)

Label(frame,text="Color Finder", font="arial 25 bold", bg="white").place(x=100,y=20)

#color
colors=Canvas(frame,bg="#fff",width=150,height=265,bd=0)
colors.place(x=20,y=90)

id1 = colors.create_rectangle((10,10,50,50), fill="#b8255f")

hex1=Label(colors,text="#b8255f", fg="#000", font="arial 12 bold", bg="white")
hex1.place(x=60,y=15)


root.mainloop()