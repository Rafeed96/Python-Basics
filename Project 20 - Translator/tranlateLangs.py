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


root.mainloop()

