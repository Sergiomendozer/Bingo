from tkinter import *
from drawing_numbers import random_bingo_number
from PIL import ImageTk, Image
import random
from threading import Timer
import time
import datetime

root = Tk()
root.title("BINGO")
root.geometry("1015x590")

# BINGO balls:
##B BINGO ball
original_B_ball = Image.open("B-Bingo-ball.png")  # call image b4 resize
# resizing image
resized_B = original_B_ball.resize((200, 150), Image.ANTIALIAS)  # resize(sides, height)
resized_B_ball = ImageTk.PhotoImage(resized_B)
## I BINGO ball
original_I_ball = Image.open("I-Bingo-ball.png")  # call image b4 resize
resized_I = original_I_ball.resize((200, 150), Image.ANTIALIAS)  # resize(sides, height)
resized_I_ball = ImageTk.PhotoImage(resized_I)
##N BINGO ball
original_N_ball = Image.open("N-Bingo-ball.png")  # call image b4 resize
resized_N = original_N_ball.resize((200, 150), Image.ANTIALIAS)  # resize(sides, height)
resized_N_ball = ImageTk.PhotoImage(resized_N)
##G BINGO ball
original_G_ball = Image.open("G-Bingo-ball.png")  # call image b4 resize
resized_G = original_G_ball.resize((200, 150), Image.ANTIALIAS)  # resize(sides, height)
resized_G_ball = ImageTk.PhotoImage(resized_G)
##O BINGO ball
original_O_ball = Image.open("O-Bingo-ball.png")  # call image b4 resize
resized_O = original_O_ball.resize((200, 150), Image.ANTIALIAS)  # resize(sides, height)
resized_O_ball = ImageTk.PhotoImage(resized_O)


# ROW 1
bingo_ball = Label(root, image=resized_O_ball)


def bingo_ball_color(
    drawn_bingo_number,
    B_list_drawn_str,
    I_list_drawn_str,
    N_list_drawn_str,
    G_list_drawn_str,
    O_list_drawn_str,
):
    if drawn_bingo_number.startswith("B"):
        bingo_ball.config(image=resized_B_ball)
        B_list_drawn_str = B_list_drawn_str + " " + drawn_bingo_number[2:]
        B_list_drawn.config(
            text=B_list_drawn_str,
            bg="#00CCFF",
            font=("Helvetica", 15),
            padx=2,
            pady=4,
        )
        return (
            B_list_drawn_str,
            I_list_drawn_str,
            N_list_drawn_str,
            G_list_drawn_str,
            O_list_drawn_str,
        )
    elif drawn_bingo_number.startswith("I"):
        bingo_ball.config(image=resized_I_ball)
        I_list_drawn_str = I_list_drawn_str + " " + drawn_bingo_number[2:]
        I_list_drawn.config(
            text=I_list_drawn_str,
            bg="#FF0000",
            font=("Helvetica", 15),
            padx=2,
            pady=4,
        )
        return (
            B_list_drawn_str,
            I_list_drawn_str,
            N_list_drawn_str,
            G_list_drawn_str,
            O_list_drawn_str,
        )

    elif drawn_bingo_number.startswith("N"):
        bingo_ball.config(image=resized_N_ball)
        N_list_drawn_str = N_list_drawn_str + " " + drawn_bingo_number[2:]
        N_list_drawn.config(
            text=N_list_drawn_str,
            bg="#E2DF00",
            font=("Helvetica", 15),
            padx=2,
            pady=4,
        )
        return (
            B_list_drawn_str,
            I_list_drawn_str,
            N_list_drawn_str,
            G_list_drawn_str,
            O_list_drawn_str,
        )

    elif drawn_bingo_number.startswith("G"):
        bingo_ball.config(image=resized_G_ball)
        G_list_drawn_str = G_list_drawn_str + " " + drawn_bingo_number[2:]
        G_list_drawn.config(
            text=G_list_drawn_str,
            bg="#F96815",
            font=("Helvetica", 15),
            padx=2,
            pady=4,
        )
        return (
            B_list_drawn_str,
            I_list_drawn_str,
            N_list_drawn_str,
            G_list_drawn_str,
            O_list_drawn_str,
        )
    elif drawn_bingo_number.startswith("O"):
        bingo_ball.config(image=resized_O_ball)
        O_list_drawn_str = O_list_drawn_str + " " + drawn_bingo_number[2:]
        O_list_drawn.config(
            text=O_list_drawn_str,
            bg="#00FF33",
            font=("Helvetica", 15),
            padx=2,
            pady=4,
        )
        return (
            B_list_drawn_str,
            I_list_drawn_str,
            N_list_drawn_str,
            G_list_drawn_str,
            O_list_drawn_str,
        )


