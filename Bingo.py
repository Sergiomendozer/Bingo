from tkinter import *
from drawing_numbers import random_bingo_number
from PIL import ImageTk,Image
root = Tk()
root.title("BINGO")
root.geometry("1015x570")
## make the layout 
#row is up and down
#column is left to right

drawn_bingo_number = random_bingo_number()
# BINGO balls:
##B BINGO ball
original_b_ball = Image.open("B-Bingo-ball.png") #call image b4 resize
#resizing image
resized_b = original_b_ball.resize((200,150), Image.ANTIALIAS) # resize(sides, height)
resized_b_ball = ImageTk.PhotoImage(resized_b)
Random_number_picked_label =Label(root, image = resized_b_ball)

## I BINGO ball
original_I_ball = Image.open("I-Bingo-ball.png") #call image b4 resize
#resizing image
resized_I = original_I_ball.resize((200,150), Image.ANTIALIAS) # resize(sides, height)
resized_I_ball = ImageTk.PhotoImage(resized_I)
# Random_number_picked_label =Label(root, image = resized_I_ball)

##N BINGO ball
original_N_ball = Image.open("N-Bingo-ball.png") #call image b4 resize
#resizing image
resized_N = original_N_ball.resize((200,150), Image.ANTIALIAS) # resize(sides, height)
resized_N_ball = ImageTk.PhotoImage(resized_N)
# Random_number_picked_label =Label(root, image = resized_N_ball)

##G BINGO ball
original_G_ball = Image.open("G-Bingo-ball.png") #call image b4 resize
#resizing image
resized_G = original_G_ball.resize((200,150), Image.ANTIALIAS) # resize(sides, height)
resized_G_ball = ImageTk.PhotoImage(resized_G)
# Random_number_picked_label =Label(root, image = resized_G_ball)

##O BINGO ball
original_O_ball = Image.open("O-Bingo-ball.png") #call image b4 resize
#resizing image
resized_O = original_O_ball.resize((200,150), Image.ANTIALIAS) # resize(sides, height)
resized_O_ball = ImageTk.PhotoImage(resized_O)
#Random_number_picked_label =Label(root, image = resized_O_ball)

#ROW 1
Next_draw_Label = Label(root, text = "Next draw in: 5s", padx = 5, pady = 45, font =("Helvetica", 17)) # add time
#Random_number_picked_label = Label(root, text = drawn_bingo_number, bg = "#1DED41", font =("Helvetica", 40), padx = 5,pady = 45, )
#Random_number_picked_label =Label(root, image = resized_b_ball)
list_of_drawn_numbers_label = Label(root, text = "all random numbers picked list", bg = "#B900FF", font =("Helvetica", 15),padx = 5, pady = 45, )

#ROW 1 positions
Next_draw_Label.grid(row=1, column=1, columnspan = 2, sticky="nsew")
Random_number_picked_label.grid(row=1, column=3,columnspan = 2, sticky="nsew") # chaneg to bingo_ball
Random_number_picked_label.grid(row=1, column=3,columnspan = 2, sticky="nsew") # place
list_of_drawn_numbers_label.grid(row=1, column=5, columnspan = 6, sticky="nsew")

#ROW 2
your_card_Label = Label(root, text = "Your card",bg = "#FF4646", font =("Helvetica", 15), padx = 50)
Bots_card_Label = Label(root, text = "Bots card", bg = "#96FF50", font =("Helvetica", 15), padx = 50)


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

#BINGO row 1
B_bingo = Button(root, text = "B1", bg = "#00CCFF", font =("Helvetica", 20))
I_bingo = Button(root, text = "I", bg = "#FF0000", font =("Helvetica", 20))
N_bingo = Button(root, text = "N", bg = "#E2DF00", font =("Helvetica", 20))
G_bingo = Button(root, text = "G", bg = "#F96815", font =("Helvetica", 20))
O_bingo = Button(root, text = "O", bg = "#00FF33", font =("Helvetica", 20))
#BINGO row 1 positions
B_bingo.grid(row=4, column = 1, sticky="nsew")
I_bingo.grid(row=4, column = 2, sticky="nsew")
N_bingo.grid(row=4, column = 3, sticky="nsew")
G_bingo.grid(row=4, column = 4, sticky="nsew")
O_bingo.grid(row=4, column = 5, sticky="nsew")

