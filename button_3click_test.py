from tkinter import *

root = Tk()


def click_row_1_B():
    """Provide a fancy multicolored button click handler that
    changes backgroundcolor based on clicks and an assigned color list"""
    # increase the click count
    click_row_1_B.click += 1

    # lengths of color list
    colorLen = len(click_row_1_B.colors)

    # set background to "click % colorLen" index in color list
    B_bingo_row_1.config(bg=click_row_1_B.colors[click_row_1_B.click % colorLen])


# put properties on the function - do it before you use them (avoid NameError)
# colors will be cycled in order with each click, wrapping around
click_row_1_B.click = 0
click_row_1_B.colors = ["#00ccff", "#B900ff", "#eee993"]

B_bingo_row_1 = Button(
    root,
    text="B1",
    bg=click_row_1_B.colors[0],  # 1st col to start
    font=("Helvetica", 20),
    command=click_row_1_B,
)

B_bingo_row_1.grid(row=9, column=1, sticky="nsew")

root.mainloop()
