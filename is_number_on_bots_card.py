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

B_list_drawn_str = " "
I_list_drawn_str = " "
N_list_drawn_str = " "
G_list_drawn_str = " "
O_list_drawn_str = " "

drawn_bingo_number = 1

# B_bingo_row_1_bot = Label(
#     root, text=bot_row_1_B_number, bg="#00CCFF", font=("Helvetica", 20)
# )
# ### above is just for test


# def is_number_on_bots_card():
#     global drawn_bingo_number, bot_row_1_B_number, bot_row_2_B_number, bot_row_3_B_number, bot_row_4_B_number, bot_row_5_B_number, bot_row_1_I_number, bot_row_2_I_number, bot_row_3_I_number, bot_row_4_I_number, bot_row_5_I_number, bot_row_1_N_number, bot_row_2_N_number, bot_row_3_N_number, bot_row_4_N_number, bot_row_5_N_number, bot_row_1_G_number, bot_row_2_G_number, bot_row_3_G_number, bot_row_4_G_number, bot_row_5_G_number, bot_row_1_O_number, bot_row_2_O_number, bot_row_3_O_number, bot_row_4_O_number, bot_row_5_O_number
# if bot_row_1_B_number == drawn_bingo_number:
#     B_bingo_row_1_bot.config(text=bot_row_1_B_number, bg="#B900FF", font=("Helvetica", 20))
# elif bot_row_2_B_number == drawn_bingo_number:
#     B_bingo_row_2_bot.config(text=bot_row_2_B_number, bg="#B900FF", font=("Helvetica", 20))
# elif bot_row_3_B_number == drawn_bingo_number:
#     B_bingo_row_3_bot.config(text=bot_row_3_B_number, bg="#B900FF", font=("Helvetica", 20))
# elif bot_row_4_B_number == drawn_bingo_number:
#     B_bingo_row_4_bot.config(text=bot_row_4_B_number, bg="#B900FF", font=("Helvetica", 20))
# elif bot_row_5_B_number == drawn_bingo_number:
#     B_bingo_row_5_bot.config(text=bot_row_5_B_number, bg="#B900FF", font=("Helvetica", 20))

### above is old
# * highlighted bookmark
# def is_number_on_bots_card():
#     global drawn_bingo_number, bot_row_1_B_number, bot_row_2_B_number, bot_row_3_B_number, bot_row_4_B_number, bot_row_5_B_number, bot_row_1_I_number, bot_row_2_I_number, bot_row_3_I_number, bot_row_4_I_number, bot_row_5_I_number, bot_row_1_N_number, bot_row_2_N_number, bot_row_3_N_number, bot_row_4_N_number, bot_row_5_N_number, bot_row_1_G_number, bot_row_2_G_number, bot_row_3_G_number, bot_row_4_G_number, bot_row_5_G_number, bot_row_1_O_number, bot_row_2_O_number, bot_row_3_O_number, bot_row_4_O_number, bot_row_5_O_number
#     print(drawn_bingo_number[2:])  # !delete used for test
#     print(bot_row_1_B_number)  # !delete for test
#     if bot_row_1_B_number == drawn_bingo_number[2:]:
#         B_bingo_row_1_bot.config(bg="#B900FF")
#     elif bot_row_2_B_number == drawn_bingo_number[2:]:
#         B_bingo_row_2_bot.config(bg="#B900FF")
#     elif bot_row_3_B_number == drawn_bingo_number[2:]:
#         B_bingo_row_3_bot.config(bg="#B900FF")
#     elif bot_row_4_B_number == drawn_bingo_number[2:]:
#         B_bingo_row_4_bot.config(bg="#B900FF")
#     elif bot_row_5_B_number == drawn_bingo_number[2:]:
#         B_bingo_row_5_bot.config(bg="#B900FF")

#     elif bot_row_1_I_number == drawn_bingo_number[2:]:
#         I_bingo_row_1_bot.config(bg="#B900FF")
#     elif bot_row_2_I_number == drawn_bingo_number[2:]:
#         I_bingo_row_2_bot.config(bg="#B900FF")
#     elif bot_row_3_I_number == drawn_bingo_number[2:]:
#         I_bingo_row_3_bot.config(bg="#B900FF")
#     elif bot_row_4_I_number == drawn_bingo_number[2:]:
#         I_bingo_row_4_bot.config(bg="#B900FF")
#     elif bot_row_5_I_number == drawn_bingo_number[2:]:
#         I_bingo_row_5_bot.config(bg="#B900FF")

#     elif bot_row_1_N_number == drawn_bingo_number[2:]:
#         N_bingo_row_1_bot.config(bg="#B900FF")
#     elif bot_row_2_N_number == drawn_bingo_number[2:]:
#         N_bingo_row_2_bot.config(bg="#B900FF")
#     elif bot_row_3_N_number == drawn_bingo_number[2:]:
#         N_bingo_row_3_bot.config(bg="#B900FF")  ### star here star is # !delete
#     elif bot_row_4_N_number == drawn_bingo_number[2:]:
#         N_bingo_row_4_bot.config(bg="#B900FF")
#     elif bot_row_5_N_number == drawn_bingo_number[2:]:
#         N_bingo_row_5_bot.config(bg="#B900FF")

#     elif bot_row_1_G_number == drawn_bingo_number[2:]:
#         G_bingo_row_1_bot.config(bg="#B900FF")
#     elif bot_row_2_G_number == drawn_bingo_number[2:]:
#         G_bingo_row_2_bot.config(bg="#B900FF")
#     elif bot_row_3_G_number == drawn_bingo_number[2:]:
#         G_bingo_row_3_bot.config(bg="#B900FF")
#     elif bot_row_4_G_number == drawn_bingo_number[2:]:
#         G_bingo_row_4_bot.config(bg="#B900FF")
#     elif bot_row_5_G_number == drawn_bingo_number[2:]:
#         G_bingo_row_5_bot.config(bg="#B900FF")

#     elif bot_row_1_O_number == drawn_bingo_number[2:]:
#         O_bingo_row_1_bot.config(bg="#B900FF")
#     elif bot_row_2_O_number == drawn_bingo_number[2:]:
#         O_bingo_row_2_bot.config(bg="#B900FF")
#     elif bot_row_3_O_number == drawn_bingo_number[2:]:
#         O_bingo_row_3_bot.config(bg="#B900FF")
#     elif bot_row_4_O_number == drawn_bingo_number[2:]:
#         O_bingo_row_4_bot.config(bg="#B900FF")
#     elif bot_row_5_O_number == drawn_bingo_number[2:]:
#         O_bingo_row_5_bot.config(bg="#B900FF")