bingo_ball.grid(row=1, column=3, columnspan=2, rowspan=6, sticky="nsew")

# drawing ball update label
def update_drawn_ball(
    bingo_numbers,
    B_list_drawn_str,
    I_list_drawn_str,
    N_list_drawn_str,
    G_list_drawn_str,
    O_list_drawn_str,
):
    (drawn_bingo_number, bingo_numbers) = random_bingo_number(bingo_numbers)
    Random_number_picked_label.config(
        text=drawn_bingo_number, font=("Helvetica", 24), bg="#FFFFFF"
    )
    (
        B_list_drawn_str,
        I_list_drawn_str,
        N_list_drawn_str,
        G_list_drawn_str,
        O_list_drawn_str,
    ) = bingo_ball_color(
        drawn_bingo_number,
        B_list_drawn_str,
        I_list_drawn_str,
        N_list_drawn_str,
        G_list_drawn_str,
        O_list_drawn_str,
    )
    return Random_number_picked_label.after(
        5000,
        update_drawn_ball,
        bingo_numbers,
        B_list_drawn_str,
        I_list_drawn_str,
        N_list_drawn_str,
        G_list_drawn_str,
        O_list_drawn_str,
    )  # .after(parent, ms, function = None, *args)


B_list_drawn_str = "B:"
B_list_drawn = Label(
    root,
    text=B_list_drawn_str,
    bg="#00CCFF",
    font=("Helvetica", 15),
    padx=2,
    pady=4,
)
B_list_drawn.grid(row=1, column=5, columnspan=6, rowspan=1, sticky="nsew")

I_list_drawn_str = "I:"
I_list_drawn = Label(
    root,
    text=I_list_drawn_str,
    bg="#FF0000",
    font=("Helvetica", 15),
    padx=2,
    pady=4,
)
I_list_drawn.grid(row=2, column=5, columnspan=6, rowspan=1, sticky="nsew")

N_list_drawn_str = "N:"
N_list_drawn = Label(
    root,
    text=N_list_drawn_str,
    bg="#E2DF00",
    font=("Helvetica", 15),
    padx=2,
    pady=4,
)
N_list_drawn.grid(row=3, column=5, columnspan=6, rowspan=1, sticky="nsew")

G_list_drawn_str = "G:"
G_list_drawn = Label(
    root,
    text=G_list_drawn_str,
    bg="#F96815",
    font=("Helvetica", 15),
    padx=2,
    pady=4,
)
G_list_drawn.grid(row=4, column=5, columnspan=6, rowspan=1, sticky="nsew")

O_list_drawn_str = "O:"
O_list_drawn = Label(
    root,
    text=O_list_drawn_str,
    bg="#00FF33",
    font=("Helvetica", 15),
    padx=2,
    pady=4,
)
O_list_drawn.grid(row=5, column=5, columnspan=6, rowspan=1, sticky="nsew")

