from tkinter import *

root = Tk()

### label used if bot wins
Bot_wins_bingo = Label(root)
Bot_wins_bingo.place(x=180, y=40)

player_wins_bingo = Label(root)
player_wins_bingo.place(x=180, y=40)

# Bot_wins_bingo.config(text="You lose, Bot has won Bingo!! ",
#     font=("Helvetica", 40),
#     bg="#FF4646",
#     padx=40,
#     pady=40
# )

#############
# player_wins_bingo.config(
#     text="BINGO!! Congrats, You win",
#     font=("Helvetica", 40),
#     bg="#B900FF",
#     padx=40,
#     pady=40
# )

#### needed for bingo player

##################
# global B_list_drawn_str, row_1_B_number, row_2_B_number, row_3_B_number, row_4_B_number, row_5_B_number, I_list_drawn_str, row_1_I_number, row_2_I_number, row_3_I_number, row_4_I_number, row_5_I_number, N_list_drawn_str, row_1_N_number, row_2_N_number, row_4_N_number, row_5_N_number, G_list_drawn_str, row_1_G_number, row_2_G_number, row_3_G_number, row_4_G_number, row_5_G_number, O_list_drawn_str, row_1_O_number, row_2_O_number, row_3_O_number, row_4_O_number, row_5_O_number
#####################
# B_list_drawn_str = " "
# bot_row_1_B_number = 0
# bot_row_2_B_number = 0
# bot_row_3_B_number = 0
# bot_row_4_B_number = 0
# bot_row_5_B_number = 0

# I_list_drawn_str = " "
# bot_row_1_I_number = 0
# bot_row_2_I_number = 0
# bot_row_3_I_number = 0
# bot_row_4_I_number = 0
# bot_row_5_I_number = 0

# N_list_drawn_str = " "
# bot_row_1_N_number = 0
# bot_row_2_N_number = 0
# bot_row_3_N_number = 0
# bot_row_4_N_number = 0
# bot_row_5_N_number = 0

# G_list_drawn_str = " "
# bot_row_1_G_number = 0
# bot_row_2_G_number = 0
# bot_row_3_G_number = 0
# bot_row_4_G_number = 0
# bot_row_5_G_number = 0

# O_list_drawn_str = " "
# bot_row_1_O_number = 0
# bot_row_2_O_number = 0
# bot_row_3_O_number = 0
# bot_row_4_O_number = 0
# bot_row_5_O_number = 0
##################################
global flag, B_list_drawn_str, bot_row_1_B_number, bot_row_2_B_number, bot_row_3_B_number, bot_row_4_B_number, bot_row_5_B_number, I_list_drawn_str, bot_row_1_I_number, bot_row_2_I_number, bot_row_3_I_number, bot_row_4_I_number, bot_row_5_I_number, N_list_drawn_str, bot_row_1_N_number, bot_row_2_N_number, bot_row_4_N_number, bot_row_5_N_number, G_list_drawn_str, bot_row_1_G_number, bot_row_2_G_number, bot_row_3_G_number, bot_row_4_G_number, bot_row_5_G_number, O_list_drawn_str, bot_row_1_O_number, bot_row_2_O_number, bot_row_3_O_number, bot_row_4_O_number, bot_row_5_O_number
# TODO: add all globals!!!!!!!!!!!!!!!!!!

# All B column for BINGO card to win
if (
    B_list_drawn_str.find(" " + bot_row_1_B_number + " ") != -1
    and B_list_drawn_str.find(" " + bot_row_2_B_number + " ") != -1
    and B_list_drawn_str.find(" " + bot_row_3_B_number + " ") != -1
    and B_list_drawn_str.find(" " + bot_row_4_B_number + " ") != -1
    and B_list_drawn_str.find(" " + bot_row_5_B_number + " ") != -1
):
    Bot_wins_bingo.config(
        text="You lose, Bot has won Bingo!! ",
        font=("Helvetica", 40),
        bg="#FF4646",
        padx=40,
        pady=40,
    )
    flag = False

# All I column for BINGO card to win
elif (
    I_list_drawn_str.find(" " + bot_row_1_I_number + " ") != -1
    and I_list_drawn_str.find(" " + bot_row_2_I_number + " ") != -1
    and I_list_drawn_str.find(" " + bot_row_3_I_number + " ") != -1
    and I_list_drawn_str.find(" " + bot_row_4_I_number + " ") != -1
    and I_list_drawn_str.find(" " + bot_row_5_I_number + " ") != -1
):
    Bot_wins_bingo.config(
        text="You lose, Bot has won Bingo!! ",
        font=("Helvetica", 40),
        bg="#FF4646",
        padx=40,
        pady=40,
    )
    flag = False

# All N column for BINGO card to win
elif (
    N_list_drawn_str.find(" " + bot_row_1_N_number + " ") != -1
    and N_list_drawn_str.find(" " + bot_row_2_N_number + " ") != -1
    and N_list_drawn_str.find(" " + bot_row_4_N_number + " ") != -1
    and N_list_drawn_str.find(" " + bot_row_5_N_number + " ") != -1
):  # no row 3 because that is were free space is
    Bot_wins_bingo.config(
        text="You lose, Bot has won Bingo!! ",
        font=("Helvetica", 40),
        bg="#FF4646",
        padx=40,
        pady=40,
    )
    flag = False
# All G column for BINGO card to win
elif (
    G_list_drawn_str.find(" " + bot_row_1_G_number + " ") != -1
    and G_list_drawn_str.find(" " + bot_row_2_G_number + " ") != -1
    and G_list_drawn_str.find(" " + bot_row_3_G_number + " ") != -1
    and G_list_drawn_str.find(" " + bot_row_4_G_number + " ") != -1
    and G_list_drawn_str.find(" " + bot_row_5_G_number + " ") != -1
):
    Bot_wins_bingo.config(
        text="You lose, Bot has won Bingo!! ",
        font=("Helvetica", 40),
        bg="#FF4646",
        padx=40,
        pady=40,
    )
    flag = False
