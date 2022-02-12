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
#     pady=40,
# )

#############
## indicates that player won
# player_wins_bingo.config(
#     text="BINGO!! Congrats, You win",
#     font=("Helvetica", 40),
#     bg="#B900FF",
#     padx=40,
#     pady=40,
# )


def reset_bingo_button():
    pass


def click_BINGO():
    pass


Bingo_button = Button(
    root, text="BINGO!", bg="#B900FF", command=click_BINGO, font=("Helvetica", 25)
)
Bingo_button.grid(row=14, column=1, columnspan=3, sticky="nsew")
##################
global B_list_drawn_str, row_1_B_number, row_2_B_number, row_3_B_number, row_4_B_number, row_5_B_number, I_list_drawn_str, row_1_I_number, row_2_I_number, row_3_I_number, row_4_I_number, row_5_I_number, N_list_drawn_str, row_1_N_number, row_2_N_number, row_4_N_number, row_5_N_number, G_list_drawn_str, row_1_G_number, row_2_G_number, row_3_G_number, row_4_G_number, row_5_G_number, O_list_drawn_str, row_1_O_number, row_2_O_number, row_3_O_number, row_4_O_number, row_5_O_number
#####################
B_list_drawn_str = " "
bot_row_1_B_number = 0
bot_row_2_B_number = 0
bot_row_3_B_number = 0
bot_row_4_B_number = 0
bot_row_5_B_number = 0

I_list_drawn_str = " "
bot_row_1_I_number = 0
bot_row_2_I_number = 0
bot_row_3_I_number = 0
bot_row_4_I_number = 0
bot_row_5_I_number = 0

N_list_drawn_str = " "
bot_row_1_N_number = 0
bot_row_2_N_number = 0
bot_row_3_N_number = 0
bot_row_4_N_number = 0
bot_row_5_N_number = 0

G_list_drawn_str = " "
bot_row_1_G_number = 0
bot_row_2_G_number = 0
bot_row_3_G_number = 0
bot_row_4_G_number = 0
bot_row_5_G_number = 0

O_list_drawn_str = " "
bot_row_1_O_number = 0
bot_row_2_O_number = 0
bot_row_3_O_number = 0
bot_row_4_O_number = 0
bot_row_5_O_number = 0
##################################
# global
# TODO: add all globals
# B column str convert:

# All B column for BINGO card to win
if (
    B_list_drawn_str.find(" " + bot_row_1_B_number + " ") != -1
    and B_list_drawn_str.find(" " + bot_row_2_B_number + " ") != -1
    and B_list_drawn_str.find(" " + bot_row_3_B_number + " ") != -1
    and B_list_drawn_str.find(" " + bot_row_4_B_number + " ") != -1
    and B_list_drawn_str.find(" " + bot_row_5_B_number + " ") != -1
):
    pass  ## add label that indicates that bot won
# All I column for BINGO card to win
elif (
    I_list_drawn_str.find(" " + bot_row_1_I_number + " ") != -1
    and I_list_drawn_str.find(" " + bot_row_2_I_number + " ") != -1
    and I_list_drawn_str.find(" " + bot_row_3_I_number + " ") != -1
    and I_list_drawn_str.find(" " + bot_row_4_I_number + " ") != -1
    and I_list_drawn_str.find(" " + bot_row_5_I_number + " ") != -1
):
    pass  ## add label that indicates that bot won
# All N column for BINGO card to win
elif (
    N_list_drawn_str.find(" " + bot_row_1_N_number + " ") != -1
    and N_list_drawn_str.find(" " + bot_row_2_N_number + " ") != -1
    and N_list_drawn_str.find(" " + bot_row_4_N_number + " ") != -1
    and N_list_drawn_str.find(" " + bot_row_5_N_number + " ") != -1
):  # no row 3 because that is were free space is
    Bingo_button.configure(
        text="YOU got BINGO!", bg="#00FF33", command=click_BINGO, font=("Helvetica", 25)
    )
# All G column for BINGO card to win
elif (
    G_list_drawn_str.find(" " + bot_row_1_G_number + " ") != -1
    and G_list_drawn_str.find(" " + bot_row_2_G_number + " ") != -1
    and G_list_drawn_str.find(" " + bot_row_3_G_number + " ") != -1
    and G_list_drawn_str.find(" " + bot_row_4_G_number + " ") != -1
    and G_list_drawn_str.find(" " + bot_row_5_G_number + " ") != -1
):
    Bingo_button.configure(
        text="YOU got BINGO!", bg="#00FF33", command=click_BINGO, font=("Helvetica", 25)
    )
