from tkinter import *
from PIL import ImageTk, Image# imports pillow
root = Tk()
root.geometry("800x500")

#call image b4 resize
original_ball = Image.open("B-Bingo-ball.png")
#resizing image
resized = original_ball.resize((100,70), Image.ANTIALIAS) # resize(sides, height)
resized_ball = ImageTk.PhotoImage(resized)

#label
label = Label(root, image = resized_ball)
label.pack()

root.mainloop()