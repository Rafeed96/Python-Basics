# Import packages
from tkinter import *
from datetime import date

# Set GUI window

root=Tk()
root.geometry("800x600")
root.resizable(False,False)
root.title("Age Calculator")

photo=PhotoImage(file="Project 12 - Age Calculator\AgeCalculator.png")
myimage=Label(image=photo)
myimage.pack(padx=15,pady=15)

Label(text="Name",font=23).place(x=200,y=250)
Label(text="Year",font=23).place(x=200,y=300)
Label(text="Month",font=23).place(x=200,y=350)
Label(text="Day",font=23).place(x=200,y=400)

nameValue = StringVar()
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()

nameEn

root.mainloop()