import random

# def test_print(p1, p2):
#     p1 = str(p1)
#     p2 = str(p2)
#     print(p1 + " " + p2)


def draw_B_numbers_row():
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
    return (row_1_B_number, numbers_for_B_list)


draw_B_numbers_row()


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
numbers_for_N_list = [
    "31",
    "32",
    "33",
    "34",
    "35",
    "36",
    "37",
    "38",
    "39",
    "40",
    "41",
    "42",
    "43",
    "44",
    "45",
]
numbers_for_G_list = [
    "46",
    "47",
    "48",
    "49",
    "50",
    "51",
    "52",
    "53",
    "54",
    "55",
    "56",
    "57",
    "58",
    "59",
    "60",
]
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
    "72",
    "72",
    "73",
    "74",
    "75",
]
