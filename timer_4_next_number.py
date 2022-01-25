from threading import Timer
from tkinter import *
import time
import datetime
root = Tk()
root.title("update Label")
root.geometry("600x400")

# def countdown(s):
#     # If not zero, decrement total time by one second
#     while s > -1:
#         # Timer represents time left on countdown
#         timer = datetime.timedelta(seconds = s)
#         # Timer made to str and s added to string to respresent secs        
#         timer = str(timer)
#         timer = timer + "s"
#         # Prints the time left on the timer
#         print(timer[-2:], end="\r") #end prints in same line
#         # Delays the program one second
#         time.sleep(1)
#         # Reduces total time by one second
#         s -= 1
#     countdown(int(5))

 
# countdown(int(5))

timer = Label(root, text = "test",font =("Helvetica", 100), padx = 100, pady=100)
timer.pack() 
root.mainloop()