# All O column for BINGO card to win
elif (
    O_list_drawn_str.find(" " + bot_row_1_O_number + " ") != -1
    and O_list_drawn_str.find(" " + bot_row_2_O_number + " ") != -1
    and O_list_drawn_str.find(" " + bot_row_3_O_number + " ") != -1
    and O_list_drawn_str.find(" " + bot_row_4_O_number + " ") != -1
    and O_list_drawn_str.find(" " + bot_row_5_O_number + " ") != -1
):
    Bot_wins_bingo.config(
        text="You lose, Bot has won Bingo!! ",
        font=("Helvetica", 40),
        bg="#FF4646",
        padx=40,
        pady=40,
    )
    flag = False
# all Row 1 for BINGO card to win
elif (
    B_list_drawn_str.find(" " + bot_row_1_B_number + " ") != -1
    and I_list_drawn_str.find(" " + bot_row_1_I_number + " ") != -1
    and N_list_drawn_str.find(" " + bot_row_1_N_number + " ") != -1
    and G_list_drawn_str.find(" " + bot_row_1_G_number + " ") != -1
    and O_list_drawn_str.find(" " + bot_row_1_O_number + " ") != -1
):
    Bot_wins_bingo.config(
        text="You lose, Bot has won Bingo!! ",
        font=("Helvetica", 40),
        bg="#FF4646",
        padx=40,
        pady=40,
    )
    flag = False
# all Row 2 for BINGO card to win
elif (
    B_list_drawn_str.find(" " + bot_row_2_B_number + " ") != -1
    and I_list_drawn_str.find(" " + bot_row_2_I_number + " ") != -1
    and N_list_drawn_str.find(" " + bot_row_2_N_number + " ") != -1
    and G_list_drawn_str.find(" " + bot_row_2_G_number + " ") != -1
    and O_list_drawn_str.find(" " + bot_row_2_O_number + " ") != -1
):
    Bot_wins_bingo.config(
        text="You lose, Bot has won Bingo!! ",
        font=("Helvetica", 40),
        bg="#FF4646",
        padx=40,
        pady=40,
    )
    flag = False
# all Row 3 for BINGO card to win
elif (
    B_list_drawn_str.find(" " + bot_row_3_B_number) != -1
    and I_list_drawn_str.find(" " + bot_row_3_I_number + " ") != -1
    and G_list_drawn_str.find(" " + bot_row_3_G_number + " ") != -1
    and O_list_drawn_str.find(" " + bot_row_3_O_number + " ") != -1
):  # no row 3 for N because that is were free space is
    Bot_wins_bingo.config(
        text="You lose, Bot has won Bingo!! ",
        font=("Helvetica", 40),
        bg="#FF4646",
        padx=40,
        pady=40,
    )
    flag = False
# all Row 4 for BINGO card to win
elif (
    B_list_drawn_str.find(" " + bot_row_4_B_number + " ") != -1
    and I_list_drawn_str.find(" " + bot_row_4_I_number + " ") != -1
    and N_list_drawn_str.find(" " + bot_row_4_N_number + " ") != -1
    and G_list_drawn_str.find(" " + bot_row_4_G_number + " ") != -1
    and O_list_drawn_str.find(" " + bot_row_4_O_number + " ") != -1
):
    Bot_wins_bingo.config(
        text="You lose, Bot has won Bingo!! ",
        font=("Helvetica", 40),
        bg="#FF4646",
        padx=40,
        pady=40,
    )
    flag = False
# all Row 5 for BINGO card to win
elif (
    B_list_drawn_str.find(" " + bot_row_5_B_number + " ") != -1
    and I_list_drawn_str.find(" " + bot_row_5_I_number + " ") != -1
    and N_list_drawn_str.find(" " + bot_row_5_N_number + " ") != -1
    and G_list_drawn_str.find(" " + bot_row_5_G_number + " ") != -1
    and O_list_drawn_str.find(" " + bot_row_5_O_number + " ") != -1
):
    Bot_wins_bingo.config(
        text="You lose, Bot has won Bingo!! ",
        font=("Helvetica", 40),
        bg="#FF4646",
        padx=40,
        pady=40,
    )
    flag = False
# right sided diagonal line for BINGO card to win
elif (
    B_list_drawn_str.find(" " + bot_row_1_B_number + " ") != -1
    and I_list_drawn_str.find(" " + bot_row_2_I_number + " ") != -1
    and G_list_drawn_str.find(" " + bot_row_4_G_number + " ") != -1
    and O_list_drawn_str.find(" " + bot_row_5_O_number + " ") != -1
):  # no N taking into account b/c that is the free space
    Bot_wins_bingo.config(
        text="You lose, Bot has won Bingo!! ",
        font=("Helvetica", 40),
        bg="#FF4646",
        padx=40,
        pady=40,
    )
    flag = False
# left sided diagonal line for BINGO card to win
elif (
    B_list_drawn_str.find(" " + bot_row_5_B_number + " ") != -1
    and I_list_drawn_str.find(" " + bot_row_4_I_number + " ") != -1
    and G_list_drawn_str.find(" " + bot_row_2_G_number + " ") != -1
    and O_list_drawn_str.find(" " + bot_row_1_O_number + " ") != -1
):  # no N taking into account b/c that is the free space
    Bot_wins_bingo.config(
        text="You lose, Bot has won Bingo!! ",
        font=("Helvetica", 40),
        bg="#FF4646",
        padx=40,
        pady=40,
    )
    flag = False
else:
    None
