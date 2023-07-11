from tkinter import *

root = Tk()
root.title("Toggle Switch")
root.geometry("400x600")
root.config(bg="white")

on=PhotoImage(file="light.png")
off=PhotoImage(file="dark.png")

button=Button(root,image=on,bd=0,bg="white")
button.pack(padx=50,pady=50)

root.mainloop() 