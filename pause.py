import tkinter as tk

root = tk.Tk()
time_var = tk.StringVar(root, value=10)

flag = True


def countdown():
    global flag
    temp = int(time_var.get())
    temp -= 1
    time_var.set(temp)
    if temp >= 0 and not flag:
        root.after(
            1000, countdown
        )  # This is where the function is called again. Time is in milseconds


def stop_timer():
    global flag
    flag = True


def start_timer():
    global flag
    flag = False
    countdown()


tk.Button(root, text="start", command=start_timer).pack(side="bottom")
tk.Button(root, text="pause", command=stop_timer).pack(side="bottom")

time = tk.Label(root, textvariable=time_var)
time.pack()
root.mainloop()
