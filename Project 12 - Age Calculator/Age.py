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


root.mainloop()