Random_number_picked_label = Label(
    root, text=" fff  ", font=("Helvetica", 24), bg="#FFFFFF"
)
Random_number_picked_label.place(x=259, y=63)
bingo_numbers = [
    "B 1",
    "B 2",
    "B 3",
    "B 4",
    "B 4",
    "B 5",
    "B 7",
    "B 8",
    "B 9",
    "B 10",
    "B 11",
    "B 12",
    "B 13",
    "B 14",
    "B 15",
    "I 16",
    "I 17",
    "I 18",
    "I 19",
    "I 20",
    "I 21",
    "I 22",
    "I 23",
    "I 24",
    "I 25",
    "I 26",
    "I 27",
    "I 28",
    "I 29",
    "I 30",
    "N 31",
    "N 32",
    "N 33",
    "N 34",
    "N 35",
    "N 36",
    "N 37",
    "N 38",
    "N 39",
    "N 40",
    "N 41",
    "N 42",
    "N 42",
    "N 44",
    "N 45",
    "G 46",
    "G 47",
    "G 48",
    "G 49",
    "G 50",
    "G 51",
    "G 52",
    "G 53",
    "G 54",
    "G 55",
    "G 56",
    "G 57",
    "G 58",
    "G 59",
    "G 60",
    "O 61",
    "O 62",
    "O 63",
    "O 64",
    "O 65",
    "O 66",
    "O 67",
    "O 68",
    "O 69",
    "O 70",
    "O 71",
    "O 72",
    "O 73",
    "O 74",
    "O 75",
]
# B_list_drawn_str,I_list_drawn_str, N_list_drawn_str,G_list_drawn_str,O_list_drawn_str
update_drawn_ball(
    bingo_numbers,
    B_list_drawn_str,
    I_list_drawn_str,
    N_list_drawn_str,
    G_list_drawn_str,
    O_list_drawn_str,
)

### timer for next ball
def update_timer_countdown(n):
    if n != "1":
        n = int(n)
        n -= 1
        n = str(n)
        timer.config(
            text="Next draw in:" + n + "s", padx=5, pady=45, font=("Helvetica", 17)
        )
        return timer.after(1000, update_timer_countdown, n)
    else:
        return update_timer_countdown(6)


timer = Label(root, text="Next draw in:" + "s", padx=5, pady=45, font=("Helvetica", 17))
timer.grid(row=1, column=1, columnspan=2, rowspan=5, sticky="nsew")
update_timer_countdown(6)

# ROW 2
your_card_Label = Label(
    root, text="Your card", bg="#FF4646", font=("Helvetica", 15), padx=50
)
Bots_card_Label = Label(
    root, text="Bots card", bg="#96FF50", font=("Helvetica", 15), padx=50
)


# ROW 2 positions
your_card_Label.grid(row=7, column=1, columnspan=5, sticky="nsew")
Bots_card_Label.grid(row=7, column=6, columnspan=5, sticky="nsew")

# Player's BINGO
B_bingo = Label(root, text="B", bg="#00CCFF", font=("Helvetica", 20), padx=40)
I_bingo = Label(root, text="I", bg="#FF0000", font=("Helvetica", 20), padx=40)
N_bingo = Label(root, text="N", bg="#E2DF00", font=("Helvetica", 20), padx=40)
G_bingo = Label(root, text="G", bg="#F96815", font=("Helvetica", 20), padx=40)
O_bingo_player = Label(root, text="O", bg="#00FF33", font=("Helvetica", 20), padx=40)
# Player's BINGO positions
B_bingo.grid(row=8, column=1, sticky="nsew")
I_bingo.grid(row=8, column=2, sticky="nsew")
N_bingo.grid(row=8, column=3, sticky="nsew")
G_bingo.grid(row=8, column=4, sticky="nsew")
O_bingo_player.grid(row=8, column=5, sticky="nsew")

# Bots's BINGO
B_bingo = Label(root, text="B", bg="#00CCFF", font=("Helvetica", 20), padx=40)
I_bingo = Label(root, text="I", bg="#FF0000", font=("Helvetica", 20), padx=40)
N_bingo = Label(root, text="N", bg="#E2DF00", font=("Helvetica", 20), padx=40)
G_bingo = Label(root, text="G", bg="#F96815", font=("Helvetica", 20), padx=40)
O_bingo_bot = Label(root, text="O", bg="#00FF33", font=("Helvetica", 20), padx=40)
# Bots's BINGO positions
B_bingo.grid(row=8, column=6, sticky="nsew")
I_bingo.grid(row=8, column=7, sticky="nsew")
N_bingo.grid(row=8, column=8, sticky="nsew")
G_bingo.grid(row=8, column=9, sticky="nsew")
O_bingo_bot.grid(row=8, column=10, sticky="nsew")

