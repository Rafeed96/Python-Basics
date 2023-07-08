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
image_icon=PhotoImage(file="Project 13 - BMI Calculator\--bmi.jpg")
root.iconphoto(False,image_icon)

# Top

top= PhotoImage(file="Project 13 - BMI Calculator\top.png")
top_image=Label(root,image=top,background="#f0f1f5")
top_image.place(x=-10, y=-10)            

# Bottom Box
Label(root,width=72,height=18,bg="lightblue").pack(side=BOTTOM)

# TWO Boxes
box = PhotoImage(file="Project 13 - BMI Calculator\box.png")
Label(root,image=box).place(x=20,y=100)
Label(root,image=box).place(x=240,y=100)

# Scale
scale = PhotoImage(file="Project 13 - BMI Calculator\scale.png")
Label(root,image=scale).place(x=20,y=310)
Label(root,image=box).place(x=240,y=100)



root.mainloop()
