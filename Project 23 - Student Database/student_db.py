# Install packages pathlib
# install packge openpyxl
# install packge xlrd
# install packge pillow

from tkinter import *
from datetime import date
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from tkinter.ttk import Combobox
import openpyxl, xlrd
from openpyxl import Workbook
import pathlib

backG = "#06283D"
framBG = "#EDEDED"
framFG = "#06283D"

root=Tk()
root.title("Student Registration")
root.geometry("1250x7700+210+100")
root.configure(bg="#06283D")

file=pathlib.Path("Student_Data.xlsx")

if file.exists():
    pass
else:
    file=Workbook()
    sheet=file.active
    sheet["A1"]="Registration Np."
    sheet["B1"]="Name"
    sheet["C1"]="Class"
    sheet["D1"]="Gender"
    sheet["E1"]="DOB"
    sheet["F1"]="Date of Registration"
    sheet["G1"]="Religion"
    sheet["H1"]="Skill"
    sheet["I1"]="Father's Name"
    sheet["J1"]="Mother's Name"
    sheet["K1"]="Father's Occupation"
    sheet["L1"]="Mother's Occupation"

    file.save("Student_Data.xlsx")

# Upper Frame
Label(root,text="Email: homepc@gmail.com",width=10,height=3,bg="#f0687c",anchor='e').pack(side=TOP,fill=X)
Label(root,text="STUDENT REGISTRATION",width=10,height=2,bg="#c36464",fg="#fff",font="arial 20 bold").pack(side=TOP,fill=X)


# Search box
Search=StringVar()
Entry(root,textvariable=Search,width=15,bd=2,font="arial 20").place(x=820,y=70)
imageicon3=PhotoImage(file="Project 23 - Student Database\images (1).png")
Srch=Button(root,text="Search",compound=LEFT,image=imageicon3,width=123,bg="#68ddfa",font="arial 13 bold")
Srch.place(x=1060,y=66)

imageicon4=PhotoImage(file="Project 23 - Student Database\imageupdate1.png")
Update_button=Button(root,image=imageicon4,bg="#c36464")
Update_button.place(x=110,y=64)


root.mainloop()