#Bots's BINGO row 1
B_bingo = Button(root, text = "B", bg = "#00CCFF", font =("Helvetica", 20))
I_bingo = Button(root, text = "I", bg = "#FF0000", font =("Helvetica", 20))
N_bingo = Button(root, text = "N", bg = "#E2DF00", font =("Helvetica", 20))
G_bingo = Button(root, text = "G", bg = "#F96815", font =("Helvetica", 20))
O_bingo = Button(root, text = "O", bg = "#00FF33", font =("Helvetica", 20))
#Bots's BINGO row 1 positions
B_bingo.grid(row=4, column = 6, sticky="nsew")
I_bingo.grid(row=4, column = 7, sticky="nsew")
N_bingo.grid(row=4, column = 8, sticky="nsew")
G_bingo.grid(row=4, column = 9, sticky="nsew")
O_bingo.grid(row=4, column = 10, sticky="nsew")

#BINGO row 2
B_bingo = Button(root, text = "B2", bg = "#00CCFF", font =("Helvetica", 20))
I_bingo = Button(root, text = "I", bg = "#FF0000", font =("Helvetica", 20))
N_bingo = Button(root, text = "N", bg = "#E2DF00", font =("Helvetica", 20))
G_bingo = Button(root, text = "G", bg = "#F96815", font =("Helvetica", 20))
O_bingo = Button(root, text = "O", bg = "#00FF33", font =("Helvetica", 20))
#BINGO row 2 positions
B_bingo.grid(row=5, column = 1, sticky="nsew")
I_bingo.grid(row=5, column = 2, sticky="nsew")
N_bingo.grid(row=5, column = 3, sticky="nsew")
G_bingo.grid(row=5, column = 4, sticky="nsew")
O_bingo.grid(row=5, column = 5, sticky="nsew")

#Bots's BINGO row 2
B_bingo = Button(root, text = "B", bg = "#00CCFF", font =("Helvetica", 20))
I_bingo = Button(root, text = "I", bg = "#FF0000", font =("Helvetica", 20))
N_bingo = Button(root, text = "N", bg = "#E2DF00", font =("Helvetica", 20))
G_bingo = Button(root, text = "G", bg = "#F96815", font =("Helvetica", 20))
O_bingo = Button(root, text = "O", bg = "#00FF33", font =("Helvetica", 20))
#Bots's BINGO row 2 positions
B_bingo.grid(row=5, column = 6, sticky="nsew")
I_bingo.grid(row=5, column = 7, sticky="nsew")
N_bingo.grid(row=5, column = 8, sticky="nsew")
G_bingo.grid(row=5, column = 9, sticky="nsew")
O_bingo.grid(row=5, column = 10, sticky="nsew")


#STAR image formant
#call image b4 resize
original_star = Image.open("STAR.png")
#resizing image
resized = original_star.resize((95,52), Image.ANTIALIAS) # resize(sides, height)
star = ImageTk.PhotoImage(resized)

#BINGO row 3
B_bingo = Button(root, text = "B3", bg = "#00CCFF", font =("Helvetica", 20))
I_bingo = Button(root, text = "I", bg = "#FF0000", font =("Helvetica", 20))
N_bingo = Label(root, image = star) #FREE SPACE
G_bingo = Button(root, text = "G", bg = "#F96815", font =("Helvetica", 20))
O_bingo = Button(root, text = "O", bg = "#00FF33", font =("Helvetica", 20))
#BINGO row 3 positions
B_bingo.grid(row=6, column = 1, sticky="nsew")
I_bingo.grid(row=6, column = 2, sticky="nsew")
N_bingo.grid(row=6, column = 3, sticky="nsew")
G_bingo.grid(row=6, column = 4, sticky="nsew")
O_bingo.grid(row=6, column = 5, sticky="nsew")

#Bots's BINGO row 3
B_bingo = Button(root, text = "B", bg = "#00CCFF", font =("Helvetica", 20))
I_bingo = Button(root, text = "I", bg = "#FF0000", font =("Helvetica", 20))
N_bingo = Label(root, image = star) #FREE SPACE
G_bingo = Button(root, text = "G", bg = "#F96815", font =("Helvetica", 20))
O_bingo = Button(root, text = "O", bg = "#00FF33", font =("Helvetica", 20))
#Bots's BINGO row 3 positions
B_bingo.grid(row=6, column = 6, sticky="nsew")
I_bingo.grid(row=6, column = 7, sticky="nsew")
N_bingo.grid(row=6, column = 8, sticky="nsew")
G_bingo.grid(row=6, column = 9, sticky="nsew")
O_bingo.grid(row=6, column = 10, sticky="nsew")

