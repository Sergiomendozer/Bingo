from cProfile import label
from tkinter import *
root = Tk()
root.title("<TITLE>")
root.geometry("1015x570")
from PIL import ImageTk,Image

bg = ImageTk.PhotoImage(Image.open("ball.png"))###
Label1 = Label(root, image = bg)
Label1.place(x=0,y=0, relwidth= 1, relheight=1) # grid

#
tex = Label(root, text = "B 75") # set background to color of image so it look see through
tex.pack() ### grid
root.mainloop()


root.mainloop()