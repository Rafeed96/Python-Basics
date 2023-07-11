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


def showimage():
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image File", filetypes=(("PNG file","*.png"),("JPG file","*.jpg"),("ALL file","*.txt")))

    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=310,height=270)
    lbl.image=img

def Findcolor():

    ct=ColorThief(filename)
    palette = ct.get_palette(color_count=11)

    



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





#color strip 1
colors2=Canvas(frame,bg="#fff",width=150,height=265,bd=0)
colors2.place(x=180,y=90)

id6 = colors2.create_rectangle((10,10,50,50), fill="#7ecc49")
id7 = colors2.create_rectangle((10,50,50,100), fill="#299438")
id8 = colors2.create_rectangle((10,100,50,150), fill="#6accbc")
id9 = colors2.create_rectangle((10,150,50,200), fill="#158fad")
id10 = colors2.create_rectangle((10,200,50,250), fill="#14aaf5")



hex6=Label(colors2,text="#7ecc49", fg="#000", font="arial 12 bold", bg="white")
hex6.place(x=60,y=15)

hex7=Label(colors2,text="#299438", fg="#000", font="arial 12 bold", bg="white")
hex7.place(x=60,y=65)

hex8=Label(colors2,text="#6accbc", fg="#000", font="arial 12 bold", bg="white")
hex8.place(x=60,y=115)

hex9=Label(colors2,text="#158fad", fg="#000", font="arial 12 bold", bg="white")
hex9.place(x=60,y=165)

hex10=Label(colors2,text="#14aaf5", fg="#000", font="arial 12 bold", bg="white")
hex10.place(x=60,y=215)


# selected image
selectimage = Frame(frame,width=340,height=350,bg="#d6dee5")
selectimage.place(x=350,y=10)

f=Frame(selectimage,bd=3,bg="black",width=320,height=280,relief=GROOVE)
f.place(x=10,y=10)

lbl = Label(f,bg="black")
lbl.place(x=0,y=0)

Button(selectimage,text="Select Image",width=12,height=1,font="arial 14 bold",command=showimage).place(x=10,y=300)
Button(selectimage,text="Find Colors",width=12,height=1,font="arial 14 bold",command=Findcolor).place(x=176,y=300)


root.mainloop()