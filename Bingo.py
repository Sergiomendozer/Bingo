from tkinter import *
root = Tk() # change tk to bingo
root.geometry("1000x600")
## make the layout 
#row is up and down
#column is left to right

#ROW 1
Next_draw_Label = Label(root, text = "Next draw in: 5s", padx = 10) # add time
Random_number_picked_label = Label(root, text = "Random number picked", bg = "#1DED41", font =("Helvetica", 20), padx = 15)
list_of_drawn_numbers_label = Label(root, text = "all random numbers picked list", bg = "#B900FF", font =("Helvetica", 30),padx = 25)

#ROW 1 positions
Next_draw_Label.grid(row=1, column=1, columnspan = 2,sticky="nsew")
Random_number_picked_label .grid(row=1, column=2,columnspan = 4, sticky="nsew")
list_of_drawn_numbers_label.grid(row=1, column=3, columnspan = 6,sticky="nsew")
# Grid.rowconfigure(root, 0, weight = 2)
# Grid.columnconfigure(root, 0, weight = 1)
# Grid.columnconfigure(root, 1, weight = 1)
# Grid.columnconfigure(root, 2, weight = 5)

#ROW 2
your_card_Label = Label(root, text = "Your card",bg = "#1DED41", font =("Helvetica", 10), padx = 50)
#Bots_card_Label = Label(root, text = "Bots card", bg = "#1DED41", font =("Helvetica", 10), padx = 50)


#ROW 2 positions
your_card_Label.grid(row=2, column = 1, columnspan = 3, sticky="nsew")
#Bots_card_Label.grid(row=1,  column = 1,sticky="nsew")

#ROW Player's BINGO
B_bingo = Label(root, text = "B", bg = "#1DED41", font =("Helvetica", 20), padx = 15)
I_bingo = Label(root, text = "I", bg = "#1DED41", font =("Helvetica", 20), padx = 15)
N_bingo = Label(root, text = "N", bg = "#1DED41", font =("Helvetica", 20), padx = 15)
G_bingo = Label(root, text = "G", bg = "#1DED41", font =("Helvetica", 20), padx = 15)
O_bingo = Label(root, text = "O", bg = "#1DED41", font =("Helvetica", 20), padx = 15)
#ROW BINGO positions
B_bingo.grid(row=3, column = 1, sticky="nsew")
I_bingo.grid(row=3, column = 2, sticky="nsew")
N_bingo.grid(row=3, column = 3, sticky="nsew")
G_bingo.grid(row=3, column = 4, sticky="nsew")
O_bingo.grid(row=3, column = 5, sticky="nsew")


root.mainloop()