### Buttons Clicks all
def click_row_1_B():
    # increase the click count
    click_row_1_B.click += 1
    # lengths of color list
    colorLen = len(click_row_1_B.colors)
    # set background to "click % colorLen" index in color list
    B_bingo_row_1.config(bg=click_row_1_B.colors[click_row_1_B.click % colorLen])


# put properties on the function - do it before you use them (avoid NameError)
# colors will be cycled in order with each click, wrapping around
click_row_1_B.click = 0
click_row_1_B.colors = ["#00ccff", "#B900ff"]


def click_row_1_I():
    click_row_1_I.click += 1
    colorLen = len(click_row_1_B.colors)
    I_bingo_row_1.config(bg=click_row_1_I.colors[click_row_1_I.click % colorLen])


click_row_1_I.click = 0
click_row_1_I.colors = ["#FF0000", "#B900ff"]


def click_row_1_N():
    click_row_1_N.click += 1
    colorLen = len(click_row_1_N.colors)
    N_bingo_row_1.config(bg=click_row_1_N.colors[click_row_1_N.click % colorLen])


click_row_1_N.click = 0
click_row_1_N.colors = ["#E2DF00", "#B900ff"]


def click_row_1_G():
    click_row_1_G.click += 1
    colorLen = len(click_row_1_G.colors)
    G_bingo_row_1.config(bg=click_row_1_G.colors[click_row_1_G.click % colorLen])


click_row_1_G.click = 0
click_row_1_G.colors = ["#F96815", "#B900ff"]


def click_row_1_O():
    click_row_1_O.click += 1
    colorLen = len(click_row_1_O.colors)
    O_bingo_row_1.config(bg=click_row_1_O.colors[click_row_1_O.click % colorLen])


click_row_1_O.click = 0
click_row_1_O.colors = ["#00FF33", "#B900ff"]


def click_row_2_B():
    click_row_2_B.click += 1
    colorLen = len(click_row_2_B.colors)
    B_bingo_row_2.config(bg=click_row_2_B.colors[click_row_2_B.click % colorLen])


click_row_2_B.click = 0
click_row_2_B.colors = ["#00ccff", "#B900ff"]


def click_row_2_I():
    click_row_2_I.click += 1
    colorLen = len(click_row_2_B.colors)
    I_bingo_row_2.config(bg=click_row_2_I.colors[click_row_2_I.click % colorLen])


click_row_2_I.click = 0
click_row_2_I.colors = ["#FF0000", "#B900ff"]


def click_row_2_N():
    click_row_2_N.click += 1
    colorLen = len(click_row_2_N.colors)
    N_bingo_row_2.config(bg=click_row_2_N.colors[click_row_2_N.click % colorLen])


click_row_2_N.click = 0
click_row_2_N.colors = ["#E2DF00", "#B900ff"]


def click_row_2_G():
    click_row_2_G.click += 1
    colorLen = len(click_row_2_G.colors)
    G_bingo_row_2.config(bg=click_row_2_G.colors[click_row_2_G.click % colorLen])


click_row_2_G.click = 0
click_row_2_G.colors = ["#F96815", "#B900ff"]


def click_row_2_O():
    click_row_2_O.click += 1
    colorLen = len(click_row_2_O.colors)
    O_bingo_row_2.config(bg=click_row_2_O.colors[click_row_2_O.click % colorLen])


click_row_2_O.click = 0
click_row_2_O.colors = ["#00FF33", "#B900ff"]


def click_row_3_B():
    click_row_3_B.click += 1
    colorLen = len(click_row_3_B.colors)
    B_bingo_row_3.config(bg=click_row_3_B.colors[click_row_3_B.click % colorLen])


click_row_3_B.click = 0
click_row_3_B.colors = ["#00ccff", "#B900ff"]


def click_row_3_I():
    click_row_3_I.click += 1
    colorLen = len(click_row_3_B.colors)
    I_bingo_row_3.config(bg=click_row_3_I.colors[click_row_3_I.click % colorLen])


click_row_3_I.click = 0
click_row_3_I.colors = ["#FF0000", "#B900ff"]


