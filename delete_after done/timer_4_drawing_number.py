from threading import Timer
from tkinter import *
import time
import datetime
root = Tk()
root.title("update timer loop")
root.geometry("600x400")


def update_timer_countdown(n):
    if n != "0":
        n= int(n)
        n -= 1
        n = str(n)
        timer.config(text= n+"s",font =("Helvetica", 100), padx = 100, pady=100)
        return timer.after(1000,update_timer_countdown, n)
    else:
        return update_timer_countdown(6)


timer = Label(root, text = "",font =("Helvetica", 100), padx = 100, pady=100)
timer.pack() 
update_timer_countdown(6)
root.mainloop()