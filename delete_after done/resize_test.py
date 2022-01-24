#pip install pillow
from tkinter import *
from PIL import ImageTk, Image# imports pillow
root = Tk()
root.geometry("800x500")

#call image b4 resize
original_star = Image.open("STAR.png")
#resizing image
resized = original_star.resize((100,70), Image.ANTIALIAS) # resize(sides, height)
resized_star = ImageTk.PhotoImage(resized)

#label
label = Label(root, image = resized_star)
label.pack()

root.mainloop()
