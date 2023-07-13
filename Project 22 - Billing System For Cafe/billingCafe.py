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

Label(f,font=("Lucida Calligraphy",15,"bold"),text="Moghlai Parata ... Tk 60/pc",fg="black", bg="gray").place(x=10,y=80)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Daal Puri          ... Tk 05/pc",fg="black", bg="gray").place(x=10,y=110)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Aloo Puri          ... Tk 05/pc",fg="black", bg="gray").place(x=10,y=140)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Shingara          ... Tk 10/pc",fg="black", bg="gray").place(x=10,y=170)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Samosa            ... Tk 10/pc",fg="black", bg="gray").place(x=10,y=200)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Tea                   ... Tk 10/pc",fg="black", bg="gray").place(x=10,y=230)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Naan Roti          ... Tk 15/pc",fg="black", bg="gray").place(x=10,y=260)


root.mainloop()