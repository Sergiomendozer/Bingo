from tkinter import *
root = Tk()
## make the layout 
#myLabel1 = Label(root, text = "1").grid(row=0, column=0)
myLabel1 = Label(root, text = "1")
myLabel2 = Label(root, text = "2")
myLabel3 = Label(root, text = "3")
myLabel4 = Label(root, text = "4")
myLabel5 = Label(root, text = "5")
myLabel6 = Label(root, text = "6")
#row is up and down
#column is left to right
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=0, column=1)
myLabel3.grid(row=0, column=2)
myLabel4.grid(row=1, column=0)
myLabel5.grid(row=1, column=1)
myLabel6.grid(row=1, column=2)

root.mainloop()