# All O column for BINGO card to win
elif (
    O_list_drawn_str.find(" " + bot_row_1_O_number + " ") != -1
    and O_list_drawn_str.find(" " + bot_row_2_O_number + " ") != -1
    and O_list_drawn_str.find(" " + bot_row_3_O_number + " ") != -1
    and O_list_drawn_str.find(" " + bot_row_4_O_number + " ") != -1
    and O_list_drawn_str.find(" " + bot_row_5_O_number + " ") != -1
):
    Bingo_button.configure(
        text="YOU got BINGO!", bg="#00FF33", command=click_BINGO, font=("Helvetica", 25)
    )
# all Row 1 for BINGO card to win
elif (
    B_list_drawn_str.find(" " + bot_row_1_B_number + " ") != -1
    and I_list_drawn_str.find(" " + bot_row_1_I_number + " ") != -1
    and N_list_drawn_str.find(" " + bot_row_1_N_number + " ") != -1
    and G_list_drawn_str.find(" " + bot_row_1_G_number + " ") != -1
    and O_list_drawn_str.find(" " + bot_row_1_O_number + " ") != -1
):
    Bingo_button.configure(
        text="YOU got BINGO!", bg="#00FF33", command=click_BINGO, font=("Helvetica", 25)
    )
# all Row 2 for BINGO card to win
elif (
    B_list_drawn_str.find(" " + bot_row_2_B_number + " ") != -1
    and I_list_drawn_str.find(" " + bot_row_2_I_number + " ") != -1
    and N_list_drawn_str.find(" " + bot_row_2_N_number + " ") != -1
    and G_list_drawn_str.find(" " + bot_row_2_G_number + " ") != -1
    and O_list_drawn_str.find(" " + bot_row_2_O_number + " ") != -1
):
    Bingo_button.configure(
        text="YOU got BINGO!", bg="#00FF33", command=click_BINGO, font=("Helvetica", 25)
    )
# all Row 3 for BINGO card to win
elif (
    B_list_drawn_str.find(" " + bot_row_3_B_number) != -1
    and I_list_drawn_str.find(" " + bot_row_3_I_number + " ") != -1
    and G_list_drawn_str.find(" " + bot_row_3_G_number + " ") != -1
    and O_list_drawn_str.find(" " + bot_row_3_O_number + " ") != -1
):  # no row 3 for N because that is were free space is
    Bingo_button.configure(
        text="YOU got BINGO!", bg="#00FF33", command=click_BINGO, font=("Helvetica", 25)
    )
# all Row 4 for BINGO card to win
elif (
    B_list_drawn_str.find(" " + bot_row_4_B_number + " ") != -1
    and I_list_drawn_str.find(" " + bot_row_4_I_number + " ") != -1
    and N_list_drawn_str.find(" " + bot_row_4_N_number + " ") != -1
    and G_list_drawn_str.find(" " + bot_row_4_G_number + " ") != -1
    and O_list_drawn_str.find(" " + bot_row_4_O_number + " ") != -1
):
    Bingo_button.configure(
        text="YOU got BINGO!", bg="#00FF33", command=click_BINGO, font=("Helvetica", 25)
    )
# all Row 5 for BINGO card to win
elif (
    B_list_drawn_str.find(" " + bot_row_5_B_number + " ") != -1
    and I_list_drawn_str.find(" " + bot_row_5_I_number + " ") != -1
    and N_list_drawn_str.find(" " + bot_row_5_N_number + " ") != -1
    and G_list_drawn_str.find(" " + bot_row_5_G_number + " ") != -1
    and O_list_drawn_str.find(" " + bot_row_5_O_number + " ") != -1
):
    Bingo_button.configure(
        text="YOU got BINGO!", bg="#00FF33", command=click_BINGO, font=("Helvetica", 25)
    )
# right sided diagonal line for BINGO card to win
elif (
    B_list_drawn_str.find(" " + bot_row_1_B_number + " ") != -1
    and I_list_drawn_str.find(" " + bot_row_2_I_number + " ") != -1
    and G_list_drawn_str.find(" " + bot_row_4_G_number + " ") != -1
    and O_list_drawn_str.find(" " + bot_row_5_O_number + " ") != -1
):  # no N taking into account b/c that is the free space
    Bingo_button.configure(
        text="YOU got BINGO!", bg="#00FF33", command=click_BINGO, font=("Helvetica", 25)
    )
# left sided diagonal line for BINGO card to win
elif (
    B_list_drawn_str.find(" " + bot_row_5_B_number + " ") != -1
    and I_list_drawn_str.find(" " + bot_row_4_I_number + " ") != -1
    and G_list_drawn_str.find(" " + bot_row_2_G_number + " ") != -1
    and O_list_drawn_str.find(" " + bot_row_1_O_number + " ") != -1
):  # no N taking into account b/c that is the free space
    Bingo_button.configure(
        text="YOU got BINGO!", bg="#00FF33", command=click_BINGO, font=("Helvetica", 25)
    )
else:
    Bingo_button.config(text="NO BINGO!!!", bg="#FF0000", font=("Helvetica", 25))
    Bingo_button.after(3000, reset_bingo_button)
