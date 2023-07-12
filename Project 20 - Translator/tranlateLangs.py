#import packages

from tkinter import *
from tkinter import ttk,messagebox
import googletrans
import textblob 

root=Tk()
root.title("Translator")
root.geometry("1000x400")
root.configure(bg="white")

def label_change():
    c=combo1.get()
    c1=combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000,label_change)


#arrow
arrow_image=PhotoImage(file="Project 20 - Translator\images.png")
image_label=Label(root,image=arrow_image,width=90)
image_label.place(x=455,y=50)

language=googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

combo1=ttk.Combobox(root,values=languageV,font="Roboto 14", state="r")
combo1.place(x=110,y=20)
combo1.set("English")

label1 = Label(root,text="Select Language",font="segeo 30 bold", bg="white", width=18,bd=5,relief=GROOVE)
label1.place(x=10,y=50)

f=Frame(root,bg="Black",bd=5)
f.place(x=10,y=118,width=440,height=210)

text1=Text(f,font="Roboto 20", bg="white", relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=430,height=200)

scrollbar1=Scrollbar(f)
scrollbar1.pack(side="right", fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)



combo2=ttk.Combobox(root,values=languageV,font="Roboto 14", state="r")
combo2.place(x=650,y=20)
combo2.set("Select Language")

label2 = Label(root,text="English",font="segeo 30 bold", bg="white", width=18,bd=5,relief=GROOVE)
label2.place(x=550,y=50)


f1=Frame(root,bg="Black",bd=5)
f1.place(x=550,y=118,width=440,height=210)

text2=Text(f1,font="Roboto 20", bg="white", relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=430,height=200)

scrollbar2=Scrollbar(f1)
scrollbar2.pack(side="right", fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)


# Translate Button
translate = Button(root,text="Translate",font="Roboto 12 bold italic", activebackground="purple", cursor="hand2", bd=5,bg="red",fg="white")
translate.place(x=450,y=250)

label_change()

root.mainloop()

