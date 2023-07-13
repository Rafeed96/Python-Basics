from tkinter import *

root=Tk()
root.title("Billing System")
root.geometry("1000x500")
root.resizable(False,False)

Label(text="Billing System", bg="black", fg="white",font=("calibri",33),width=300,height=2).pack()

# Menu Items with Prices
f=Frame(root,bg="Gray",highlightbackground="black",highlightthickness=1,width=300,height=370)
f.place(x=10,y=118)

Label(f,text="Menu",font=("Gabriola",40,"bold"),bg="gray", fg="black").place(x=80,y=0)


root.mainloop()