import random


def draw_B_numbers_row_2(numbers_for_B_list):
    row_2_B_number = random.choice(numbers_for_B_list)
    # takes out drawing number from the list
    take_out_of_list_B = numbers_for_B_list.index(row_2_B_number)
    numbers_for_B_list.pop(take_out_of_list_B)
    print("second: " + row_2_B_number)  ### for testing
    print(numbers_for_B_list)  ### for tetsing
    return row_2_B_number


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
    print("first: " + row_1_B_number)  ### for testing
    print(numbers_for_B_list)  ### for tetsing
    # draw_B_numbers_row_2(numbers_for_B_list)
    return row_1_B_number


draw_B_numbers_row_1()
