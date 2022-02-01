# ? do these need to be global for bingo button function row_1_b
# B column test:
# B_list_drawn_str = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15"
B_list_drawn_str = ""
row_1_B_number = 2
row_2_B_number = 1
row_3_B_number = 3
row_4_B_number = 4
row_5_B_number = 5
row_1_B_number = str(row_1_B_number)
row_2_B_number = str(row_1_B_number)
row_3_B_number = str(row_1_B_number)
row_4_B_number = str(row_1_B_number)
row_5_B_number = str(row_1_B_number)

# I column test:
I_list_drawn_str = "16 17 18 19 20 21 22 23 24 25 26 27 28 29 30"
row_1_I_number = 16
row_2_I_number = 18
row_3_I_number = 23
row_4_I_number = 24
row_5_I_number = 25
row_1_I_number = str(row_1_I_number)
row_2_I_number = str(row_1_I_number)
row_3_I_number = str(row_1_I_number)
row_4_I_number = str(row_1_I_number)
row_5_I_number = str(row_1_I_number)

# column B check if bingo
if (
    B_list_drawn_str.find(row_1_B_number) != -1
    and B_list_drawn_str.find(row_2_B_number) != -1
    and B_list_drawn_str.find(row_3_B_number) != -1
    and B_list_drawn_str.find(row_4_B_number) != -1
    and B_list_drawn_str.find(row_5_B_number) != -1
):
    print("B column pass")
elif (
    I_list_drawn_str.find(row_1_I_number) != -1
    and I_list_drawn_str.find(row_2_I_number) != -1
    and I_list_drawn_str.find(row_3_I_number) != -1
    and I_list_drawn_str.find(row_4_I_number) != -1
    and I_list_drawn_str.find(row_5_I_number) != -1
):
    print("I column pass")
else:
    print("NO BINGO!!!")
# row_1_B_number
# row_2_B_number
# row_3_B_number
# row_4_B_number
# row_5_B_number
