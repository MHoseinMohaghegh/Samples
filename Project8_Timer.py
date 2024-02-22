# Time

# import time module
import time

# countdown function


def countdown(t):
    # delay time is 5 seconds at first
    x = 5
    # this loop works until the adjusted time has over
    while t > 0:
        # using divmod function to display the time in mm:ss format
        mins, secs = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        # clear the line before display the decreased time
        print(timer, end="\r")
        # the program stops until the "x" seconds and after that goes to the below lines
        time.sleep(x)
        # We get the new time after subtracting the delay time
        t -= x
        # the delay time decreases 1 second every time, this loop runs, until the delay time become 1 second
        if x > 1:
            x -= 1
    print("Time is over.")


# get the time period from the user
t = input("Enter the time in seconds: ")
# calling the countdown function
countdown(int(t))
# get the user input before exit the program
input()
