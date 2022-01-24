from cProfile import label
from tkinter import *
root = Tk()
root.title("<TITLE>")
root.geometry("1015x570")
from PIL import ImageTk,Image

bg = ImageTk.PhotoImage(Image.open("B-Bingo-ball.png"))###
Label1 = Label(root, image = bg)
Label1.grid(row=1, column=1, sticky="nsew")
# Label1.place(x=0,y=0, relwidth= 1, relheight=1) # grid

#
tex = Label(root, text = "B 75", bg = 'white') # set background to color of image so it look see through
#tex.grid(row=1, column=1, sticky="nsew")
tex.place(x=500, y=600) ### grid
root.mainloop()


root.mainloop()