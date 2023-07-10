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

#color strip 1
colors=Canvas(frame,bg="#fff",width=150,height=265,bd=0)
colors.place(x=20,y=90)

id1 = colors.create_rectangle((10,10,50,50), fill="#b8255f")
id2 = colors.create_rectangle((10,50,50,100), fill="#db4035")
id3 = colors.create_rectangle((10,100,50,150), fill="#ff9933")
id4 = colors.create_rectangle((10,150,50,200), fill="#fad000")
id5 = colors.create_rectangle((10,200,50,250), fill="#afb83b")



hex1=Label(colors,text="#b8255f", fg="#000", font="arial 12 bold", bg="white")
hex1.place(x=60,y=15)

hex2=Label(colors,text="#db4035", fg="#000", font="arial 12 bold", bg="white")
hex2.place(x=60,y=65)

hex3=Label(colors,text="#ff9933", fg="#000", font="arial 12 bold", bg="white")
hex3.place(x=60,y=115)

hex4=Label(colors,text="#fad000", fg="#000", font="arial 12 bold", bg="white")
hex4.place(x=60,y=165)

hex5=Label(colors,text="#afb83b", fg="#000", font="arial 12 bold", bg="white")
hex5.place(x=60,y=215)


root.mainloop()