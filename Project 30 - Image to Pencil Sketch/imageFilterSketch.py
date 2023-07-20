# Import packages
from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk
from tkinter import filedialog as fd

# Black and white colours 

co0 = "#ffffff"
co1 = "#000000"
co2 = "#63b9ff"

window = Tk()
window.title("Sketch")
window.geometry("300x356")
window.config(bg=co0)
window.resizable(width=False,height=False)

global original_img, l_img, img

def choose_img():
    global original_img, l_img, img 

    img = fd.askopenfilename()



style = ttk.Style(window)
style.theme_use("clam")

app_img = Image.open("Project 30 - Image to Pencil Sketch\imagePencil.png")
app_img = app_img.resize((50,50))
app_img =ImageTk.PhotoImage(app_img)

app_logo = Label(window,image=app_img,text="Image to Pencil", width=300, compound=LEFT, relief=RAISED, anchor=NW, font=("System 15 bold"), bg=co0, fg=co1)
app_logo.place(x=0, y=0)

l_options = Label(window, text="Setting----------------------------------------------------------".upper(), anchor=NW, font=("Verdana 7 bold"), bg=co0, fg=co1)
l_options.place(x=10, y=260)


scale = Scale(window, from_=0, to=255, length=120, bg=co0, fg="red", orient=HORIZONTAL)
scale.place(x=10, y=300)

b_choose = Button(window, text="Choose img", width=15, overrelief=RIDGE, font=("Ivy 10"), bg=co2, fg=co1)
b_choose.place(x=147, y=287)

b_save = Button(window, text="Save img", width=15, overrelief=RIDGE, font=("Ivy 10"), bg=co2, fg=co1)
b_save.place(x=147, y=317)

window.mainloop()
