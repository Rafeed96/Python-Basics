# Import packages for gui

from tkinter import *
from tkinter import messagebox
import ast

window=Tk()
window.title("Sign Up")
window.geometry("925x500+300+200")
window.configure(bg="#fff")
window.resizable(False,False)

img = PhotoImage(file='Project 28 - Sign Up Form\login.png')
Label(window,image=img,border=0,bg="white").place(x=50,y=90)

frame =Frame(window,width=350,height=390,bg="#fff")
frame.place(x=480,y=50)

heading =Label(frame,text="Sign In",fg="#57a1f8",bg="white",font=("Microsoft Yahei UI Light",23,"bold"))
heading.place(x=100,y=5)


# User
def on_enter(e):
    user.delete(0, "end")
def on_leave(e):
    if user.get()=="":
        user.insert(0, "Username")

user = Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft Yahei UI light", 11))
user.place(x=30,y=80)
user.insert(0,"Username")
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)

# Password
def on_enter(e):
    code.delete(0, "end")
def on_leave(e):
    if code.get()=="":
        code.insert(0, "Password")

code = Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft Yahei UI light", 11))
code.place(x=30,y=150)
code.insert(0,"Password")
code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)


window.mainloop()