def click_row_3_G():
    click_row_3_G.click += 1
    colorLen = len(click_row_3_G.colors)
    G_bingo_row_3.config(bg=click_row_3_G.colors[click_row_3_G.click % colorLen])


click_row_3_G.click = 0
click_row_3_G.colors = ["#F96815", "#B900ff"]


def click_row_3_O():
    click_row_3_O.click += 1
    colorLen = len(click_row_3_O.colors)
    O_bingo_row_3.config(bg=click_row_3_O.colors[click_row_3_O.click % colorLen])


click_row_3_O.click = 0
click_row_3_O.colors = ["#00FF33", "#B900ff"]


def click_row_4_B():
    click_row_4_B.click += 1
    colorLen = len(click_row_4_B.colors)
    B_bingo_row_4.config(bg=click_row_4_B.colors[click_row_4_B.click % colorLen])


click_row_4_B.click = 0
click_row_4_B.colors = ["#00ccff", "#B900ff"]


def click_row_4_I():
    click_row_4_I.click += 1
    colorLen = len(click_row_4_B.colors)
    I_bingo_row_4.config(bg=click_row_4_I.colors[click_row_4_I.click % colorLen])


click_row_4_I.click = 0
click_row_4_I.colors = ["#FF0000", "#B900ff"]


def click_row_4_N():
    click_row_4_N.click += 1
    colorLen = len(click_row_4_N.colors)
    N_bingo_row_4.config(bg=click_row_4_N.colors[click_row_4_N.click % colorLen])


click_row_4_N.click = 0
click_row_4_N.colors = ["#E2DF00", "#B900ff"]


def click_row_4_G():
    click_row_4_G.click += 1
    colorLen = len(click_row_4_G.colors)
    G_bingo_row_4.config(bg=click_row_4_G.colors[click_row_4_G.click % colorLen])


click_row_4_G.click = 0
click_row_4_G.colors = ["#F96815", "#B900ff"]


def click_row_4_O():
    click_row_4_O.click += 1
    colorLen = len(click_row_4_O.colors)
    O_bingo_row_4.config(bg=click_row_4_O.colors[click_row_4_O.click % colorLen])


click_row_4_O.click = 0
click_row_4_O.colors = ["#00FF33", "#B900ff"]


def click_row_5_B():
    click_row_5_B.click += 1
    colorLen = len(click_row_5_B.colors)
    B_bingo_row_5.config(bg=click_row_5_B.colors[click_row_5_B.click % colorLen])


click_row_5_B.click = 0
click_row_5_B.colors = ["#00ccff", "#B900ff"]


def click_row_5_I():
    click_row_5_I.click += 1
    colorLen = len(click_row_5_B.colors)
    I_bingo_row_5.config(bg=click_row_5_I.colors[click_row_5_I.click % colorLen])


click_row_5_I.click = 0
click_row_5_I.colors = ["#FF0000", "#B900ff"]


def click_row_5_N():
    click_row_5_N.click += 1
    colorLen = len(click_row_1_N.colors)
    N_bingo_row_5.config(bg=click_row_5_N.colors[click_row_5_N.click % colorLen])


click_row_5_N.click = 0
click_row_5_N.colors = ["#E2DF00", "#B900ff"]


def click_row_5_G():
    click_row_5_G.click += 1
    colorLen = len(click_row_1_G.colors)
    G_bingo_row_5.config(bg=click_row_5_G.colors[click_row_5_G.click % colorLen])


click_row_5_G.click = 0
click_row_5_G.colors = ["#F96815", "#B900ff"]


def click_row_5_O():
    click_row_5_O.click += 1
    colorLen = len(click_row_5_O.colors)
    O_bingo_row_5.config(bg=click_row_5_O.colors[click_row_5_O.click % colorLen])


click_row_5_O.click = 0
click_row_5_O.colors = ["#00FF33", "#B900ff"]

# #Player card maker: ###NEW
def draw_B_numbers_row_2(numbers_for_B_list_out_1):
    row_2_B_number = random.choice(numbers_for_B_list_out_1)
    # takes out drawing number from the list
    take_out_of_list_B = numbers_for_B_list_out_1.index(row_2_B_number)
    numbers_for_B_list_out_1.pop(take_out_of_list_B)
    # numbers_for_B_list_out_2 = numbers_for_B_list_out_1
    # draw_B_numbers_row_3(numbers_for_B_list)
    return row_2_B_number


