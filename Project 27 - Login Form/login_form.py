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

frame =Frame(root,width=350,height=350,bg="red")
frame.place(x=480,y=70)


root.mainloop()