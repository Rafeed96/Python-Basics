from tkinter import *

root=Tk()
root.title("Billing System")
root.geometry("1000x500")
root.resizable(False,False)

def Reset():
    entry_parata.delete(0,END)
    entry_daal.delete(0,END)
    entry_aloo.delete(0,END)
    entry_shingara.delete(0,END)
    entry_samosa.delete(0,END)
    entry_tea.delete(0,END)
    entry_naan.delete(0,END)


def Total():
    try: i1=int(parata.get())
    except: i1=0
    
    try: i2=int(daal.get())
    except: i2=0

    try: i3=int(aloo.get())
    except: i3=0

    try: i4=int(shingara.get())
    except: i4=0

    try: i5=int(samosa.get())
    except: i5=0

    try: i6=int(tea.get())
    except: i6=0

    try: i7=int(naan.get())
    except: i7=0

    # Update cost of each item based on item frequency 
    c1 = 60*i1
    c2 = 5*i2
    c3 = 5*i3
    c4 = 10*i4
    c5 = 10*i5
    c6 = 10*i6
    c7 = 15*i7

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

# Enter Items
f1 =Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()

parata=StringVar()
daal=StringVar()
aloo=StringVar()
shingara=StringVar()
samosa=StringVar()
tea=StringVar()
naan=StringVar()

#Label
lbl_parata=Label(f1,font=("aria",20,"bold"),text="Parata",width=12,fg="black")
lbl_daal=Label(f1,font=("aria",20,"bold"),text="Daal",width=12,fg="black")
lbl_aloo=Label(f1,font=("aria",20,"bold"),text="Aloo",width=12,fg="black")
lbl_shingara=Label(f1,font=("aria",20,"bold"),text="Shingara",width=12,fg="black")
lbl_samosa=Label(f1,font=("aria",20,"bold"),text="Samosa",width=12,fg="black")
lbl_tea=Label(f1,font=("aria",20,"bold"),text="Tea",width=12,fg="black")
lbl_naan=Label(f1,font=("aria",20,"bold"),text="Naan",width=12,fg="black")

lbl_parata.grid(row=1,column=0)
lbl_daal.grid(row=2,column=0)
lbl_aloo.grid(row=3,column=0)
lbl_shingara.grid(row=4,column=0)
lbl_samosa.grid(row=5,column=0)
lbl_tea.grid(row=6,column=0)
lbl_naan.grid(row=7,column=0)

#Entry
entry_parata=Entry(f1,font=("aria",20,"bold"),textvariable=parata,bd=6,width=8,bg="lightgreen")
entry_daal=Entry(f1,font=("aria",20,"bold"),textvariable=daal,bd=6,width=8,bg="lightgreen")
entry_aloo=Entry(f1,font=("aria",20,"bold"),textvariable=aloo,bd=6,width=8,bg="lightgreen")
entry_shingara=Entry(f1,font=("aria",20,"bold"),textvariable=shingara,bd=6,width=8,bg="lightgreen")
entry_samosa=Entry(f1,font=("aria",20,"bold"),textvariable=samosa,bd=6,width=8,bg="lightgreen")
entry_tea=Entry(f1,font=("aria",20,"bold"),textvariable=tea,bd=6,width=8,bg="lightgreen")
entry_naan=Entry(f1,font=("aria",20,"bold"),textvariable=naan,bd=6,width=8,bg="lightgreen")

entry_parata.grid(row=1,column=1)
entry_daal.grid(row=2,column=1)
entry_aloo.grid(row=3,column=1)
entry_shingara.grid(row=4,column=1)
entry_samosa.grid(row=5,column=1)
entry_tea.grid(row=6,column=1)
entry_naan.grid(row=7,column=1)


#Button

btn_reset=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,"bold"), width=10,text="Reset",command=Reset)
btn_reset.grid(row=8,column=0)

btn_total=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,"bold"), width=10,text="Total",command=Total)
btn_total.grid(row=8,column=1)

root.mainloop()