#BINGO row 4
B_bingo = Button(root, text = "B4", bg = "#00CCFF", font =("Helvetica", 20))
I_bingo = Button(root, text = "I", bg = "#FF0000", font =("Helvetica", 20))
N_bingo = Button(root, text = "N", bg = "#E2DF00", font =("Helvetica", 20))
G_bingo = Button(root, text = "G", bg = "#F96815", font =("Helvetica", 20))
O_bingo = Button(root, text = "O", bg = "#00FF33", font =("Helvetica", 20))
#BINGO row 4 positions
B_bingo.grid(row=7, column = 1, sticky="nsew")
I_bingo.grid(row=7, column = 2, sticky="nsew")
N_bingo.grid(row=7, column = 3, sticky="nsew")
G_bingo.grid(row=7, column = 4, sticky="nsew")
O_bingo.grid(row=7, column = 5, sticky="nsew")

#Bots's BINGO row 4
B_bingo = Button(root, text = "B", bg = "#00CCFF", font =("Helvetica", 20))
I_bingo = Button(root, text = "I", bg = "#FF0000", font =("Helvetica", 20))
N_bingo = Button(root, text = "N", bg = "#E2DF00", font =("Helvetica", 20))
G_bingo = Button(root, text = "G", bg = "#F96815", font =("Helvetica", 20))
O_bingo = Button(root, text = "O", bg = "#00FF33", font =("Helvetica", 20))
#Bots's BINGO row 4 positions
B_bingo.grid(row=7, column = 6, sticky="nsew")
I_bingo.grid(row=7, column = 7, sticky="nsew")
N_bingo.grid(row=7, column = 8, sticky="nsew")
G_bingo.grid(row=7, column = 9, sticky="nsew")
O_bingo.grid(row=7, column = 10, sticky="nsew")

#BINGO row 5
B_bingo = Button(root, text = "B5", bg = "#00CCFF", font =("Helvetica", 20))
I_bingo = Button(root, text = "I", bg = "#FF0000", font =("Helvetica", 20))
N_bingo = Button(root, text = "N", bg = "#E2DF00", font =("Helvetica", 20))
G_bingo = Button(root, text = "G", bg = "#F96815", font =("Helvetica", 20))
O_bingo = Button(root, text = "O", bg = "#00FF33", font =("Helvetica", 20))
#BINGO row 5 positions
B_bingo.grid(row=8, column = 1, sticky="nsew")
I_bingo.grid(row=8, column = 2, sticky="nsew")
N_bingo.grid(row=8, column = 3, sticky="nsew")
G_bingo.grid(row=8, column = 4, sticky="nsew")
O_bingo.grid(row=8, column = 5, sticky="nsew")

#Bots's BINGO row 5
B_bingo = Button(root, text = "B", bg = "#00CCFF", font =("Helvetica", 20))
I_bingo = Button(root, text = "I", bg = "#FF0000", font =("Helvetica", 20))
N_bingo = Button(root, text = "N", bg = "#E2DF00", font =("Helvetica", 20))
G_bingo = Button(root, text = "G", bg = "#F96815", font =("Helvetica", 20))
O_bingo = Button(root, text = "O", bg = "#00FF33", font =("Helvetica", 20))
#Bots's BINGO row 5 positions
B_bingo.grid(row=8, column = 6, sticky="nsew")
I_bingo.grid(row=8, column = 7, sticky="nsew")
N_bingo.grid(row=8, column = 8, sticky="nsew")
G_bingo.grid(row=8, column = 9, sticky="nsew")
O_bingo.grid(row=8, column = 10, sticky="nsew")

#last row
Bingo_button = Button(root, text = "BINGO!", bg = "#B900FF", font =("Helvetica", 25))
blank = Label(root, bg = "#737373")
New_card = Button(root, text = "New Card", bg = "#29EFD1", font =("Helvetica", 20))
New_game = Button(root, text = "New Game", bg = "#FF4646", font =("Helvetica", 20))
pause_play = Button(root, text = "Pause/Play", bg = "#96FF50", font =("Helvetica", 20))

#last row positions # columnspan = 5
Bingo_button.grid(row=9, column = 1, columnspan = 3, sticky="nsew")
blank.grid(row=9, column = 4, columnspan = 1, sticky="nsew")
New_card.grid(row=9, column = 5, columnspan = 2,sticky="nsew")
New_game.grid(row=9, column = 7, columnspan = 2,sticky="nsew")
pause_play.grid(row=9, column = 9, columnspan = 2,sticky="nsew")

root.mainloop()