def draw_B_numbers_row_1():
    numbers_for_B_list = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
    ]
    row_1_B_number = random.choice(numbers_for_B_list)
    # takes out drawing number from the list
    take_out_of_list_B = numbers_for_B_list.index(row_1_B_number)
    numbers_for_B_list.pop(take_out_of_list_B)
    print("first: " + row_1_B_number)  ### for testing
    print(numbers_for_B_list)  ### for tetsing
    row_2_B_number = draw_B_numbers_row_2(numbers_for_B_list)  #### needed???
    numbers_for_B_list_out_1 = numbers_for_B_list
    return row_1_B_number, numbers_for_B_list_out_1


row_1_B_number, numbers_for_B_list_out_1 = draw_B_numbers_row_1()
row_2_B_number = draw_B_numbers_row_2(numbers_for_B_list_out_1)
# BINGO row 1
B_bingo_row_1 = Button(
    root,
    text=row_1_B_number,
    bg=click_row_1_B.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_1_B,
)
I_bingo_row_1 = Button(
    root,
    text="I",
    bg=click_row_1_I.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_1_I,
)
N_bingo_row_1 = Button(
    root,
    text="N",
    bg=click_row_1_N.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_1_N,
)
G_bingo_row_1 = Button(
    root,
    text="G",
    bg=click_row_1_G.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_1_G,
)
O_bingo_row_1 = Button(
    root,
    text="O",
    bg=click_row_1_O.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_1_O,
)
# BINGO row 1 positions
B_bingo_row_1.grid(row=9, column=1, sticky="nsew")
I_bingo_row_1.grid(row=9, column=2, sticky="nsew")
N_bingo_row_1.grid(row=9, column=3, sticky="nsew")
G_bingo_row_1.grid(row=9, column=4, sticky="nsew")
O_bingo_row_1.grid(row=9, column=5, sticky="nsew")

# Bots's BINGO row 1
B_bingo_row_1_bot = Button(root, text="B", bg="#00CCFF", font=("Helvetica", 20))
I_bingo_row_1_bot = Button(root, text="I", bg="#FF0000", font=("Helvetica", 20))
N_bingo_row_1_bot = Button(root, text="N", bg="#E2DF00", font=("Helvetica", 20))
G_bingo_row_1_bot = Button(root, text="G", bg="#F96815", font=("Helvetica", 20))
O_bingo_row_1_bot = Button(root, text="O", bg="#00FF33", font=("Helvetica", 20))
# Bots's BINGO row 1 positions
B_bingo_row_1_bot.grid(row=9, column=6, sticky="nsew")
I_bingo_row_1_bot.grid(row=9, column=7, sticky="nsew")
N_bingo_row_1_bot.grid(row=9, column=8, sticky="nsew")
G_bingo_row_1_bot.grid(row=9, column=9, sticky="nsew")
O_bingo_row_1_bot.grid(row=9, column=10, sticky="nsew")

B_bingo_row_2 = Button(
    root,
    text=row_2_B_number,
    bg=click_row_2_B.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_2_B,
)
I_bingo_row_2 = Button(
    root,
    text="I",
    bg=click_row_2_I.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_2_I,
)
N_bingo_row_2 = Button(
    root,
    text="N",
    bg=click_row_2_N.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_2_N,
)
G_bingo_row_2 = Button(
    root,
    text="G",
    bg=click_row_2_G.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_2_G,
)
O_bingo_row_2 = Button(
    root,
    text="O",
    bg=click_row_2_O.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_2_O,
)

# BINGO row 2 positions
B_bingo_row_2.grid(row=10, column=1, sticky="nsew")
I_bingo_row_2.grid(row=10, column=2, sticky="nsew")
N_bingo_row_2.grid(row=10, column=3, sticky="nsew")
G_bingo_row_2.grid(row=10, column=4, sticky="nsew")
O_bingo_row_2.grid(row=10, column=5, sticky="nsew")

