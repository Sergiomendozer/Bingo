from tkinter import *
root = Tk() # change tk to bingo
root.geometry("1000x600")
## make the layout 
#row is up and down
#column is left to right

#ROW 1
Next_draw_Label = Label(root, text = "Next draw in: 5s", padx = 20) # add time
Random_number_picked_label = Label(root, text = "Random number picked", bg = "#1DED41", font =("Helvetica", 20), padx = 40)
#list_of_drawn_numbers_label = Label(root, text = "all random numbers picked list", bg = "#B900FF", font =("Helvetica", 30))
Next_draw_Label.grid(row=0, column=0, sticky="nsew")
Random_number_picked_label .grid(row=0, column=1, sticky="nsew")
#list_of_drawn_numbers_label.grid(row=0, column=2, sticky="nsew")
#Random_number_picked_label.place(x=0, y=0)
# Grid.rowconfigure(root, 0, weight = 2)
# Grid.columnconfigure(root, 0, weight = 1)
# Grid.columnconfigure(root, 1, weight = 1)
# Grid.columnconfigure(root, 2, weight = 5)

#ROW 2
# your_card_Label = Label(root, text = "your card",bg = "#1DED41", font =("Helvetica", 10))
# myLabel6 = Label(root, text = "bots card", bg = "#1DED41", font =("Helvetica", 10))
# your_card_Label.grid(row=1, column=0, sticky="nsew")
# myLabel6.grid(row=1, column=1, sticky="nsew")
# Grid.rowconfigure(root, 1, weight = 1)
# Grid.columnconfigure(root, 0, weight = 20)
# Grid.columnconfigure(root, 1, weight = 20)





root.mainloop()
