# install packages
from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Login")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False,False)

img = PhotoImage("Project 27 - Login Form\vecteezy_cloud-computing-modern-flat-concept-for-web-banner-design_5879539.jpg")
Label(root,image=img,bg="red").place(x=50,y=50)

frame =Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading =Label(frame,text="Sign In",fg="#57a1f8",bg="white",font=("Microsoft Yahei UI Light",23,"bold"))
heading.place(x=100,y=5)

user = Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft Yahei UI Light",11))
user.place(x=30,y=80)
user.insert(0,"Username")


root.mainloop()