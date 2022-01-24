from tkinter import *
root = Tk()
root.title("CLOCK")
root.geometry("600x400")

def update():
    label_1.config(text="new text")

label_1 = Label(root, text = "nn")
label_1.pack(pady=20)

label_1.after(5000, update)# time 5second = 5000

root.mainloop()