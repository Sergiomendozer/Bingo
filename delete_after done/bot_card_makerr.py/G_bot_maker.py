import random


def bot_draw_G_numbers_row_5(bot_numbers_for_G_list_out_4):
    bot_row_5_G_number = random.choice(bot_numbers_for_G_list_out_4)
    # takes out drawing number from the list
    bot_take_out_of_list_G = bot_numbers_for_G_list_out_4.index(bot_row_5_G_number)
    bot_numbers_for_G_list_out_4.pop(bot_take_out_of_list_G)
    print(bot_row_5_G_number)  ### delete
    return bot_row_5_G_number


def bot_draw_G_numbers_row_4(bot_numbers_for_G_list_out_3):
    bot_row_4_G_number = random.choice(bot_numbers_for_G_list_out_3)
    # takes out drawing number from the list
    bot_take_out_of_list_G = bot_numbers_for_G_list_out_3.index(bot_row_4_G_number)
    bot_numbers_for_G_list_out_3.pop(bot_take_out_of_list_G)
    bot_numbers_for_G_list_out_4 = bot_numbers_for_G_list_out_3
    print(bot_row_4_G_number, bot_numbers_for_G_list_out_4)  ### delete
    return bot_row_4_G_number, bot_numbers_for_G_list_out_4


def bot_draw_G_numbers_row_3(bot_numbers_for_G_list_out_2):
    bot_row_3_G_number = random.choice(bot_numbers_for_G_list_out_2)
    # takes out drawing number from the list
    bot_take_out_of_list_G = bot_numbers_for_G_list_out_2.index(bot_row_3_G_number)
    bot_numbers_for_G_list_out_2.pop(bot_take_out_of_list_G)
    bot_numbers_for_G_list_out_3 = bot_numbers_for_G_list_out_2
    print(bot_row_3_G_number, bot_numbers_for_G_list_out_3)  ### delete
    return bot_row_3_G_number, bot_numbers_for_G_list_out_3


def bot_draw_G_numbers_row_2(bot_numbers_for_G_list_out_1):
    bot_row_2_G_number = random.choice(bot_numbers_for_G_list_out_1)
    # takes out drawing number from the list
    bot_take_out_of_list_G = bot_numbers_for_G_list_out_1.index(bot_row_2_G_number)
    bot_numbers_for_G_list_out_1.pop(bot_take_out_of_list_G)
    bot_numbers_for_G_list_out_2 = bot_numbers_for_G_list_out_1
    print(bot_row_2_G_number, bot_numbers_for_G_list_out_2)  ### delete
    return bot_row_2_G_number, bot_numbers_for_G_list_out_2


def bot_draw_G_numbers_row_1():
    bot_numbers_for_G_list = []
    bot_numbers_for_G_list_int = [i for i in range(1, 16)]
    for e in bot_numbers_for_G_list_int:
        e = str(e)
        bot_numbers_for_G_list.append(e)
    bot_row_1_G_number = random.choice(bot_numbers_for_G_list)
    # takes out drawing number from the list
    take_out_of_list_G = bot_numbers_for_G_list.index(bot_row_1_G_number)
    bot_numbers_for_G_list.pop(take_out_of_list_G)
    bot_numbers_for_G_list_out_1 = bot_numbers_for_G_list
    print(bot_row_1_G_number, bot_numbers_for_G_list_out_1)  ### delete
    return bot_row_1_G_number, bot_numbers_for_G_list_out_1


bot_row_1_G_number, bot_numbers_for_G_list_out_1 = bot_draw_G_numbers_row_1()
bot_row_2_G_number, bot_numbers_for_G_list_out_2 = bot_draw_G_numbers_row_2(
    bot_numbers_for_G_list_out_1
)
bot_row_3_G_number, bot_numbers_for_G_list_out_3 = bot_draw_G_numbers_row_3(
    bot_numbers_for_G_list_out_2
)
bot_row_4_G_number, bot_numbers_for_G_list_out_4 = bot_draw_G_numbers_row_4(
    bot_numbers_for_G_list_out_3
)
bot_row_5_G_number = bot_draw_G_numbers_row_5(bot_numbers_for_G_list_out_4)
