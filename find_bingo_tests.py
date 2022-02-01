# ? do these need to be global for bingo button function row_1_b
B_list_drawn_str = "1 2 3 4 5"
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
# column B
if (
    B_list_drawn_str.find(row_1_B_number) != -1
    and B_list_drawn_str.find(row_2_B_number) != -1
    and B_list_drawn_str.find(row_3_B_number) != -1
    and B_list_drawn_str.find(row_4_B_number) != -1
    and B_list_drawn_str.find(row_5_B_number) != -1
):
    print("B column pass")

else:
    print("NO BINGO!!!")
# row_1_B_number
# row_2_B_number
# row_3_B_number
# row_4_B_number
# row_5_B_number
