from tkinter import *

root = Tk()

# designate height and width of app
app_width = 1015
app_height = 570
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (app_width / 2)
y_coordinate = (screen_height / 2) - (app_height / 2)
root.geometry(f"{app_width}x{app_height}+{int(x_coordinate)}+{int(y_coordinate)}")

root.mainloop()
