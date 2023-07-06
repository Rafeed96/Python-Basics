# Install playsound package

from tkinter import *
from playsound import playsound
import time

root=Tk()
root.title("Time Countdown")
root.geometry("400x600")
root.config(bg="#000")
root.resizable(False,False)

heading = Label(root,text="Timer", font="arial 30 bold", bg="#000", fg="#ea3548")
heading.pack(pady=10)

# The Clock Time
Label(root,font=("arial", 15, "bold"), text="Current Time:", bg="papaya whip").place(x=65, y=70)
            
def clock()            :
    clock_time = time.strftime('%H:%M:%S %p')
    current_time.config(text=clock_time)
    current_time.after(1000,clock)

current_time = Label(root,font=("arial", 15, "bold"), text="", fg="#000",bg="#fff")
current_time.place(x=190, y=70)
clock()


# Timer
hrs=StringVar()
Entry(root,textvariable=hrs,width=2,font="arial 50").place(x=30, y=155)
hrs.set("00")

mins=StringVar()
Entry(root,textvariable=mins,width=2,font="arial 50").place(x=150, y=155)
mins.set("00")

sec=StringVar()
Entry(root,textvariable=sec,width=2,font="arial 50").place(x=270, y=155)
sec.set("00")


root.mainloop()