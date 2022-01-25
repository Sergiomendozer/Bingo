from tkinter import *
from drawing_numbers import random_bingo_number
import time
root = Tk()
root.title("update Label")
root.geometry("1015x570")


def update_drawn_ball(bingo_numbers):
    (drawn_bingo_number,bingo_numbers) = random_bingo_number(bingo_numbers)
    bingo_number = list(bingo_numbers)
    Random_number_picked_label.config(text = drawn_bingo_number, font =("Helvetica", 24), bg = "#FFFFFF")
    return Random_number_picked_label.after(5000,update_drawn_ball, bingo_numbers) #.after(parent, ms, function = None, *args)


Random_number_picked_label =Label(root,text = " fff  ", font =("Helvetica", 24), bg = "#FFFFFF") 
Random_number_picked_label.place(x = 260, y =55) 
bingo_numbers = ["B 1","B 2","B 3","B 4","B 4","B 5","B 7", "B 8","B 9","B 10","B 11","B 12","B 13","B 14","B 15","I 16","I 17","I 18","I 19","I 20","I 21","I 22","I 23","I 24","I 25","I 26","I 27","I 28","I 29","I 30","N 31","N 32","N 33","N 34","N 35","N 36","N 37","N 38","N 39","N 40","N 41","N 42","N 42","N 44","N 45","G 46","G 47","G 48","G 49","G 50","G 51","G 52","G 53","G 54","G 55","G 56","G 57","G 58","G 59","G 60","O 61","O 62","O 63","O 64","O 65","O 66","O 67","O 68","O 69","O 70","O 71","O 72","O 73","O 74","O 75"]
update_drawn_ball(bingo_numbers)
root.mainloop()