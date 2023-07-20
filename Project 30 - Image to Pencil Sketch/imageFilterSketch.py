# Import packages
from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk

# Black and white colours 

co0 = "#ffffff"
co1 = "#000000"
co2 = "#63b9ff"

window = Tk()
window.title("Sketch")
window.geometry("300x356")
window.config(bg=co0)
window.resizable(width=False,height=False)

style = ttk.Style(window)
style.theme_use("clam")

app_img = Image.open("Project 30 - Image to Pencil Sketch\imagePencil.png")
app_img = app_img.resize((50,50))
app_img =ImageTk.PhotoImage(app_img)

app_logo = Label(window,image=app_img,text="Image to Pencil", width=300, compound=LEFT, relief=RAISED, anchor=NW, font=("System 15 bold"), bg=co0, fg=co1)
app_logo.place(x=0, y=0)

l_options = Label(window, text="Setting----------------------------------------------------------".upper(), anchor=NW, font=("Verdana 7 bold"), bg=co0, fg=co1)
l_options.place(x=10, y=260)


window.mainloop()
