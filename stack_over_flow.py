from tkinter import *

root = Tk()


def click_row_1_B():
    B_bingo_row_1.config(bg="#B900FF")


B_bingo_row_1 = Button(
    root, text="B1", bg="#00CCFF", font=("Helvetica", 20), command=click_row_1_B
)

B_bingo_row_1.grid(row=9, column=1, sticky="nsew")

root.mainloop()
