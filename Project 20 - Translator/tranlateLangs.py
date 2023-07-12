#import packages

from tkinter import *
from tkinter import ttk,messagebox
import googletrans
import textblob 

root=Tk()
root.title("Translator")
root.geometry("1000x400")
root.configure(bg="white")

language=googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

combo1=ttk.Combobox(root,values=languageV,font="Roboto 14", state="r")
combo1.place(x=110,y=20)
combo1.set("English")

label1 = Label(root,text="English",font="segeo 30 bold", bg="white", width=18,bd=5,relief=GROOVE)
label1.place(x=10,y=50)

f=Frame(root,bg="Black",bd=5)
f.place(x=10,y=118,width=440,height=210)

text1=Text(f,font="Roboto 20", bg="white", relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=430,height=200)


combo2=ttk.Combobox(root,values=languageV,font="Roboto 14", state="r")
combo2.place(x=730,y=20)
combo2.set("Select Language")

label2 = Label(root,text="English",font="segeo 30 bold", bg="white", width=18,bd=5,relief=GROOVE)
label2.place(x=620,y=50)

root.mainloop()

