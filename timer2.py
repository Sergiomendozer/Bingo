import time
def seconds_down(a):
    a = int(a)
    a = a -1
    if a > -1:
        a = str(a)
        seconds_down(a)
        print (a)
        time.sleep(1)
        return a
    else:
        return seconds_down(7)

seconds_down(7)