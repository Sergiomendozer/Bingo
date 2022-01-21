from tkinter import *
root = Tk()
root.geometry("1000x600")
## make the layout 

myLabel1 = Label(root, text = "Random number picked")
myLabel2 = Label(root, text = "all random numbers picked list")
myLabel3 = Label(root, text = "time till next draw")
myLabel4 = Label(root, text = "time in seconds")
myLabel5 = Label(root, text = "your card")
myLabel6 = Label(root, text = "bots card")
#row is up and down
#column is left to right
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=0, column=1)
myLabel3.grid(row=1, column=0)
myLabel4.grid(row=1, column=1)
myLabel5.grid(row=1, column=2)
myLabel6.grid(row=1, column=3)

root.mainloop()
