from tkinter import *
from drawing_numbers import random_bingo_number
from PIL import ImageTk,Image

from threading import Timer
import time
import datetime

root = Tk()
root.title("BINGO")
root.geometry("1015x570")

# BINGO balls:
##B BINGO ball
original_b_ball = Image.open("B-Bingo-ball.png") #call image b4 resize
#resizing image
resized_b = original_b_ball.resize((200,150), Image.ANTIALIAS) # resize(sides, height)
resized_b_ball = ImageTk.PhotoImage(resized_b)
bingo_ball =Label(root, image = resized_b_ball)

## I BINGO ball
original_I_ball = Image.open("I-Bingo-ball.png") #call image b4 resize
#resizing image
resized_I = original_I_ball.resize((200,150), Image.ANTIALIAS) # resize(sides, height)
resized_I_ball = ImageTk.PhotoImage(resized_I)
# bingo_ball =Label(root, image = resized_I_ball)

##N BINGO ball
original_N_ball = Image.open("N-Bingo-ball.png") #call image b4 resize
#resizing image
resized_N = original_N_ball.resize((200,150), Image.ANTIALIAS) # resize(sides, height)
resized_N_ball = ImageTk.PhotoImage(resized_N)
# bingo_ball =Label(root, image = resized_N_ball)

##G BINGO ball
original_G_ball = Image.open("G-Bingo-ball.png") #call image b4 resize
#resizing image
resized_G = original_G_ball.resize((200,150), Image.ANTIALIAS) # resize(sides, height)
resized_G_ball = ImageTk.PhotoImage(resized_G)
# bingo_ball =Label(root, image = resized_G_ball)

##O BINGO ball
original_O_ball = Image.open("O-Bingo-ball.png") #call image b4 resize
#resizing image
resized_O = original_O_ball.resize((200,150), Image.ANTIALIAS) # resize(sides, height)
resized_O_ball = ImageTk.PhotoImage(resized_O)
# bingo_ball=Label(root, image = resized_O_ball)


# drawing ball update label
def update_drawn_ball(all_random_numbers_picked_list,bingo_numbers):
    (drawn_bingo_number,bingo_numbers) = random_bingo_number(bingo_numbers)
    #call functions to update all_random_numbers_picked_list
    all_random_numbers_picked_list = all_random_numbers_picked_list +" " + drawn_bingo_number
    list_of_drawn_numbers_label.config(text = all_random_numbers_picked_list, bg = "#B900FF", font =("Helvetica", 15),padx = 5, pady = 45, )
    # update_append_bingo_numbers(all_random_numbers_picked_list,drawn_bingo_number)
    Random_number_picked_label.config(text = drawn_bingo_number, font =("Helvetica", 24), bg = "#FFFFFF")
    return Random_number_picked_label.after(5000,update_drawn_ball,all_random_numbers_picked_list, bingo_numbers) #.after(parent, ms, function = None, *args)
    
list_of_drawn_numbers_label = Label(root, text = "", bg = "#B900FF", font =("Helvetica", 15),padx = 5, pady = 45, )
list_of_drawn_numbers_label.grid(row=1, column=5, columnspan = 6, sticky="nsew")
Random_number_picked_label =Label(root,text = " fff  ", font =("Helvetica", 24), bg = "#FFFFFF") 
Random_number_picked_label.place(x = 260, y =55) 
bingo_numbers = ["B 1","B 2","B 3","B 4","B 4","B 5","B 7", "B 8","B 9","B 10","B 11","B 12","B 13","B 14","B 15","I 16","I 17","I 18","I 19","I 20","I 21","I 22","I 23","I 24","I 25","I 26","I 27","I 28","I 29","I 30","N 31","N 32","N 33","N 34","N 35","N 36","N 37","N 38","N 39","N 40","N 41","N 42","N 42","N 44","N 45","G 46","G 47","G 48","G 49","G 50","G 51","G 52","G 53","G 54","G 55","G 56","G 57","G 58","G 59","G 60","O 61","O 62","O 63","O 64","O 65","O 66","O 67","O 68","O 69","O 70","O 71","O 72","O 73","O 74","O 75"]
all_random_numbers_picked_list =""
update_drawn_ball(all_random_numbers_picked_list,bingo_numbers)

### timer for next ball
def update_timer_countdown(n):
    if n != "1":
        n= int(n)
        n -= 1
        n = str(n)
        timer.config(text = "Next draw in:" + n+  "s", padx = 5, pady = 45, font =("Helvetica", 17))
        return timer.after(1000,update_timer_countdown, n)
    else:
        return update_timer_countdown(6)


timer = Label(root, text = "Next draw in:" + "s", padx = 5, pady = 45, font =("Helvetica", 17))
timer.grid(row=1, column=1, columnspan = 2, sticky="nsew")
update_timer_countdown(6)

#ROW 1
# list_of_drawn_numbers_label = Label(root, text = all_random_numbers_picked_list, bg = "#B900FF", font =("Helvetica", 15),padx = 5, pady = 45, )
# list_of_drawn_numbers_label = Label(root, text = all_random_numbers_picked_list, bg = "#B900FF", font =("Helvetica", 15),padx = 5, pady = 45, )
# list_of_drawn_numbers_label.grid(row=1, column=5, columnspan = 6, sticky="nsew")
#ROW 1 positions
bingo_ball.grid(row=1, column=3,columnspan = 2, sticky="nsew") # chaneg to bingo_ball
# list_of_drawn_numbers_label.grid(row=1, column=5, columnspan = 6, sticky="nsew")

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
