from tkinter import *

root = Tk()


def click_row_1_B(event):
    B_bingo_row_1.config(bg="#B900FF")


def double_click_row_1_B(event):
    B_bingo_row_1.config(bg="#00CCFF")


B_bingo_row_1 = Button(root, text="B1", bg="#00CCFF", font=("Helvetica", 20))
B_bingo_row_1.grid(row=9, column=1, sticky="nsew")

B_bingo_row_1.bind("<Double-Button-1>", double_click_row_1_B)
B_bingo_row_1.bind("<Button-1>", click_row_1_B)

root.mainloop()
