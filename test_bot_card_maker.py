import random


def draw_B_numbers_row_2(numbers_for_B_list_out_1):
    row_2_B_number = random.choice(numbers_for_B_list_out_1)
    # takes out drawing number from the list
    take_out_of_list_B = numbers_for_B_list_out_1.index(row_2_B_number)
    numbers_for_B_list_out_1.pop(take_out_of_list_B)
    numbers_for_B_list_out_2 = numbers_for_B_list_out_1
    print(row_2_B_number, numbers_for_B_list_out_2)  ### delete
    return row_2_B_number, numbers_for_B_list_out_2


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
    print(bot_row_1_B_number, bot_numbers_for_B_list_out_1)  ### delete
    return bot_row_1_B_number, bot_numbers_for_B_list_out_1


bot_row_1_B_number, bot_numbers_for_B_list_out_1 = bot_draw_B_numbers_row_1()
row_2_B_number, numbers_for_B_list_out_2 = draw_B_numbers_row_2(
    bot_numbers_for_B_list_out_1
)
# row_3_B_number, numbers_for_B_list_out_3 = draw_B_numbers_row_3(
#     numbers_for_B_list_out_2
# )
# row_4_B_number, numbers_for_B_list_out_4 = draw_B_numbers_row_4(
#     numbers_for_B_list_out_3
# )
# row_5_B_number = draw_B_numbers_row_5(numbers_for_B_list_out_4)
