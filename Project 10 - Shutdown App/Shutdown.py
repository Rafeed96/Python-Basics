from tkinter import *
import os

root=Tk()
root.title("Shutdown App")
root.geometry("400x580")

# Restart Button
restart_time_button = PhotoImage(file="E:\Projects\Repositories\Python\Python-Basics\Project 10 - Shutdown App\redo-refresh-restart.jpg")
first_botton = Button(root, image=restart_time_button, borderwidth=0, cursor="hand2")
first_botton.place(x=10, y=10)

# Close Button
close_button = PhotoImage(file="Project 10 - Shutdown App/close-button-red.jpg")
second_botton = Button(root, image=close_button, borderwidth=0, cursor="hand2")
second_botton.place(x=200, y=10)

# Restart Button
restart_button = PhotoImage(file="E:\Projects\Repositories\Python\Python-Basics\Project 10 - Shutdown App\redo-refresh-restart.jpg")
third_botton = Button(root, image=restart_button, borderwidth=0, cursor="hand2")
third_botton.place(x=10, y=200)

# Shutdown Button
shutdown_button = PhotoImage(file="E:\Projects\Repositories\Python\Python-Basics\Project 10 - Shutdown App\shutdown.jpg")
fourth_botton = Button(root, image=shutdown_button, borderwidth=0, cursor="hand2")
fourth_botton.place(x=200, y=200)





root.mainloop()
