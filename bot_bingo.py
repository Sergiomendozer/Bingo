from tkinter import *

root = Tk()

### indicates that bot won
# Bot_wins_bingo = Label(
#     root,
#     text="You lose, Bot has won Bingo!! ",
#     font=("Helvetica", 40),
#     bg="#FF4646",
#     padx=40,
#     pady=40,
# )
# Bot_wins_bingo.place(x=180, y=40)


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
row_1_B_number = 0
row_2_B_number = 0
row_3_B_number = 0
row_4_B_number = 0
row_5_B_number = 0
I_list_drawn_str = "3 9"
row_1_I_number = 0
row_2_I_number = 0
row_3_I_number = 0
row_4_I_number = 0
row_5_I_number = 0
N_list_drawn_str = ""
row_1_N_number = 0
row_2_N_number = 0
row_4_N_number = 0
row_5_N_number = 0
G_list_drawn_str = ""
row_1_G_number = 0
row_2_G_number = 0
row_3_G_number = 0
row_4_G_number = 0
row_5_G_number = 0
O_list_drawn_str = ""
row_1_O_number = 0
row_2_O_number = 0
row_3_O_number = 0
row_4_O_number = 0
row_5_O_number = 0

#######

# B column str convert:
row_1_B_number = str(row_1_B_number)
row_2_B_number = str(row_2_B_number)
row_3_B_number = str(row_3_B_number)
row_4_B_number = str(row_4_B_number)
row_5_B_number = str(row_5_B_number)

# I column convert:
row_1_I_number = str(row_1_I_number)
row_2_I_number = str(row_2_I_number)
row_3_I_number = str(row_3_I_number)
row_4_I_number = str(row_4_I_number)
row_5_I_number = str(row_5_I_number)

# N column convert:
row_1_N_number = str(row_1_N_number)
row_2_N_number = str(row_2_N_number)
row_4_N_number = str(row_4_N_number)
row_5_N_number = str(row_5_N_number)

# G column convert:
row_1_G_number = str(row_1_G_number)
row_2_G_number = str(row_2_G_number)
row_3_G_number = str(row_3_G_number)
row_4_G_number = str(row_4_G_number)
row_5_G_number = str(row_5_G_number)

# O column convert:
row_1_O_number = str(row_1_O_number)
row_2_O_number = str(row_2_O_number)
row_3_O_number = str(row_3_O_number)
row_4_O_number = str(row_4_O_number)
row_5_O_number = str(row_5_O_number)

# All B column for BINGO card to win
if (
    B_list_drawn_str.find(" " + row_1_B_number + " ") != -1
    and B_list_drawn_str.find(" " + row_2_B_number + " ") != -1
    and B_list_drawn_str.find(" " + row_3_B_number + " ") != -1
    and B_list_drawn_str.find(" " + row_4_B_number + " ") != -1
    and B_list_drawn_str.find(" " + row_5_B_number + " ") != -1
):
    Bingo_button.configure(
        text="YOU got BINGO!", bg="#00FF33", command=click_BINGO, font=("Helvetica", 25)
    )
# All I column for BINGO card to win
elif (
    I_list_drawn_str.find(" " + row_1_I_number + " ") != -1
    and I_list_drawn_str.find(" " + row_2_I_number + " ") != -1
    and I_list_drawn_str.find(" " + row_3_I_number + " ") != -1
    and I_list_drawn_str.find(" " + row_4_I_number + " ") != -1
    and I_list_drawn_str.find(" " + row_5_I_number + " ") != -1
):
    Bingo_button.configure(
        text="YOU got BINGO!", bg="#00FF33", command=click_BINGO, font=("Helvetica", 25)
    )
# All N column for BINGO card to win
elif (
    N_list_drawn_str.find(" " + row_1_N_number + " ") != -1
    and N_list_drawn_str.find(" " + row_2_N_number + " ") != -1
    and N_list_drawn_str.find(" " + row_4_N_number + " ") != -1
    and N_list_drawn_str.find(" " + row_5_N_number + " ") != -1
):  # no row 3 because that is were free space is
    Bingo_button.configure(
        text="YOU got BINGO!", bg="#00FF33", command=click_BINGO, font=("Helvetica", 25)
    )
# All G column for BINGO card to win
elif (
    G_list_drawn_str.find(" " + row_1_G_number + " ") != -1
    and G_list_drawn_str.find(" " + row_2_G_number + " ") != -1
    and G_list_drawn_str.find(" " + row_3_G_number + " ") != -1
    and G_list_drawn_str.find(" " + row_4_G_number + " ") != -1
    and G_list_drawn_str.find(" " + row_5_G_number + " ") != -1
):
    Bingo_button.configure(
        text="YOU got BINGO!", bg="#00FF33", command=click_BINGO, font=("Helvetica", 25)
    )
