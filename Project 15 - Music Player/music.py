# import packages

from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os

root=Tk()
root.title("Music Magic")
root.geometry("920x670+290+85")
root.configure(bg="#0f1a2b")
root.resizable(False,False)

mixer.init()

#icon
image_icon = PhotoImage(file="Project 15 - Music Player/logo.png")
root.iconphoto(False,image_icon)

Top=PhotoImage(file="Project 15 - Music Player\top1.jpg")
Label(root,image=Top,bg="#0f1a2b").pack()


#logo
Logo=PhotoImage(file="Project 15 - Music Player/logo.png")
Label(root,image=Logo,bg="#0f1a2b").place(x=65,y=115)


#button\
play_button = PhotoImage(file="Project 15 - Music Player\play.png")
Button(root,image=play_button,bg="#0f1a2b",bd=0).place(x=100,y=400)

stop_button = PhotoImage(file="Project 15 - Music Player\stop.png")
Button(root,image=stop_button,bg="#0f1a2b",bd=0).place(x=30,y=500)

resume_button = PhotoImage(file="Project 15 - Music Player\resume.png")
Button(root,image=resume_button,bg="#0f1a2b",bd=0).place(x=115,y=500)

pause_button = PhotoImage(file="Project 15 - Music Player\pause.png")
Button(root,image=pause_button,bg="#0f1a2b",bd=0).place(x=200,y=500)


#music
Menu=PhotoImage(file="")
Label(root,image=Menu,bg="#0f1a2b").pack(padx=10,pady=50,side=RIGHT)

music_frame = Frame(root,bd=2,relief=RIDGE)
music_frame.place(x=330,y=350,width=560,height=250)


root.mainloop()