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


class window_functions:
    # Center window
    app_width = 1015
    app_height = 590
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (app_width / 2)
    y_coordinate = (screen_height / 2) - (app_height / 2)
    root.geometry(f"{app_width}x{app_height}+{int(x_coordinate)}+{int(y_coordinate)}")


# opens png and resizes for use
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

### sorts list for B:, I:, N:, G:, O:, in ascending order
def sort_string(string):
    sorted_list = []
    now_str_is_a_list = string.split()
    for e in now_str_is_a_list:
        e = int(e)
        sorted_list.append(e)
        sorted_list.sort()
        string = " ".join([str(element) for element in sorted_list])
    return string


def bingo_ball_color(
    drawn_bingo_number,
    B_list_drawn_str,
    I_list_drawn_str,
    N_list_drawn_str,
    G_list_drawn_str,
    O_list_drawn_str,
):
    if drawn_bingo_number.startswith("B"):
        B_list_drawn_list = []
        bingo_ball.config(image=resized_B_ball)
        B_list_drawn_str = B_list_drawn_str + " " + drawn_bingo_number[2:]
        B_list_drawn_str = sort_string(B_list_drawn_str)
        B_list_drawn.config(
            text="B: " + B_list_drawn_str,
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
        I_list_drawn_str = sort_string(I_list_drawn_str)
        I_list_drawn.config(
            text="I: " + I_list_drawn_str,
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
        N_list_drawn_str = sort_string(N_list_drawn_str)
        N_list_drawn.config(
            text="N: " + N_list_drawn_str,
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
        G_list_drawn_str = sort_string(G_list_drawn_str)
        G_list_drawn.config(
            text="G: " + G_list_drawn_str,
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
        O_list_drawn_str = sort_string(O_list_drawn_str)
        O_list_drawn.config(
            text="O: " + O_list_drawn_str,
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


B_list_drawn_str = ""
B_list_drawn = Label(
    root,
    text="B:" + B_list_drawn_str,
    bg="#00CCFF",
    font=("Helvetica", 15),
    padx=2,
    pady=4,
)
B_list_drawn.grid(row=1, column=5, columnspan=6, rowspan=1, sticky="nsew")

I_list_drawn_str = ""
I_list_drawn = Label(
    root,
    text="I:" + I_list_drawn_str,
    bg="#FF0000",
    font=("Helvetica", 15),
    padx=2,
    pady=4,
)
I_list_drawn.grid(row=2, column=5, columnspan=6, rowspan=1, sticky="nsew")

N_list_drawn_str = ""
N_list_drawn = Label(
    root,
    text="N:" + N_list_drawn_str,
    bg="#E2DF00",
    font=("Helvetica", 15),
    padx=2,
    pady=4,
)
N_list_drawn.grid(row=3, column=5, columnspan=6, rowspan=1, sticky="nsew")

G_list_drawn_str = ""
G_list_drawn = Label(
    root,
    text="G:" + G_list_drawn_str,
    bg="#F96815",
    font=("Helvetica", 15),
    padx=2,
    pady=4,
)
G_list_drawn.grid(row=4, column=5, columnspan=6, rowspan=1, sticky="nsew")

O_list_drawn_str = ""
O_list_drawn = Label(
    root,
    text="O:" + O_list_drawn_str,
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

# makes list for all bingo number
bingo_numbers = []
bingo_numbers_int = [i for i in range(1, 76)]
for e in bingo_numbers_int:
    if e <= 15:
        b_string = "B "
        e = str(e)
        b_string = b_string + e
        bingo_numbers.append(b_string)
    elif e <= 30:
        I_string = "I "
        e = str(e)
        I_string = I_string + e
        bingo_numbers.append(I_string)
    elif e <= 45:
        N_string = "N "
        e = str(e)
        N_string = N_string + e
        bingo_numbers.append(N_string)
    elif e <= 60:
        G_string = "G "
        e = str(e)
        G_string = G_string + e
        bingo_numbers.append(G_string)
    elif e <= 75:
        O_string = "O "
        e = str(e)
        O_string = O_string + e
        bingo_numbers.append(O_string)


update_drawn_ball(
    bingo_numbers,
    B_list_drawn_str,
    I_list_drawn_str,
    N_list_drawn_str,
    G_list_drawn_str,
    O_list_drawn_str,
)

flag = True
holder_for_time = 6
# timer for next ball
def update_timer_countdown(n):  ###mark
    global flag
    if flag == True and n != "1":
        n = int(n)
        n -= 1
        n = str(n)
        timer.config(
            text="Next draw in:" + n + "s", padx=5, pady=45, font=("Helvetica", 17)
        )
        return timer.after(1000, update_timer_countdown, n)
    elif flag == True and n == "1":
        return update_timer_countdown(6)
    elif flag == False:
        global holder_for_time
        holder_for_time = n


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

# Buttons Clicks all
# player click buttons
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


bot_row_1_B_number = ""
bot_row_2_B_number = ""
bot_row_3_B_number = ""
bot_row_4_B_number = ""
bot_row_5_B_number = ""

bot_row_1_I_number = ""
bot_row_2_I_number = ""
bot_row_3_I_number = ""
bot_row_4_I_number = ""
bot_row_5_I_number = ""

bot_row_1_N_number = ""
bot_row_2_N_number = ""
bot_row_3_N_number = ""
bot_row_4_N_number = ""
bot_row_5_N_number = ""

bot_row_1_G_number = ""
bot_row_2_G_number = ""
bot_row_3_G_number = ""
bot_row_4_G_number = ""
bot_row_5_G_number = ""

bot_row_1_O_number = ""
bot_row_2_O_number = ""
bot_row_3_O_number = ""
bot_row_4_O_number = ""
bot_row_5_O_number = ""

# player strings for cards empty
row_1_B_number = ""
row_2_B_number = ""
row_3_B_number = ""
row_4_B_number = ""
row_5_B_number = ""

row_1_I_number = ""
row_2_I_number = ""
row_3_I_number = ""
row_4_I_number = ""
row_5_I_number = ""

row_1_N_number = ""
row_2_N_number = ""
row_3_N_number = ""
row_4_N_number = ""
row_5_N_number = ""

row_1_G_number = ""
row_2_G_number = ""
row_3_G_number = ""
row_4_G_number = ""
row_5_G_number = ""

row_1_O_number = ""
row_2_O_number = ""
row_3_O_number = ""
row_4_O_number = ""
row_5_O_number = ""


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
    text=row_1_I_number,
    bg=click_row_1_I.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_1_I,
)
N_bingo_row_1 = Button(
    root,
    text=row_1_N_number,
    bg=click_row_1_N.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_1_N,
)
G_bingo_row_1 = Button(
    root,
    text=row_1_G_number,
    bg=click_row_1_G.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_1_G,
)
O_bingo_row_1 = Button(
    root,
    text=row_1_O_number,
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
B_bingo_row_1_bot = Label(
    root, text=bot_row_1_B_number, bg="#00CCFF", font=("Helvetica", 20)
)
I_bingo_row_1_bot = Label(
    root, text=bot_row_1_I_number, bg="#FF0000", font=("Helvetica", 20)
)
N_bingo_row_1_bot = Label(
    root, text=bot_row_1_N_number, bg="#E2DF00", font=("Helvetica", 20)
)
G_bingo_row_1_bot = Label(
    root, text=bot_row_1_G_number, bg="#F96815", font=("Helvetica", 20)
)
O_bingo_row_1_bot = Label(
    root, text=bot_row_1_O_number, bg="#00FF33", font=("Helvetica", 20)
)
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
    text=row_2_I_number,
    bg=click_row_2_I.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_2_I,
)
N_bingo_row_2 = Button(
    root,
    text=row_2_N_number,
    bg=click_row_2_N.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_2_N,
)
G_bingo_row_2 = Button(
    root,
    text=row_2_G_number,
    bg=click_row_2_G.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_2_G,
)
O_bingo_row_2 = Button(
    root,
    text=row_2_O_number,
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
B_bingo_row_2_bot = Label(
    root, text=bot_row_2_B_number, bg="#00CCFF", font=("Helvetica", 20)
)
I_bingo_row_2_bot = Label(
    root, text=bot_row_2_I_number, bg="#FF0000", font=("Helvetica", 20)
)
N_bingo_row_2_bot = Label(
    root, text=bot_row_2_N_number, bg="#E2DF00", font=("Helvetica", 20)
)
G_bingo_row_2_bot = Label(
    root, text=bot_row_2_G_number, bg="#F96815", font=("Helvetica", 20)
)
O_bingo_row_2_bot = Label(
    root, text=bot_row_2_O_number, bg="#00FF33", font=("Helvetica", 20)
)
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
    text=row_3_B_number,
    bg=click_row_3_B.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_3_B,
)
I_bingo_row_3 = Button(
    root,
    text=row_3_I_number,
    bg=click_row_3_I.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_3_I,
)
N_bingo = Label(root, image=star)  # FREE SPACE

G_bingo_row_3 = Button(
    root,
    text=row_3_G_number,
    bg=click_row_3_G.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_3_G,
)
O_bingo_row_3 = Button(
    root,
    text=row_3_O_number,
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
B_bingo_row_3_bot = Label(
    root, text=bot_row_3_B_number, bg="#00CCFF", font=("Helvetica", 20)
)
I_bingo_row_3_bot = Label(
    root, text=bot_row_3_I_number, bg="#FF0000", font=("Helvetica", 20)
)
N_bingo = Label(root, image=star)  # FREE SPACE
G_bingo_row_3_bot = Label(
    root, text=bot_row_3_G_number, bg="#F96815", font=("Helvetica", 20)
)
O_bingo_row_3_bot = Label(
    root, text=bot_row_3_O_number, bg="#00FF33", font=("Helvetica", 20)
)
# Bots's BINGO row 3 positions
B_bingo_row_3_bot.grid(row=11, column=6, sticky="nsew")
I_bingo_row_3_bot.grid(row=11, column=7, sticky="nsew")
N_bingo.grid(row=11, column=8, sticky="nsew")
G_bingo_row_3_bot.grid(row=11, column=9, sticky="nsew")
O_bingo_row_3_bot.grid(row=11, column=10, sticky="nsew")

# BINGO row 4
B_bingo_row_4 = Button(
    root,
    text=row_4_B_number,
    bg=click_row_4_B.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_4_B,
)
I_bingo_row_4 = Button(
    root,
    text=row_4_I_number,
    bg=click_row_4_I.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_4_I,
)
N_bingo_row_4 = Button(
    root,
    text=row_4_N_number,
    bg=click_row_4_N.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_4_N,
)
G_bingo_row_4 = Button(
    root,
    text=row_4_G_number,
    bg=click_row_4_G.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_4_G,
)
O_bingo_row_4 = Button(
    root,
    text=row_4_O_number,
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
B_bingo_row_4_bot = Label(
    root, text=bot_row_4_B_number, bg="#00CCFF", font=("Helvetica", 20)
)
I_bingo_row_4_bot = Label(
    root, text=bot_row_4_I_number, bg="#FF0000", font=("Helvetica", 20)
)
N_bingo_row_4_bot = Label(
    root, text=bot_row_4_N_number, bg="#E2DF00", font=("Helvetica", 20)
)
G_bingo_row_4_bot = Label(
    root, text=bot_row_4_G_number, bg="#F96815", font=("Helvetica", 20)
)
O_bingo_row_4_bot = Label(
    root, text=bot_row_4_O_number, bg="#00FF33", font=("Helvetica", 20)
)
# Bots's BINGO row 4 positions
B_bingo_row_4_bot.grid(row=12, column=6, sticky="nsew")
I_bingo_row_4_bot.grid(row=12, column=7, sticky="nsew")
N_bingo_row_4_bot.grid(row=12, column=8, sticky="nsew")
G_bingo_row_4_bot.grid(row=12, column=9, sticky="nsew")
O_bingo_row_4_bot.grid(row=12, column=10, sticky="nsew")

# BINGO row 5
B_bingo_row_5 = Button(
    root,
    text=row_5_B_number,
    bg=click_row_5_B.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_5_B,
)
I_bingo_row_5 = Button(
    root,
    text=row_5_I_number,
    bg=click_row_5_I.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_5_I,
)
N_bingo_row_5 = Button(
    root,
    text=row_5_N_number,
    bg=click_row_5_N.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_5_N,
)
G_bingo_row_5 = Button(
    root,
    text=row_5_G_number,
    bg=click_row_5_G.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_5_G,
)
O_bingo_row_5 = Button(
    root,
    text=row_5_O_number,
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
B_bingo_row_5_bot = Label(
    root, text=bot_row_5_B_number, bg="#00CCFF", font=("Helvetica", 20)
)
I_bingo_row_5_bot = Label(
    root, text=bot_row_5_I_number, bg="#FF0000", font=("Helvetica", 20)
)
N_bingo_row_5_bot = Label(
    root, text=bot_row_5_N_number, bg="#E2DF00", font=("Helvetica", 20)
)
G_bingo_row_5_bot = Label(
    root, text=bot_row_5_G_number, bg="#F96815", font=("Helvetica", 20)
)
O_bingo_row_5_bot = Label(
    root, text=bot_row_5_O_number, bg="#00FF33", font=("Helvetica", 20)
)
# Bots's BINGO row 5 positions
B_bingo_row_5_bot.grid(row=13, column=6, sticky="nsew")
I_bingo_row_5_bot.grid(row=13, column=7, sticky="nsew")
N_bingo_row_5_bot.grid(row=13, column=8, sticky="nsew")
G_bingo_row_5_bot.grid(row=13, column=9, sticky="nsew")
O_bingo_row_5_bot.grid(row=13, column=10, sticky="nsew")


# Player card maker:
# player card maker for B row:
def draw_B_numbers_row_5(numbers_for_B_list_out_4):
    row_5_B_number = random.choice(numbers_for_B_list_out_4)
    # takes out drawing number from the list
    take_out_of_list_B = numbers_for_B_list_out_4.index(row_5_B_number)
    numbers_for_B_list_out_4.pop(take_out_of_list_B)
    B_bingo_row_5.configure(
        text=row_5_B_number,
        bg=click_row_5_B.colors[0],
        font=("Helvetica", 20),
        command=click_row_5_B,
    )


def draw_B_numbers_row_4(numbers_for_B_list_out_3):
    row_4_B_number = random.choice(numbers_for_B_list_out_3)
    # takes out drawing number from the list
    take_out_of_list_B = numbers_for_B_list_out_3.index(row_4_B_number)
    numbers_for_B_list_out_3.pop(take_out_of_list_B)
    numbers_for_B_list_out_4 = numbers_for_B_list_out_3
    B_bingo_row_4.configure(
        text=row_4_B_number,
        bg=click_row_4_B.colors[0],
        font=("Helvetica", 20),
        command=click_row_4_B,
    )
    return draw_B_numbers_row_5(numbers_for_B_list_out_4)


def draw_B_numbers_row_3(numbers_for_B_list_out_2):
    row_3_B_number = random.choice(numbers_for_B_list_out_2)
    # takes out drawing number from the list
    take_out_of_list_B = numbers_for_B_list_out_2.index(row_3_B_number)
    numbers_for_B_list_out_2.pop(take_out_of_list_B)
    numbers_for_B_list_out_3 = numbers_for_B_list_out_2
    B_bingo_row_3.configure(
        text=row_3_B_number,
        bg=click_row_3_B.colors[0],
        font=("Helvetica", 20),
        command=click_row_3_B,
    )
    return draw_B_numbers_row_4(numbers_for_B_list_out_3)


def draw_B_numbers_row_2(numbers_for_B_list_out_1):
    row_2_B_number = random.choice(numbers_for_B_list_out_1)
    # takes out drawing number from the list
    take_out_of_list_B = numbers_for_B_list_out_1.index(row_2_B_number)
    numbers_for_B_list_out_1.pop(take_out_of_list_B)
    numbers_for_B_list_out_2 = numbers_for_B_list_out_1
    B_bingo_row_2.configure(
        text=row_2_B_number,
        bg=click_row_2_B.colors[0],
        font=("Helvetica", 20),
        command=click_row_2_B,
    )
    return draw_B_numbers_row_3(numbers_for_B_list_out_2)


def draw_B_numbers_row_1():
    numbers_for_B_list = []
    numbers_for_B_list_int = [i for i in range(1, 16)]
    for e in numbers_for_B_list_int:
        e = str(e)
        numbers_for_B_list.append(e)
    row_1_B_number = random.choice(numbers_for_B_list)
    # takes out drawing number from the list
    take_out_of_list_B = numbers_for_B_list.index(row_1_B_number)
    numbers_for_B_list.pop(take_out_of_list_B)
    numbers_for_B_list_out_1 = numbers_for_B_list
    B_bingo_row_1.configure(
        text=row_1_B_number,
        bg=click_row_1_B.colors[0],
        font=("Helvetica", 20),
        command=click_row_1_B,
    )
    return draw_B_numbers_row_2(numbers_for_B_list_out_1)


# player card maker for I row:
def draw_I_numbers_row_5(numbers_for_I_list_out_4):
    row_5_I_number = random.choice(numbers_for_I_list_out_4)
    # takes out drawing number from the list
    take_out_of_list_I = numbers_for_I_list_out_4.index(row_5_I_number)
    numbers_for_I_list_out_4.pop(take_out_of_list_I)
    I_bingo_row_5.configure(
        text=row_5_I_number,
        bg=click_row_5_I.colors[0],
        font=("Helvetica", 20),
        command=click_row_5_I,
    )


def draw_I_numbers_row_4(numbers_for_I_list_out_3):
    row_4_I_number = random.choice(numbers_for_I_list_out_3)
    # takes out drawing number from the list
    take_out_of_list_I = numbers_for_I_list_out_3.index(row_4_I_number)
    numbers_for_I_list_out_3.pop(take_out_of_list_I)
    numbers_for_I_list_out_4 = numbers_for_I_list_out_3
    I_bingo_row_4.configure(
        text=row_4_I_number,
        bg=click_row_4_I.colors[0],
        font=("Helvetica", 20),
        command=click_row_4_I,
    )
    return draw_I_numbers_row_5(numbers_for_I_list_out_4)


def draw_I_numbers_row_3(numbers_for_I_list_out_2):
    row_3_I_number = random.choice(numbers_for_I_list_out_2)
    # takes out drawing number from the list
    take_out_of_list_I = numbers_for_I_list_out_2.index(row_3_I_number)
    numbers_for_I_list_out_2.pop(take_out_of_list_I)
    numbers_for_I_list_out_3 = numbers_for_I_list_out_2
    I_bingo_row_3.configure(
        text=row_3_I_number,
        bg=click_row_3_I.colors[0],
        font=("Helvetica", 20),
        command=click_row_3_I,
    )
    return draw_I_numbers_row_4(numbers_for_I_list_out_3)


def draw_I_numbers_row_2(numbers_for_I_list_out_1):
    row_2_I_number = random.choice(numbers_for_I_list_out_1)
    # takes out drawing number from the list
    take_out_of_list_I = numbers_for_I_list_out_1.index(row_2_I_number)
    numbers_for_I_list_out_1.pop(take_out_of_list_I)
    numbers_for_I_list_out_2 = numbers_for_I_list_out_1
    I_bingo_row_2.configure(
        text=row_2_I_number,
        bg=click_row_2_I.colors[0],
        font=("Helvetica", 20),
        command=click_row_2_I,
    )
    return draw_I_numbers_row_3(numbers_for_I_list_out_2)


def draw_I_numbers_row_1():
    numbers_for_I_list = []
    numbers_for_I_list_int = [i for i in range(16, 31)]
    for e in numbers_for_I_list_int:
        e = str(e)
        numbers_for_I_list.append(e)
    row_1_I_number = random.choice(numbers_for_I_list)
    # takes out drawing number from the list
    take_out_of_list_I = numbers_for_I_list.index(row_1_I_number)
    numbers_for_I_list.pop(take_out_of_list_I)
    numbers_for_I_list_out_1 = numbers_for_I_list
    I_bingo_row_1.configure(
        text=row_1_I_number,
        bg=click_row_1_I.colors[0],
        font=("Helvetica", 20),
        command=click_row_1_I,
    )
    return draw_I_numbers_row_2(numbers_for_I_list_out_1)


# player card maker for N row:
def draw_N_numbers_row_5(numbers_for_N_list_out_4):
    row_5_N_number = random.choice(numbers_for_N_list_out_4)
    # takes out drawing number from the list
    take_out_of_list_N = numbers_for_N_list_out_4.index(row_5_N_number)
    numbers_for_N_list_out_4.pop(take_out_of_list_N)
    N_bingo_row_5.configure(
        text=row_5_N_number,
        bg=click_row_5_N.colors[0],
        font=("Helvetica", 20),
        command=click_row_5_N,
    )


def draw_N_numbers_row_4(numbers_for_N_list_out_3):
    row_4_N_number = random.choice(numbers_for_N_list_out_3)
    # takes out drawing number from the list
    take_out_of_list_N = numbers_for_N_list_out_3.index(row_4_N_number)
    numbers_for_N_list_out_3.pop(take_out_of_list_N)
    numbers_for_N_list_out_4 = numbers_for_N_list_out_3
    N_bingo_row_4.configure(
        text=row_4_N_number,
        bg=click_row_4_N.colors[0],
        font=("Helvetica", 20),
        command=click_row_4_N,
    )
    return draw_N_numbers_row_5(numbers_for_N_list_out_4)


def draw_N_numbers_row_3(numbers_for_N_list_out_2):
    row_3_N_number = random.choice(numbers_for_N_list_out_2)
    # takes out drawing number from the list
    take_out_of_list_N = numbers_for_N_list_out_2.index(row_3_N_number)
    numbers_for_N_list_out_2.pop(take_out_of_list_N)
    numbers_for_N_list_out_3 = numbers_for_N_list_out_2
    return draw_N_numbers_row_4(numbers_for_N_list_out_3)


def draw_N_numbers_row_2(numbers_for_N_list_out_1):
    row_2_N_number = random.choice(numbers_for_N_list_out_1)
    # takes out drawing number from the list
    take_out_of_list_I = numbers_for_N_list_out_1.index(row_2_N_number)
    numbers_for_N_list_out_1.pop(take_out_of_list_I)
    numbers_for_N_list_out_2 = numbers_for_N_list_out_1
    N_bingo_row_2.configure(
        text=row_2_N_number,
        bg=click_row_2_N.colors[0],
        font=("Helvetica", 20),
        command=click_row_2_N,
    )
    return draw_N_numbers_row_3(numbers_for_N_list_out_2)


def draw_N_numbers_row_1():
    numbers_for_N_list = []
    numbers_for_N_list_int = [i for i in range(31, 46)]
    for e in numbers_for_N_list_int:
        e = str(e)
        numbers_for_N_list.append(e)
    row_1_N_number = random.choice(numbers_for_N_list)
    # takes out drawing number from the list
    take_out_of_list_I = numbers_for_N_list.index(row_1_N_number)
    numbers_for_N_list.pop(take_out_of_list_I)
    numbers_for_N_list_out_1 = numbers_for_N_list
    N_bingo_row_1.configure(
        text=row_1_N_number,
        bg=click_row_1_N.colors[0],
        font=("Helvetica", 20),
        command=click_row_1_N,
    )
    return draw_N_numbers_row_2(numbers_for_N_list_out_1)


# player card maker for G row:
def draw_G_numbers_row_5(numbers_for_G_list_out_4):
    row_5_G_number = random.choice(numbers_for_G_list_out_4)
    # takes out drawing number from the list
    take_out_of_list_G = numbers_for_G_list_out_4.index(row_5_G_number)
    numbers_for_G_list_out_4.pop(take_out_of_list_G)
    G_bingo_row_5.configure(
        text=row_5_G_number,
        bg=click_row_5_G.colors[0],
        font=("Helvetica", 20),
        command=click_row_5_G,
    )


def draw_G_numbers_row_4(numbers_for_G_list_out_3):
    row_4_G_number = random.choice(numbers_for_G_list_out_3)
    # takes out drawing number from the list
    take_out_of_list_G = numbers_for_G_list_out_3.index(row_4_G_number)
    numbers_for_G_list_out_3.pop(take_out_of_list_G)
    numbers_for_G_list_out_4 = numbers_for_G_list_out_3
    G_bingo_row_4.configure(
        text=row_4_G_number,
        bg=click_row_4_G.colors[0],
        font=("Helvetica", 20),
        command=click_row_4_G,
    )
    return draw_G_numbers_row_5(numbers_for_G_list_out_4)


def draw_G_numbers_row_3(numbers_for_G_list_out_2):
    row_3_G_number = random.choice(numbers_for_G_list_out_2)
    # takes out drawing number from the list
    take_out_of_list_G = numbers_for_G_list_out_2.index(row_3_G_number)
    numbers_for_G_list_out_2.pop(take_out_of_list_G)
    numbers_for_G_list_out_3 = numbers_for_G_list_out_2
    G_bingo_row_3.configure(
        text=row_3_G_number,
        bg=click_row_3_G.colors[0],
        font=("Helvetica", 20),
        command=click_row_3_G,
    )
    return draw_G_numbers_row_4(numbers_for_G_list_out_3)


def draw_G_numbers_row_2(numbers_for_G_list_out_1):
    row_2_G_number = random.choice(numbers_for_G_list_out_1)
    # takes out drawing number from the list
    take_out_of_list_G = numbers_for_G_list_out_1.index(row_2_G_number)
    numbers_for_G_list_out_1.pop(take_out_of_list_G)
    numbers_for_G_list_out_2 = numbers_for_G_list_out_1
    G_bingo_row_2.configure(
        text=row_2_G_number,
        bg=click_row_2_G.colors[0],
        font=("Helvetica", 20),
        command=click_row_2_G,
    )
    return draw_G_numbers_row_3(numbers_for_G_list_out_2)


def draw_G_numbers_row_1():
    numbers_for_G_list = []
    numbers_for_G_list_int = [i for i in range(46, 61)]
    for e in numbers_for_G_list_int:
        e = str(e)
        numbers_for_G_list.append(e)
    row_1_G_number = random.choice(numbers_for_G_list)
    # takes out drawing number from the list
    take_out_of_list_I = numbers_for_G_list.index(row_1_G_number)
    numbers_for_G_list.pop(take_out_of_list_I)
    numbers_for_G_list_out_1 = numbers_for_G_list
    G_bingo_row_1.configure(
        text=row_1_G_number,
        bg=click_row_1_G.colors[0],
        font=("Helvetica", 20),
        command=click_row_1_G,
    )
    return draw_G_numbers_row_2(numbers_for_G_list_out_1)


# player card maker for O row:
def draw_O_numbers_row_5(numbers_for_O_list_out_4):
    row_5_O_number = random.choice(numbers_for_O_list_out_4)
    # takes out drawing number from the list
    take_out_of_list_O = numbers_for_O_list_out_4.index(row_5_O_number)
    numbers_for_O_list_out_4.pop(take_out_of_list_O)
    O_bingo_row_5.configure(
        text=row_5_O_number,
        bg=click_row_5_O.colors[0],
        font=("Helvetica", 20),
        command=click_row_5_O,
    )


def draw_O_numbers_row_4(numbers_for_O_list_out_3):
    row_4_O_number = random.choice(numbers_for_O_list_out_3)
    # takes out drawing number from the list
    take_out_of_list_O = numbers_for_O_list_out_3.index(row_4_O_number)
    numbers_for_O_list_out_3.pop(take_out_of_list_O)
    numbers_for_O_list_out_4 = numbers_for_O_list_out_3
    O_bingo_row_4.configure(
        text=row_4_O_number,
        bg=click_row_4_O.colors[0],
        font=("Helvetica", 20),
        command=click_row_4_O,
    )
    return draw_O_numbers_row_5(numbers_for_O_list_out_4)


def draw_O_numbers_row_3(numbers_for_O_list_out_2):
    row_3_O_number = random.choice(numbers_for_O_list_out_2)
    # takes out drawing number from the list
    take_out_of_list_O = numbers_for_O_list_out_2.index(row_3_O_number)
    numbers_for_O_list_out_2.pop(take_out_of_list_O)
    numbers_for_O_list_out_3 = numbers_for_O_list_out_2
    O_bingo_row_3.configure(
        text=row_3_O_number,
        bg=click_row_3_O.colors[0],
        font=("Helvetica", 20),
        command=click_row_3_O,
    )
    return draw_O_numbers_row_4(numbers_for_O_list_out_3)


def draw_O_numbers_row_2(numbers_for_O_list_out_1):
    row_2_O_number = random.choice(numbers_for_O_list_out_1)
    # takes out drawing number from the list
    take_out_of_list_O = numbers_for_O_list_out_1.index(row_2_O_number)
    numbers_for_O_list_out_1.pop(take_out_of_list_O)
    numbers_for_O_list_out_2 = numbers_for_O_list_out_1
    O_bingo_row_2.configure(
        text=row_2_O_number,
        bg=click_row_2_O.colors[0],
        font=("Helvetica", 20),
        command=click_row_2_O,
    )
    return draw_O_numbers_row_3(numbers_for_O_list_out_2)


def draw_O_numbers_row_1():
    numbers_for_O_list = []
    numbers_for_O_list_int = [i for i in range(61, 76)]
    for e in numbers_for_O_list_int:
        e = str(e)
        numbers_for_O_list.append(e)
    row_1_O_number = random.choice(numbers_for_O_list)
    # takes out drawing number from the list
    take_out_of_list_O = numbers_for_O_list.index(row_1_O_number)
    numbers_for_O_list.pop(take_out_of_list_O)
    numbers_for_O_list_out_1 = numbers_for_O_list
    O_bingo_row_1.configure(
        text=row_1_O_number,
        bg=click_row_1_O.colors[0],
        font=("Helvetica", 20),
        command=click_row_1_O,
    )
    return draw_O_numbers_row_2(numbers_for_O_list_out_1)


# Call functions that make player's card
draw_B_numbers_row_1()
draw_I_numbers_row_1()
draw_N_numbers_row_1()
draw_G_numbers_row_1()
draw_O_numbers_row_1()

# Bot card maker:
# Bot card maker for B row:
def bot_draw_B_numbers_row_5(bot_numbers_for_B_list_out_4):
    bot_row_5_B_number = random.choice(bot_numbers_for_B_list_out_4)
    # takes out drawing number from the list
    bot_take_out_of_list_B = bot_numbers_for_B_list_out_4.index(bot_row_5_B_number)
    bot_numbers_for_B_list_out_4.pop(bot_take_out_of_list_B)
    B_bingo_row_5_bot.configure(
        text=bot_row_5_B_number, bg="#00CCFF", font=("Helvetica", 20)
    )


def bot_draw_B_numbers_row_4(bot_numbers_for_B_list_out_3):
    bot_row_4_B_number = random.choice(bot_numbers_for_B_list_out_3)
    # takes out drawing number from the list
    bot_take_out_of_list_B = bot_numbers_for_B_list_out_3.index(bot_row_4_B_number)
    bot_numbers_for_B_list_out_3.pop(bot_take_out_of_list_B)
    bot_numbers_for_B_list_out_4 = bot_numbers_for_B_list_out_3
    B_bingo_row_4_bot.configure(
        text=bot_row_4_B_number, bg="#00CCFF", font=("Helvetica", 20)
    )
    return bot_draw_B_numbers_row_5(bot_numbers_for_B_list_out_4)


def bot_draw_B_numbers_row_3(bot_numbers_for_B_list_out_2):
    bot_row_3_B_number = random.choice(bot_numbers_for_B_list_out_2)
    # takes out drawing number from the list
    bot_take_out_of_list_B = bot_numbers_for_B_list_out_2.index(bot_row_3_B_number)
    bot_numbers_for_B_list_out_2.pop(bot_take_out_of_list_B)
    bot_numbers_for_B_list_out_3 = bot_numbers_for_B_list_out_2
    B_bingo_row_3_bot.configure(
        text=bot_row_3_B_number, bg="#00CCFF", font=("Helvetica", 20)
    )
    return bot_draw_B_numbers_row_4(bot_numbers_for_B_list_out_3)


def bot_draw_B_numbers_row_2(bot_numbers_for_B_list_out_1):
    bot_row_2_B_number = random.choice(bot_numbers_for_B_list_out_1)
    # takes out drawing number from the list
    bot_take_out_of_list_B = bot_numbers_for_B_list_out_1.index(bot_row_2_B_number)
    bot_numbers_for_B_list_out_1.pop(bot_take_out_of_list_B)
    bot_numbers_for_B_list_out_2 = bot_numbers_for_B_list_out_1
    B_bingo_row_2_bot.configure(
        text=bot_row_2_B_number, bg="#00CCFF", font=("Helvetica", 20)
    )
    return bot_draw_B_numbers_row_3(bot_numbers_for_B_list_out_2)


def bot_draw_B_numbers_row_1():
    bot_numbers_for_B_list = []
    bot_numbers_for_B_list_int = [i for i in range(1, 16)]
    for e in bot_numbers_for_B_list_int:
        e = str(e)
        bot_numbers_for_B_list.append(e)
    bot_row_1_B_number = random.choice(bot_numbers_for_B_list)
    # takes out drawing number from the list
    take_out_of_list_B = bot_numbers_for_B_list.index(bot_row_1_B_number)
    bot_numbers_for_B_list.pop(take_out_of_list_B)
    bot_numbers_for_B_list_out_1 = bot_numbers_for_B_list
    B_bingo_row_1_bot.configure(
        text=bot_row_1_B_number, bg="#00CCFF", font=("Helvetica", 20)
    )
    return bot_draw_B_numbers_row_2(bot_numbers_for_B_list_out_1)


# Bot card maker for I row:
def bot_draw_I_numbers_row_5(bot_numbers_for_I_list_out_4):
    bot_row_5_I_number = random.choice(bot_numbers_for_I_list_out_4)
    # takes out drawing number from the list
    bot_take_out_of_list_I = bot_numbers_for_I_list_out_4.index(bot_row_5_I_number)
    bot_numbers_for_I_list_out_4.pop(bot_take_out_of_list_I)
    I_bingo_row_5_bot.configure(
        text=bot_row_5_I_number, bg="#FF0000", font=("Helvetica", 20)
    )


def bot_draw_I_numbers_row_4(bot_numbers_for_I_list_out_3):
    bot_row_4_I_number = random.choice(bot_numbers_for_I_list_out_3)
    # takes out drawing number from the list
    bot_take_out_of_list_I = bot_numbers_for_I_list_out_3.index(bot_row_4_I_number)
    bot_numbers_for_I_list_out_3.pop(bot_take_out_of_list_I)
    bot_numbers_for_I_list_out_4 = bot_numbers_for_I_list_out_3
    I_bingo_row_4_bot.configure(
        text=bot_row_4_I_number, bg="#FF0000", font=("Helvetica", 20)
    )
    return bot_draw_I_numbers_row_5(bot_numbers_for_I_list_out_4)


def bot_draw_I_numbers_row_3(bot_numbers_for_I_list_out_2):
    bot_row_3_I_number = random.choice(bot_numbers_for_I_list_out_2)
    # takes out drawing number from the list
    bot_take_out_of_list_I = bot_numbers_for_I_list_out_2.index(bot_row_3_I_number)
    bot_numbers_for_I_list_out_2.pop(bot_take_out_of_list_I)
    bot_numbers_for_I_list_out_3 = bot_numbers_for_I_list_out_2
    I_bingo_row_3_bot.configure(
        text=bot_row_3_I_number, bg="#FF0000", font=("Helvetica", 20)
    )
    return bot_draw_I_numbers_row_4(bot_numbers_for_I_list_out_3)


def bot_draw_I_numbers_row_2(bot_numbers_for_I_list_out_1):
    bot_row_2_I_number = random.choice(bot_numbers_for_I_list_out_1)
    # takes out drawing number from the list
    bot_take_out_of_list_I = bot_numbers_for_I_list_out_1.index(bot_row_2_I_number)
    bot_numbers_for_I_list_out_1.pop(bot_take_out_of_list_I)
    bot_numbers_for_I_list_out_2 = bot_numbers_for_I_list_out_1
    I_bingo_row_2_bot.configure(
        text=bot_row_2_I_number, bg="#FF0000", font=("Helvetica", 20)
    )
    return bot_draw_I_numbers_row_3(bot_numbers_for_I_list_out_2)


def bot_draw_I_numbers_row_1():
    bot_numbers_for_I_list = []
    bot_numbers_for_I_list_int = [i for i in range(16, 31)]
    for e in bot_numbers_for_I_list_int:
        e = str(e)
        bot_numbers_for_I_list.append(e)
    bot_row_1_I_number = random.choice(bot_numbers_for_I_list)
    # takes out drawing number from the list
    take_out_of_list_I = bot_numbers_for_I_list.index(bot_row_1_I_number)
    bot_numbers_for_I_list.pop(take_out_of_list_I)
    bot_numbers_for_I_list_out_1 = bot_numbers_for_I_list
    I_bingo_row_1_bot.configure(
        text=bot_row_1_I_number, bg="#FF0000", font=("Helvetica", 20)
    )
    return bot_draw_I_numbers_row_2(bot_numbers_for_I_list_out_1)


#  Bot card maker for N row:
def bot_draw_N_numbers_row_5(bot_numbers_for_N_list_out_4):
    bot_row_5_N_number = random.choice(bot_numbers_for_N_list_out_4)
    # takes out drawing number from the list
    bot_take_out_of_list_N = bot_numbers_for_N_list_out_4.index(bot_row_5_N_number)
    bot_numbers_for_N_list_out_4.pop(bot_take_out_of_list_N)
    N_bingo_row_5_bot.configure(
        text=bot_row_5_N_number, bg="#E2DF00", font=("Helvetica", 20)
    )


def bot_draw_N_numbers_row_4(bot_numbers_for_N_list_out_3):
    bot_row_4_N_number = random.choice(bot_numbers_for_N_list_out_3)
    # takes out drawing number from the list
    bot_take_out_of_list_N = bot_numbers_for_N_list_out_3.index(bot_row_4_N_number)
    bot_numbers_for_N_list_out_3.pop(bot_take_out_of_list_N)
    bot_numbers_for_N_list_out_4 = bot_numbers_for_N_list_out_3
    N_bingo_row_4_bot.configure(
        text=bot_row_4_N_number, bg="#E2DF00", font=("Helvetica", 20)
    )
    return bot_draw_N_numbers_row_5(bot_numbers_for_N_list_out_4)


def bot_draw_N_numbers_row_3(bot_numbers_for_N_list_out_2):
    bot_row_3_N_number = random.choice(bot_numbers_for_N_list_out_2)
    # takes out drawing number from the list
    bot_take_out_of_list_N = bot_numbers_for_N_list_out_2.index(bot_row_3_N_number)
    bot_numbers_for_N_list_out_2.pop(bot_take_out_of_list_N)
    bot_numbers_for_N_list_out_3 = bot_numbers_for_N_list_out_2
    # no configure b/c cause free space
    return bot_draw_N_numbers_row_4(bot_numbers_for_N_list_out_3)


def bot_draw_N_numbers_row_2(bot_numbers_for_N_list_out_1):
    bot_row_2_N_number = random.choice(bot_numbers_for_N_list_out_1)
    # takes out drawing number from the list
    bot_take_out_of_list_N = bot_numbers_for_N_list_out_1.index(bot_row_2_N_number)
    bot_numbers_for_N_list_out_1.pop(bot_take_out_of_list_N)
    bot_numbers_for_N_list_out_2 = bot_numbers_for_N_list_out_1
    N_bingo_row_2_bot.configure(
        text=bot_row_2_N_number, bg="#E2DF00", font=("Helvetica", 20)
    )
    return bot_draw_N_numbers_row_3(bot_numbers_for_N_list_out_2)


def bot_draw_N_numbers_row_1():
    bot_numbers_for_N_list = []
    bot_numbers_for_N_list_int = [i for i in range(31, 46)]
    for e in bot_numbers_for_N_list_int:
        e = str(e)
        bot_numbers_for_N_list.append(e)
    bot_row_1_N_number = random.choice(bot_numbers_for_N_list)
    # takes out drawing number from the list
    take_out_of_list_N = bot_numbers_for_N_list.index(bot_row_1_N_number)
    bot_numbers_for_N_list.pop(take_out_of_list_N)
    bot_numbers_for_N_list_out_1 = bot_numbers_for_N_list
    N_bingo_row_1_bot.configure(
        text=bot_row_1_N_number, bg="#E2DF00", font=("Helvetica", 20)
    )
    return bot_draw_N_numbers_row_2(bot_numbers_for_N_list_out_1)


#  Bot card maker for G row:
def bot_draw_G_numbers_row_5(bot_numbers_for_G_list_out_4):
    bot_row_5_G_number = random.choice(bot_numbers_for_G_list_out_4)
    # takes out drawing number from the list
    bot_take_out_of_list_G = bot_numbers_for_G_list_out_4.index(bot_row_5_G_number)
    bot_numbers_for_G_list_out_4.pop(bot_take_out_of_list_G)
    G_bingo_row_5_bot.configure(
        text=bot_row_5_G_number, bg="#F96815", font=("Helvetica", 20)
    )


def bot_draw_G_numbers_row_4(bot_numbers_for_G_list_out_3):
    bot_row_4_G_number = random.choice(bot_numbers_for_G_list_out_3)
    # takes out drawing number from the list
    bot_take_out_of_list_G = bot_numbers_for_G_list_out_3.index(bot_row_4_G_number)
    bot_numbers_for_G_list_out_3.pop(bot_take_out_of_list_G)
    bot_numbers_for_G_list_out_4 = bot_numbers_for_G_list_out_3
    G_bingo_row_4_bot.configure(
        text=bot_row_4_G_number, bg="#F96815", font=("Helvetica", 20)
    )
    return bot_draw_G_numbers_row_5(bot_numbers_for_G_list_out_4)


def bot_draw_G_numbers_row_3(bot_numbers_for_G_list_out_2):
    bot_row_3_G_number = random.choice(bot_numbers_for_G_list_out_2)
    # takes out drawing number from the list
    bot_take_out_of_list_G = bot_numbers_for_G_list_out_2.index(bot_row_3_G_number)
    bot_numbers_for_G_list_out_2.pop(bot_take_out_of_list_G)
    bot_numbers_for_G_list_out_3 = bot_numbers_for_G_list_out_2
    G_bingo_row_3_bot.configure(
        text=bot_row_3_G_number, bg="#F96815", font=("Helvetica", 20)
    )
    return bot_draw_G_numbers_row_4(bot_numbers_for_G_list_out_3)


def bot_draw_G_numbers_row_2(bot_numbers_for_G_list_out_1):
    bot_row_2_G_number = random.choice(bot_numbers_for_G_list_out_1)
    # takes out drawing number from the list
    bot_take_out_of_list_G = bot_numbers_for_G_list_out_1.index(bot_row_2_G_number)
    bot_numbers_for_G_list_out_1.pop(bot_take_out_of_list_G)
    bot_numbers_for_G_list_out_2 = bot_numbers_for_G_list_out_1
    G_bingo_row_2_bot.configure(
        text=bot_row_2_G_number, bg="#F96815", font=("Helvetica", 20)
    )
    return bot_draw_G_numbers_row_3(bot_numbers_for_G_list_out_2)


def bot_draw_G_numbers_row_1():
    bot_numbers_for_G_list = []
    bot_numbers_for_G_list_int = [i for i in range(46, 61)]
    for e in bot_numbers_for_G_list_int:
        e = str(e)
        bot_numbers_for_G_list.append(e)
    bot_row_1_G_number = random.choice(bot_numbers_for_G_list)
    # takes out drawing number from the list
    take_out_of_list_G = bot_numbers_for_G_list.index(bot_row_1_G_number)
    bot_numbers_for_G_list.pop(take_out_of_list_G)
    bot_numbers_for_G_list_out_1 = bot_numbers_for_G_list
    G_bingo_row_1_bot.configure(
        text=bot_row_1_G_number, bg="#F96815", font=("Helvetica", 20)
    )
    return bot_draw_G_numbers_row_2(bot_numbers_for_G_list_out_1)


# bot card maker row O
def bot_draw_O_numbers_row_5(bot_numbers_for_O_list_out_4):
    bot_row_5_O_number = random.choice(bot_numbers_for_O_list_out_4)
    # takes out drawing number from the list
    bot_take_out_of_list_O = bot_numbers_for_O_list_out_4.index(bot_row_5_O_number)
    bot_numbers_for_O_list_out_4.pop(bot_take_out_of_list_O)
    O_bingo_row_5_bot.configure(
        text=bot_row_5_O_number, bg="#00FF33", font=("Helvetica", 20)
    )


def bot_draw_O_numbers_row_4(bot_numbers_for_O_list_out_3):
    bot_row_4_O_number = random.choice(bot_numbers_for_O_list_out_3)
    # takes out drawing number from the list
    bot_take_out_of_list_O = bot_numbers_for_O_list_out_3.index(bot_row_4_O_number)
    bot_numbers_for_O_list_out_3.pop(bot_take_out_of_list_O)
    bot_numbers_for_O_list_out_4 = bot_numbers_for_O_list_out_3
    O_bingo_row_4_bot.configure(
        text=bot_row_4_O_number, bg="#00FF33", font=("Helvetica", 20)
    )
    return bot_draw_O_numbers_row_5(bot_numbers_for_O_list_out_4)


def bot_draw_O_numbers_row_3(bot_numbers_for_O_list_out_2):
    bot_row_3_O_number = random.choice(bot_numbers_for_O_list_out_2)
    # takes out drawing number from the list
    bot_take_out_of_list_O = bot_numbers_for_O_list_out_2.index(bot_row_3_O_number)
    bot_numbers_for_O_list_out_2.pop(bot_take_out_of_list_O)
    bot_numbers_for_O_list_out_3 = bot_numbers_for_O_list_out_2
    O_bingo_row_3_bot.configure(
        text=bot_row_3_O_number, bg="#00FF33", font=("Helvetica", 20)
    )
    return bot_draw_O_numbers_row_4(bot_numbers_for_O_list_out_3)


def bot_draw_O_numbers_row_2(bot_numbers_for_O_list_out_1):
    bot_row_2_O_number = random.choice(bot_numbers_for_O_list_out_1)
    # takes out drawing number from the list
    bot_take_out_of_list_O = bot_numbers_for_O_list_out_1.index(bot_row_2_O_number)
    bot_numbers_for_O_list_out_1.pop(bot_take_out_of_list_O)
    bot_numbers_for_O_list_out_2 = bot_numbers_for_O_list_out_1
    O_bingo_row_2_bot.configure(
        text=bot_row_2_O_number, bg="#00FF33", font=("Helvetica", 20)
    )
    return bot_draw_O_numbers_row_3(bot_numbers_for_O_list_out_2)


def bot_draw_O_numbers_row_1():
    bot_numbers_for_O_list = []
    bot_numbers_for_O_list_int = [i for i in range(61, 76)]
    for e in bot_numbers_for_O_list_int:
        e = str(e)
        bot_numbers_for_O_list.append(e)
    bot_row_1_O_number = random.choice(bot_numbers_for_O_list)
    # takes out drawing number from the list
    take_out_of_list_O = bot_numbers_for_O_list.index(bot_row_1_O_number)
    bot_numbers_for_O_list.pop(take_out_of_list_O)
    bot_numbers_for_O_list_out_1 = bot_numbers_for_O_list
    O_bingo_row_1_bot.configure(
        text=bot_row_1_O_number, bg="#00FF33", font=("Helvetica", 20)
    )
    return bot_draw_O_numbers_row_2(bot_numbers_for_O_list_out_1)


# Call functions that make bot's card
bot_draw_B_numbers_row_1()
bot_draw_I_numbers_row_1()
bot_draw_N_numbers_row_1()
bot_draw_G_numbers_row_1()
bot_draw_O_numbers_row_1()


# function for BINGO_button:
def reset_bingo_button():  # resets to original color
    Bingo_button.config(
        text="BINGO!", bg="#B900FF", command=click_BINGO, font=("Helvetica", 25)
    )


def click_BINGO():
    Bingo_button.config(text="NO BINGO!!!", bg="#FF0000", font=("Helvetica", 25))
    return Bingo_button.after(3000, reset_bingo_button)


def make_a_new_player_card():
    # game needs to be paused
    # calls function for row B maker
    draw_B_numbers_row_1()
    draw_I_numbers_row_1()
    draw_N_numbers_row_1()
    draw_G_numbers_row_1()
    draw_O_numbers_row_1()


def make_a_new_bot_card():
    # .config(text="new bot", bg="#FF0000", font=("Helvetica", 20))
    bot_draw_B_numbers_row_1()
    bot_draw_I_numbers_row_1()
    bot_draw_N_numbers_row_1()
    bot_draw_G_numbers_row_1()
    bot_draw_O_numbers_row_1()


def make_a_new_game():
    # call make_a_new_player_card()
    # call make_a_new_bot_card()
    make_a_new_player_card()
    make_a_new_bot_card()


###mark
def play():
    global flag
    flag = True

    pass


def pause():
    global flag
    flag = False
    timer.config(text="Game paused", padx=5, pady=45, font=("Helvetica", 17))
    pass


# last row
Bingo_button = Button(
    root, text="BINGO!", bg="#B900FF", command=click_BINGO, font=("Helvetica", 25)
)
blank = Label(root, bg="#737373")
New_card = Button(
    root,
    text="New Card",
    bg="#FFFB00",
    command=make_a_new_player_card,
    font=("Helvetica", 20),
)
New_game = Button(
    root, text="New Game", bg="#29EFD1", command=make_a_new_game, font=("Helvetica", 20)
)
pause = Button(root, text="Pause", bg="#FF0000", font=("Helvetica", 20), command=pause)
play = Button(root, text="Play", bg="#2AFF00", font=("Helvetica", 20), command=play)

# last row positions # columnspan = 5
Bingo_button.grid(row=14, column=1, columnspan=3, sticky="nsew")
blank.grid(row=14, column=4, columnspan=1, sticky="nsew")
New_card.grid(row=14, column=5, columnspan=2, sticky="nsew")
New_game.grid(row=14, column=7, columnspan=2, sticky="nsew")
pause.grid(row=14, column=10, columnspan=1, sticky="nsew")
play.grid(row=14, column=9, columnspan=1, sticky="nsew")

root.mainloop()
