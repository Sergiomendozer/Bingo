import random


def draw_I_numbers_row_5(numbers_for_I_list_out_4):
    row_5_I_number = random.choice(numbers_for_I_list_out_4)
    # takes out drawing number from the list
    take_out_of_list_I = numbers_for_I_list_out_1.index(row_5_I_number)
    numbers_for_I_list_out_4.pop(take_out_of_list_I)
    print("5th: " + row_5_I_number)  ### delete
    print(numbers_for_I_list_out_4)  ### delete
    return row_5_I_number


def draw_I_numbers_row_4(numbers_for_I_list_out_3):
    row_4_I_number = random.choice(numbers_for_I_list_out_3)
    # takes out drawing number from the list
    take_out_of_list_I = numbers_for_I_list_out_1.index(row_4_I_number)
    numbers_for_I_list_out_3.pop(take_out_of_list_I)
    print("4th: " + row_4_I_number)  ### delete
    print(numbers_for_I_list_out_3)  ### delete
    numbers_for_I_list_out_4 = numbers_for_I_list_out_3
    return row_4_I_number, numbers_for_I_list_out_3


def draw_I_numbers_row_3(numbers_for_I_list_out_2):
    row_3_I_number = random.choice(numbers_for_I_list_out_2)
    # takes out drawing number from the list
    take_out_of_list_I = numbers_for_I_list_out_2.index(row_3_I_number)
    numbers_for_I_list_out_2.pop(take_out_of_list_I)
    print("3rd: " + row_3_I_number)  ### delete
    print(numbers_for_I_list_out_1)  ### delete
    numbers_for_I_list_out_3 = numbers_for_I_list_out_2
    return row_3_I_number, numbers_for_I_list_out_3


def draw_I_numbers_row_2(numbers_for_I_list_out_1):
    row_2_I_number = random.choice(numbers_for_I_list_out_1)
    # takes out drawing number from the list
    take_out_of_list_I = numbers_for_I_list_out_1.index(row_2_I_number)
    numbers_for_I_list_out_1.pop(take_out_of_list_I)
    print("2nd: " + row_2_I_number)  ### delete
    print(numbers_for_I_list_out_1)  ### delete
    numbers_for_I_list_out_2 = numbers_for_I_list_out_1
    return row_2_I_number, numbers_for_I_list_out_2


def draw_I_numbers_row_1():
    numbers_for_I_list = [
        "16",
        "17",
        "18",
        "19",
        "20",
        "21",
        "22",
        "23",
        "24",
        "25",
        "26",
        "27",
        "28",
        "29",
        "30",
    ]
    row_1_I_number = random.choice(numbers_for_I_list)
    # takes out drawing number from the list
    take_out_of_list_I = numbers_for_I_list.index(row_1_I_number)
    numbers_for_I_list.pop(take_out_of_list_I)
    print("1st: " + row_1_I_number)  ### delete
    print(numbers_for_I_list)  ### delete
    numbers_for_I_list_out_1 = numbers_for_I_list
    return row_1_I_number, numbers_for_I_list_out_1


row_1_I_number, numbers_for_I_list_out_1 = draw_I_numbers_row_1()
row_2_I_number, numbers_for_I_list_out_2 = draw_I_numbers_row_2(
    numbers_for_I_list_out_1
)
row_3_I_number, numbers_for_I_list_out_3 = draw_I_numbers_row_3(
    numbers_for_I_list_out_2
)
row_4_I_number, numbers_for_I_list_out_4 = draw_I_numbers_row_4(
    numbers_for_I_list_out_3
)
row_5_I_number = draw_I_numbers_row_5(numbers_for_I_list_out_4)
