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

root.mainloop()