# Bots's BINGO row 2
B_bingo_row_2_bot = Button(root, text="B", bg="#00CCFF", font=("Helvetica", 20))
I_bingo_row_2_bot = Button(root, text="I", bg="#FF0000", font=("Helvetica", 20))
N_bingo_row_2_bot = Button(root, text="N", bg="#E2DF00", font=("Helvetica", 20))
G_bingo_row_2_bot = Button(root, text="G", bg="#F96815", font=("Helvetica", 20))
O_bingo_row_2_bot = Button(root, text="O", bg="#00FF33", font=("Helvetica", 20))
# Bots's BINGO row 2 positions
B_bingo_row_2_bot.grid(row=10, column=6, sticky="nsew")
I_bingo_row_2_bot.grid(row=10, column=7, sticky="nsew")
N_bingo_row_2_bot.grid(row=10, column=8, sticky="nsew")
G_bingo_row_2_bot.grid(row=10, column=9, sticky="nsew")
O_bingo_row_2_bot.grid(row=10, column=10, sticky="nsew")


# STAR image formant
# call image b4 resize
original_star = Image.open("STAR.png")
# resizing image
resized = original_star.resize((95, 52), Image.ANTIALIAS)  # resize(sides, height)
star = ImageTk.PhotoImage(resized)

B_bingo_row_3 = Button(
    root,
    text="B1",
    bg=click_row_3_B.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_3_B,
)
I_bingo_row_3 = Button(
    root,
    text="I",
    bg=click_row_3_I.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_3_I,
)
N_bingo = Label(root, image=star)  # FREE SPACE

G_bingo_row_3 = Button(
    root,
    text="G",
    bg=click_row_3_G.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_3_G,
)
O_bingo_row_3 = Button(
    root,
    text="O",
    bg=click_row_3_O.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_3_O,
)

# BINGO row 3 positions
B_bingo_row_3.grid(row=11, column=1, sticky="nsew")
I_bingo_row_3.grid(row=11, column=2, sticky="nsew")
N_bingo.grid(row=11, column=3, sticky="nsew")
G_bingo_row_3.grid(row=11, column=4, sticky="nsew")
O_bingo_row_3.grid(row=11, column=5, sticky="nsew")

# Bots's BINGO row 3
B_bingo_row_3_bot = Button(root, text="B", bg="#00CCFF", font=("Helvetica", 20))
I_bingo_row_3_bot = Button(root, text="I", bg="#FF0000", font=("Helvetica", 20))
N_bingo = Label(root, image=star)  # FREE SPACE
G_bingo_row_3_bot = Button(root, text="G", bg="#F96815", font=("Helvetica", 20))
O_bingo_row_3_bot = Button(root, text="O", bg="#00FF33", font=("Helvetica", 20))
# Bots's BINGO row 3 positions
B_bingo_row_3_bot.grid(row=11, column=6, sticky="nsew")
I_bingo_row_3_bot.grid(row=11, column=7, sticky="nsew")
N_bingo.grid(row=11, column=8, sticky="nsew")
G_bingo_row_3_bot.grid(row=11, column=9, sticky="nsew")
O_bingo_row_3_bot.grid(row=11, column=10, sticky="nsew")

# BINGO row 4
B_bingo_row_4 = Button(
    root,
    text="B1",
    bg=click_row_4_B.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_4_B,
)
I_bingo_row_4 = Button(
    root,
    text="I",
    bg=click_row_4_I.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_4_I,
)
N_bingo_row_4 = Button(
    root,
    text="N",
    bg=click_row_4_N.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_4_N,
)
G_bingo_row_4 = Button(
    root,
    text="G",
    bg=click_row_4_G.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_4_G,
)
O_bingo_row_4 = Button(
    root,
    text="O",
    bg=click_row_4_O.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_4_O,
)

# BINGO row 4 positions
B_bingo_row_4.grid(row=12, column=1, sticky="nsew")
I_bingo_row_4.grid(row=12, column=2, sticky="nsew")
N_bingo_row_4.grid(row=12, column=3, sticky="nsew")
G_bingo_row_4.grid(row=12, column=4, sticky="nsew")
O_bingo_row_4.grid(row=12, column=5, sticky="nsew")

