from datetime import date
from tkinter import *
# import pygame
from tkcalendar import *

window = Tk()
window.title("Whatever")
window.geometry("600x400")

cal = Calendar(window, selectmode="day", year=2021, month=10, day=29)
c = cal.calevent_create(date.today(), "Hello world", "reminder") #################3 IMPORTANT ########3

cal.pack(pady=20)

def return_date():
    mylable.config(text=cal.calevent_cget(c,"text")) ####################33333 IMPORANT ###############33

def new_window():
    window2 = Tk()
    window2.title("New Window")

    window2.mainloop()

button = Button(window, text="Click Me!", command=return_date)
button.pack(pady=20)

# button2 = Button(window, text="New Window", command=new_window)
# button2.pack(pady=40)

mylable = Label(window, text="<Output Here>")
mylable.pack(pady=20)

window.mainloop()


