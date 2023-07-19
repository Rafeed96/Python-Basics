from tkinter import *

clock = Tk()
clock.title("Digital Clock")
clock.geometry("1000x500")
clock.config(bg="lightyellow")

label_hr=Label(clock,text="00", font=("times New Roman",60,"bold"),bg="black",fg="white")
label_hr.place(x=120,y=40,height=110,width=100)

label_min=Label(clock,text="00", font=("times New Roman",60,"bold"),bg="black",fg="white")
label_min.place(x=340,y=40,height=110,width=100)

clock.mainloop()