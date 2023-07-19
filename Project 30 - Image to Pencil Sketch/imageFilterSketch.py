# Import packages
from tkinter import *
from tkinter import Tk, ttk

# Black and white colours 

co0 = "#ffffff"
co1 = "#000000"
co2 = "#63b9ff"

window = Tk()
window.title("Sketch")
window.geometry("300x356")
window.config(bg=co0)
window.resizable(width=False,height=False)

style = ttk.Style(window)
style.theme_use("clam")

window.mainloop()
