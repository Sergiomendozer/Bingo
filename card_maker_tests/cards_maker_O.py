import random


def draw_O_numbers_row_5(numbers_for_O_list_out_4):
    row_5_O_number = random.choice(numbers_for_O_list_out_4)
    # takes out drawing number from the list
    take_out_of_list_O = numbers_for_O_list_out_1.index(row_5_O_number)
    numbers_for_O_list_out_4.pop(take_out_of_list_O)
    print("5th: " + row_5_O_number)  ### delete
    print(numbers_for_O_list_out_4)  ### delete
    return row_5_O_number


def draw_O_numbers_row_4(numbers_for_O_list_out_3):
    row_4_O_number = random.choice(numbers_for_O_list_out_3)
    # takes out drawing number from the list
    take_out_of_list_O = numbers_for_O_list_out_1.index(row_4_O_number)
    numbers_for_O_list_out_3.pop(take_out_of_list_O)
    print("4th: " + row_4_O_number)  ### delete
    print(numbers_for_O_list_out_3)  ### delete
    numbers_for_O_list_out_4 = numbers_for_O_list_out_3
    return row_4_O_number, numbers_for_O_list_out_3


def draw_O_numbers_row_3(numbers_for_O_list_out_2):
    row_3_O_number = random.choice(numbers_for_O_list_out_2)
    # takes out drawing number from the list
    take_out_of_list_O = numbers_for_O_list_out_2.index(row_3_O_number)
    numbers_for_O_list_out_2.pop(take_out_of_list_O)
    print("3rd: " + row_3_O_number)  ### delete
    print(numbers_for_O_list_out_1)  ### delete
    numbers_for_O_list_out_3 = numbers_for_O_list_out_2
    return row_3_O_number, numbers_for_O_list_out_3


def draw_O_numbers_row_2(numbers_for_O_list_out_1):
    row_2_O_number = random.choice(numbers_for_O_list_out_1)
    # takes out drawing number from the list
    take_out_of_list_O = numbers_for_O_list_out_1.index(row_2_O_number)
    numbers_for_O_list_out_1.pop(take_out_of_list_O)
    print("2nd: " + row_2_O_number)  ### delete
    print(numbers_for_O_list_out_1)  ### delete
    numbers_for_O_list_out_2 = numbers_for_O_list_out_1
    return row_2_O_number, numbers_for_O_list_out_2


def draw_O_numbers_row_1():
    numbers_for_O_list = [
        "61",
        "62",
        "63",
        "64",
        "65",
        "66",
        "67",
        "68",
        "69",
        "70",
        "71",
        "72",
        "73",
        "74",
        "75",
    ]
    row_1_O_number = random.choice(numbers_for_O_list)
    # takes out drawing number from the list
    take_out_of_list_O = numbers_for_O_list.index(row_1_O_number)
    numbers_for_O_list.pop(take_out_of_list_O)
    print("1st: " + row_1_O_number)  ### delete
    print(numbers_for_O_list)  ### delete
    numbers_for_O_list_out_1 = numbers_for_O_list
    return row_1_O_number, numbers_for_O_list_out_1


row_1_O_number, numbers_for_O_list_out_1 = draw_O_numbers_row_1()
row_2_O_number, numbers_for_O_list_out_2 = draw_O_numbers_row_2(
    numbers_for_O_list_out_1
)
row_3_O_number, numbers_for_O_list_out_3 = draw_O_numbers_row_3(
    numbers_for_O_list_out_2
)
row_4_O_number, numbers_for_O_list_out_4 = draw_O_numbers_row_4(
    numbers_for_O_list_out_3
)
row_5_O_number = draw_O_numbers_row_5(numbers_for_O_list_out_4)
