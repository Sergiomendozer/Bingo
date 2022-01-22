from tkinter import *
root = Tk() # change tk to bingo
root.geometry("1015x600")
## make the layout 
#row is up and down
#column is left to right

#ROW 1
# Next_draw_Label = Label(root, text = "Next draw in: 5s", padx = 10) # add time
# Random_number_picked_label = Label(root, text = "Random number picked", bg = "#1DED41", font =("Helvetica", 20), padx = 15)
# list_of_drawn_numbers_label = Label(root, text = "all random numbers picked list", bg = "#B900FF", font =("Helvetica", 30),padx = 25)

# #ROW 1 positions
# Next_draw_Label.grid(row=1, column=1, columnspan = 2,sticky="nsew")
# Random_number_picked_label .grid(row=1, column=2,columnspan = 4, sticky="nsew")
# list_of_drawn_numbers_label.grid(row=1, column=3, columnspan = 6,sticky="nsew")

#ROW 2
your_card_Label = Label(root, text = "Your card",bg = "#C91A3A", font =("Helvetica", 10), padx = 50)
Bots_card_Label = Label(root, text = "Bots card", bg = "#1E9E23", font =("Helvetica", 10), padx = 50)


#ROW 2 positions
your_card_Label.grid(row=2, column = 1, columnspan = 5, sticky="nsew")
Bots_card_Label.grid(row=2,  column = 6,columnspan = 5, sticky="nsew")

#Player's BINGO
B_bingo = Label(root, text = "B", bg = "#00CCFF", font =("Helvetica", 20), padx = 40)
I_bingo = Label(root, text = "I", bg = "#FF0000", font =("Helvetica", 20), padx = 40)
N_bingo = Label(root, text = "N", bg = "#E2DF00", font =("Helvetica", 20), padx = 40)
G_bingo = Label(root, text = "G", bg = "#F96815", font =("Helvetica", 20), padx = 40)
O_bingo = Label(root, text = "O", bg = "#00FF33", font =("Helvetica", 20), padx = 40)
#Player's BINGO positions
B_bingo.grid(row=3, column = 1, sticky="nsew")
I_bingo.grid(row=3, column = 2, sticky="nsew")
N_bingo.grid(row=3, column = 3, sticky="nsew")
G_bingo.grid(row=3, column = 4, sticky="nsew")
O_bingo.grid(row=3, column = 5, sticky="nsew")

#Bots's BINGO
B_bingo = Label(root, text = "B", bg = "#00CCFF", font =("Helvetica", 20), padx = 40)
I_bingo = Label(root, text = "I", bg = "#FF0000", font =("Helvetica", 20), padx = 40)
N_bingo = Label(root, text = "N", bg = "#E2DF00", font =("Helvetica", 20), padx = 40)
G_bingo = Label(root, text = "G", bg = "#F96815", font =("Helvetica", 20), padx = 40)
O_bingo = Label(root, text = "O", bg = "#00FF33", font =("Helvetica", 20), padx = 40)
#Bots's BINGO positions
B_bingo.grid(row=3, column = 6, sticky="nsew")
I_bingo.grid(row=3, column = 7, sticky="nsew")
N_bingo.grid(row=3, column = 8, sticky="nsew")
G_bingo.grid(row=3, column = 9, sticky="nsew")
O_bingo.grid(row=3, column = 10, sticky="nsew")


root.mainloop()
