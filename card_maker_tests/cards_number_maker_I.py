import random


def draw_B_numbers_row_5(numbers_for_B_list_out_4):
    row_5_B_number = random.choice(numbers_for_B_list_out_4)
    # takes out drawing number from the list
    take_out_of_list_B = numbers_for_B_list_out_1.index(row_5_B_number)
    numbers_for_B_list_out_1.pop(take_out_of_list_B)
    print("5th: " + row_5_B_number)  ### delete
    print(numbers_for_B_list_out_4)  ### delete
    return row_5_B_number


def draw_B_numbers_row_4(numbers_for_B_list_out_3):
    row_4_B_number = random.choice(numbers_for_B_list_out_3)
    # takes out drawing number from the list
    take_out_of_list_B = numbers_for_B_list_out_1.index(row_4_B_number)
    numbers_for_B_list_out_1.pop(take_out_of_list_B)
    print("4th: " + row_4_B_number)  ### delete
    print(numbers_for_B_list_out_3)  ### delete
    numbers_for_B_list_out_4 = numbers_for_B_list_out_3
    return row_4_B_number, numbers_for_B_list_out_4


def draw_B_numbers_row_3(numbers_for_B_list_out_2):
    row_3_B_number = random.choice(numbers_for_B_list_out_2)
    # takes out drawing number from the list
    take_out_of_list_B = numbers_for_B_list_out_1.index(row_3_B_number)
    numbers_for_B_list_out_1.pop(take_out_of_list_B)
    print("3nd: " + row_3_B_number)  ### delete
    print(numbers_for_B_list_out_2)  ### delete
    numbers_for_B_list_out_3 = numbers_for_B_list_out_2
    return row_3_B_number, numbers_for_B_list_out_3


def draw_B_numbers_row_2(numbers_for_B_list_out_1):
    row_2_B_number = random.choice(numbers_for_B_list_out_1)
    # takes out drawing number from the list
    take_out_of_list_B = numbers_for_B_list_out_1.index(row_2_B_number)
    numbers_for_B_list_out_1.pop(take_out_of_list_B)
    print("2nd: " + row_2_B_number)  ### delete
    print(numbers_for_B_list_out_1)  ### delete
    numbers_for_B_list_out_2 = numbers_for_B_list_out_1
    return row_2_B_number, numbers_for_B_list_out_2


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
    print("1st: " + row_1_B_number)  ### delete
    print(numbers_for_B_list)  ### delete
    numbers_for_B_list_out_1 = numbers_for_B_list
    return row_1_B_number, numbers_for_B_list_out_1


row_1_B_number, numbers_for_B_list_out_1 = draw_B_numbers_row_1()
row_2_B_number, numbers_for_B_list_out_2 = draw_B_numbers_row_2(
    numbers_for_B_list_out_1
)
row_3_B_number, numbers_for_B_list_out_3 = draw_B_numbers_row_3(
    numbers_for_B_list_out_2
)
row_4_B_number, numbers_for_B_list_out_4 = draw_B_numbers_row_4(
    numbers_for_B_list_out_3
)
row_5_B_number = draw_B_numbers_row_5(numbers_for_B_list_out_4)