# Bots's BINGO row 4
B_bingo_row_4_bot = Button(root, text="B", bg="#00CCFF", font=("Helvetica", 20))
I_bingo_row_4_bot = Button(root, text="I", bg="#FF0000", font=("Helvetica", 20))
N_bingo_row_4_bot = Button(root, text="N", bg="#E2DF00", font=("Helvetica", 20))
G_bingo_row_4_bot = Button(root, text="G", bg="#F96815", font=("Helvetica", 20))
O_bingo_row_4_bot = Button(root, text="O", bg="#00FF33", font=("Helvetica", 20))
# Bots's BINGO row 4 positions
B_bingo_row_4_bot.grid(row=12, column=6, sticky="nsew")
I_bingo_row_4_bot.grid(row=12, column=7, sticky="nsew")
N_bingo_row_4_bot.grid(row=12, column=8, sticky="nsew")
G_bingo_row_4_bot.grid(row=12, column=9, sticky="nsew")
O_bingo_row_4_bot.grid(row=12, column=10, sticky="nsew")

# BINGO row 5
B_bingo_row_5 = Button(
    root,
    text="B1",
    bg=click_row_5_B.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_5_B,
)
I_bingo_row_5 = Button(
    root,
    text="I",
    bg=click_row_5_I.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_5_I,
)
N_bingo_row_5 = Button(
    root,
    text="N",
    bg=click_row_5_N.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_5_N,
)
G_bingo_row_5 = Button(
    root,
    text="G",
    bg=click_row_5_G.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_5_G,
)
O_bingo_row_5 = Button(
    root,
    text="O",
    bg=click_row_5_O.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_5_O,
)
# BINGO row 5 positions
B_bingo_row_5.grid(row=13, column=1, sticky="nsew")
I_bingo_row_5.grid(row=13, column=2, sticky="nsew")
N_bingo_row_5.grid(row=13, column=3, sticky="nsew")
G_bingo_row_5.grid(row=13, column=4, sticky="nsew")
O_bingo_row_5.grid(row=13, column=5, sticky="nsew")

# Bots's BINGO row 5
B_bingo_row_5_bot = Button(root, text="B", bg="#00CCFF", font=("Helvetica", 20))
I_bingo_row_5_bot = Button(root, text="I", bg="#FF0000", font=("Helvetica", 20))
N_bingo_row_5_bot = Button(root, text="N", bg="#E2DF00", font=("Helvetica", 20))
G_bingo_row_5_bot = Button(root, text="G", bg="#F96815", font=("Helvetica", 20))
O_bingo_row_5_bot = Button(root, text="O", bg="#00FF33", font=("Helvetica", 20))
# Bots's BINGO row 5 positions
B_bingo_row_5_bot.grid(row=13, column=6, sticky="nsew")
I_bingo_row_5_bot.grid(row=13, column=7, sticky="nsew")
N_bingo_row_5_bot.grid(row=13, column=8, sticky="nsew")
G_bingo_row_5_bot.grid(row=13, column=9, sticky="nsew")
O_bingo_row_5_bot.grid(row=13, column=10, sticky="nsew")

# last row
Bingo_button = Button(root, text="BINGO!", bg="#B900FF", font=("Helvetica", 25))
blank = Label(root, bg="#737373")
New_card = Button(root, text="New Card", bg="#29EFD1", font=("Helvetica", 20))
New_game = Button(root, text="New Game", bg="#FF4646", font=("Helvetica", 20))
pause_play = Button(root, text="Pause/Play", bg="#96FF50", font=("Helvetica", 20))

# last row positions # columnspan = 5
Bingo_button.grid(row=14, column=1, columnspan=3, sticky="nsew")
blank.grid(row=14, column=4, columnspan=1, sticky="nsew")
New_card.grid(row=14, column=5, columnspan=2, sticky="nsew")
New_game.grid(row=14, column=7, columnspan=2, sticky="nsew")
pause_play.grid(row=14, column=9, columnspan=2, sticky="nsew")


root.mainloop()
