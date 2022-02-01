# ? do these need to be global for bingo button function row_1_b
# B column test:
# B_list_drawn_str = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15"
B_list_drawn_str = " "
row_1_B_number = 2
row_2_B_number = 1
row_3_B_number = 3
row_4_B_number = 4
row_5_B_number = 5
row_1_B_number = str(row_1_B_number)
row_2_B_number = str(row_2_B_number)
row_3_B_number = str(row_3_B_number)
row_4_B_number = str(row_4_B_number)
row_5_B_number = str(row_5_B_number)

# I column test:
# I_list_drawn_str = "16 17 18 19 20 21 22 23 24 25 26 27 28 29 30"
I_list_drawn_str = " "
row_1_I_number = 16
row_2_I_number = 18
row_3_I_number = 23
row_4_I_number = 24
row_5_I_number = 25
row_1_I_number = str(row_1_I_number)
row_2_I_number = str(row_2_I_number)
row_3_I_number = str(row_3_I_number)
row_4_I_number = str(row_4_I_number)
row_5_I_number = str(row_5_I_number)

# column N check if bingo
# N_list_drawn_str = "31 32 33 34 35 37 38 39 40 41 42 43 44 45"
N_list_drawn_str = ""
row_1_N_number = 31
row_2_N_number = 32
row_3_N_number = 40
row_4_N_number = 44
row_5_N_number = 34
row_1_N_number = str(row_1_N_number)
row_2_N_number = str(row_2_N_number)
row_3_N_number = str(row_3_N_number)
row_4_N_number = str(row_4_N_number)
row_5_N_number = str(row_5_N_number)

# column G check if bingo
# G_list_drawn_str = "46 47 48 49 50 51 52 53 54 55 56 57 58 59 60"
G_list_drawn_str = ""
row_1_G_number = 60
row_2_G_number = 59
row_3_G_number = 55
row_4_G_number = 51
row_5_G_number = 57
row_1_G_number = str(row_1_G_number)
row_2_G_number = str(row_2_G_number)
row_3_G_number = str(row_3_G_number)
row_4_G_number = str(row_4_G_number)
row_5_G_number = str(row_5_G_number)

# column O check if bingo
# O_list_drawn_str = "61 62 63 64 65 66 67 68 69 70 71 72 73 74 75"
O_list_drawn_str = ""
row_1_O_number = 74
row_2_O_number = 73
row_3_O_number = 65
row_4_O_number = 66
row_5_O_number = 61
row_1_O_number = str(row_1_O_number)
row_2_O_number = str(row_2_O_number)
row_3_O_number = str(row_3_O_number)
row_4_O_number = str(row_4_O_number)
row_5_O_number = str(row_5_O_number)

# TODO: do rows B I N G O row 1!!! and through tests!
B_list_drawn_str = "1"
I_list_drawn_str = "16"
N_list_drawn_str = "31"
G_list_drawn_str = "46"
O_list_drawn_str = "61"
row_1_B_number = 1
row_1_I_number = 16
row_1_N_number = 31
row_1_G_number = 46
row_1_O_number = 61
row_1_B_number = str(row_1_B_number)
row_1_I_number = str(row_1_I_number)
row_1_N_number = str(row_1_N_number)
row_1_G_number = str(row_1_G_number)
row_1_O_number = str(row_1_O_number)

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
elif (
    N_list_drawn_str.find(row_1_N_number) != -1
    and N_list_drawn_str.find(row_2_N_number) != -1
    and N_list_drawn_str.find(row_3_N_number) != -1
    and N_list_drawn_str.find(row_4_N_number) != -1
    and N_list_drawn_str.find(row_5_N_number) != -1
):
    print("N column pass")
elif (
    G_list_drawn_str.find(row_1_G_number) != -1
    and G_list_drawn_str.find(row_2_G_number) != -1
    and G_list_drawn_str.find(row_3_G_number) != -1
    and G_list_drawn_str.find(row_4_G_number) != -1
    and G_list_drawn_str.find(row_5_G_number) != -1
):
    print("G column pass")
elif (
    O_list_drawn_str.find(row_1_O_number) != -1
    and O_list_drawn_str.find(row_2_O_number) != -1
    and O_list_drawn_str.find(row_3_O_number) != -1
    and O_list_drawn_str.find(row_4_O_number) != -1
    and O_list_drawn_str.find(row_5_O_number) != -1
):
    print("O column pass")
elif (
    B_list_drawn_str.find(row_1_B_number) != -1
    and I_list_drawn_str.find(row_1_I_number) != -1
    and N_list_drawn_str.find(row_1_N_number) != -1
    and G_list_drawn_str.find(row_1_G_number) != -1
    and O_list_drawn_str.find(row_1_O_number) != -1
):
    print("Row 1 of card")
else:
    print("NO BINGO!!!")

# TODO: do rows B I N G O row 1!!! and through 5
# row_1_B_number
# row_2_B_number
# row_3_B_number
# row_4_B_number
# row_5_B_number
