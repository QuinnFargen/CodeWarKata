"""
Will there be enough space?
You have to write a function that accepts three parameters:

cap is the amount of people the bus can hold excluding the driver.
on is the number of people on the bus.
wait is the number of people waiting to get on to the bus.
If there is enough space, return 0, and if there isn't, return the number of passengers he can't take.
"""



def enough(cap, on, wait):
    if on + wait < cap:
        return 0
    else:
        return (on + wait) - cap

enough(100, 60, 50) 