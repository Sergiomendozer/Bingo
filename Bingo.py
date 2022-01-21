from tkinter import *
root = Tk()
root.geometry("1000x600")
## make the layout 

#Grid.rowconfigure(root, 0, weight = 1)
# Grid.columnconfigure(root, 1, weight = 1)

Random_number_picked_label = Label(root, text = "Random number picked")
list_of_drawn_numbers_label = Label(root, text = "all random numbers picked list")
Next_draw_Label = Label(root, text = "Next draw in:")
myLabel4 = Label(root, text = "time in seconds")
myLabel5 = Label(root, text = "your card")
myLabel6 = Label(root, text = "bots card")
#row is up and down
#column is left to right
Random_number_picked_label .grid(row=0, column=0)
list_of_drawn_numbers_label.grid(row=0, column=1)
myLabel3.grid(row=1, column=0)
myLabel4.grid(row=1, column=1)
myLabel5.grid(row=1, column=2)
myLabel6.grid(row=1, column=3)

root.mainloop()