# All O column for BINGO card to win
elif (
    O_list_drawn_str.find(" " + row_1_O_number + " ") != -1
    and O_list_drawn_str.find(" " + row_2_O_number + " ") != -1
    and O_list_drawn_str.find(" " + row_3_O_number + " ") != -1
    and O_list_drawn_str.find(" " + row_4_O_number + " ") != -1
    and O_list_drawn_str.find(" " + row_5_O_number + " ") != -1
):
    Bingo_button.configure(
        text="YOU got BINGO!", bg="#00FF33", command=click_BINGO, font=("Helvetica", 25)
    )
# all Row 1 for BINGO card to win
elif (
    B_list_drawn_str.find(" " + row_1_B_number + " ") != -1
    and I_list_drawn_str.find(" " + row_1_I_number + " ") != -1
    and N_list_drawn_str.find(" " + row_1_N_number + " ") != -1
    and G_list_drawn_str.find(" " + row_1_G_number + " ") != -1
    and O_list_drawn_str.find(" " + row_1_O_number + " ") != -1
):
    Bingo_button.configure(
        text="YOU got BINGO!", bg="#00FF33", command=click_BINGO, font=("Helvetica", 25)
    )
# all Row 2 for BINGO card to win
elif (
    B_list_drawn_str.find(" " + row_2_B_number + " ") != -1
    and I_list_drawn_str.find(" " + row_2_I_number + " ") != -1
    and N_list_drawn_str.find(" " + row_2_N_number + " ") != -1
    and G_list_drawn_str.find(" " + row_2_G_number + " ") != -1
    and O_list_drawn_str.find(" " + row_2_O_number + " ") != -1
):
    Bingo_button.configure(
        text="YOU got BINGO!", bg="#00FF33", command=click_BINGO, font=("Helvetica", 25)
    )
# all Row 3 for BINGO card to win
elif (
    B_list_drawn_str.find(" " + row_3_B_number) != -1
    and I_list_drawn_str.find(" " + row_3_I_number + " ") != -1
    and G_list_drawn_str.find(" " + row_3_G_number + " ") != -1
    and O_list_drawn_str.find(" " + row_3_O_number + " ") != -1
):  # no row 3 for N because that is were free space is
    Bingo_button.configure(
        text="YOU got BINGO!", bg="#00FF33", command=click_BINGO, font=("Helvetica", 25)
    )
# all Row 4 for BINGO card to win
elif (
    B_list_drawn_str.find(" " + row_4_B_number + " ") != -1
    and I_list_drawn_str.find(" " + row_4_I_number + " ") != -1
    and N_list_drawn_str.find(" " + row_4_N_number + " ") != -1
    and G_list_drawn_str.find(" " + row_4_G_number + " ") != -1
    and O_list_drawn_str.find(" " + row_4_O_number + " ") != -1
):
    Bingo_button.configure(
        text="YOU got BINGO!", bg="#00FF33", command=click_BINGO, font=("Helvetica", 25)
    )
# all Row 5 for BINGO card to win
elif (
    B_list_drawn_str.find(" " + row_5_B_number + " ") != -1
    and I_list_drawn_str.find(" " + row_5_I_number + " ") != -1
    and N_list_drawn_str.find(" " + row_5_N_number + " ") != -1
    and G_list_drawn_str.find(" " + row_5_G_number + " ") != -1
    and O_list_drawn_str.find(" " + row_5_O_number + " ") != -1
):
    Bingo_button.configure(
        text="YOU got BINGO!", bg="#00FF33", command=click_BINGO, font=("Helvetica", 25)
    )
# right sided diagonal line for BINGO card to win
elif (
    B_list_drawn_str.find(" " + row_1_B_number + " ") != -1
    and I_list_drawn_str.find(" " + row_2_I_number + " ") != -1
    and G_list_drawn_str.find(" " + row_4_G_number + " ") != -1
    and O_list_drawn_str.find(" " + row_5_O_number + " ") != -1
):  # no N taking into account b/c that is the free space
    Bingo_button.configure(
        text="YOU got BINGO!", bg="#00FF33", command=click_BINGO, font=("Helvetica", 25)
    )
# left sided diagonal line for BINGO card to win
elif (
    B_list_drawn_str.find(" " + row_5_B_number + " ") != -1
    and I_list_drawn_str.find(" " + row_4_I_number + " ") != -1
    and G_list_drawn_str.find(" " + row_2_G_number + " ") != -1
    and O_list_drawn_str.find(" " + row_1_O_number + " ") != -1
):  # no N taking into account b/c that is the free space
    Bingo_button.configure(
        text="YOU got BINGO!", bg="#00FF33", command=click_BINGO, font=("Helvetica", 25)
    )
else:
    Bingo_button.config(text="NO BINGO!!!", bg="#FF0000", font=("Helvetica", 25))
    Bingo_button.after(3000, reset_bingo_button)
