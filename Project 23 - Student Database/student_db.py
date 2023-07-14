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

root.mainloop()