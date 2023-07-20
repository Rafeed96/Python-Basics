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

app_logo = Label(window,image=app_img,text="Image to Pencil")


window.mainloop()
