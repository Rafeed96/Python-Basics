from tkinter import *

root = Tk()
root.title("Toggle Switch")
root.geometry("400x600")
root.config(bg="white")

on=PhotoImage(file="Project 19 - Light And Dark Toggle\light2.png")
off=PhotoImage(file="Project 19 - Light And Dark Toggle\dark2.png")

button=Button(root,image=on,bd=0,bg="white")
button.pack(padx=50,pady=50)

root.mainloop() 