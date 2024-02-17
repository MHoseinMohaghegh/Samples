# Time


import time


def countdown(t):
    # Zamane delay 5 sanie.
    x = 5
    while t > 0:
        mins, secs = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        print(timer, end="\r")
        time.sleep(x)
        t -= x
        # time e delay ra 1 sanie kam mikonim, ta 1 sanie.
        if x > 1:
            x -= 1
    print("Time is over.")


t = input("Enter the time in seconds: ")
countdown(int(t))
