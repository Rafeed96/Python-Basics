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

Label(root,font=("arial", 15, "bold"), text="Current Time:", bg="papaya whip").place(x=65, y=70)
            

root.mainloop()