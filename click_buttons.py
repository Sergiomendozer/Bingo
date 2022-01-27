def click_row_1_B():
    click_row_1_B.click += 1
    colorLen = len(click_row_1_B.colors)
    B_bingo_row_1.config(bg=click_row_1_B.colors[click_row_1_B.click % colorLen])


click_row_1_B.click = 0
click_row_1_B.colors = ["#00ccff", "#B900ff"]


def click_row_1_I():
    click_row_1_I.click += 1
    colorLen = len(click_row_1_B.colors)
    I_bingo_row_1.config(bg=click_row_1_I.colors[click_row_1_I.click % colorLen])


click_row_1_I.click = 0
click_row_1_I.colors = ["#FF0000", "#B900ff"]


def click_row_1_N():
    click_row_1_N.click += 1
    colorLen = len(click_row_1_N.colors)
    N_bingo_row_1.config(bg=click_row_1_N.colors[click_row_1_N.click % colorLen])


click_row_1_N.click = 0
click_row_1_N.colors = ["#E2DF00", "#B900ff"]


def click_row_1_G():
    click_row_1_G.click += 1
    colorLen = len(click_row_1_G.colors)
    G_bingo_row_1.config(bg=click_row_1_G.colors[click_row_1_G.click % colorLen])


click_row_1_G.click = 0
click_row_1_G.colors = ["#F96815", "#B900ff"]


def click_row_1_O():
    click_row_1_O.click += 1
    colorLen = len(click_row_1_O.colors)
    O_bingo_row_1.config(bg=click_row_1_O.colors[click_row_1_O.click % colorLen])


click_row_1_O.click = 0
click_row_1_O.colors = ["#00FF33", "#B900ff"]
