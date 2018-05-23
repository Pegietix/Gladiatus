''' OFFLINE TIMER for future use'''

import atexit
import datetime
import os
import pickle
import time


def save():  # save daty uplyniecia czasu
    with open('timersave.pkl', 'wb') as f:
        pickle.dump(stop, f)


atexit.register(save)

# print(stop)    # test

if os.stat("timersave.pkl").st_size != 0:  # Load timersave if it exists
    with open('timersave.pkl', 'rb') as f:
        stop = pickle.load(f)
        check1 = str(stop)
        check2 = str(datetime.datetime.now())
        if check1 < check2:
            print("TIME PASSED")
            stop = datetime.datetime.now() + datetime.timedelta(0,
                                                                20 * 0 + 10
                                                                * 1 + 0)  #
            # data uplyniecia czasu
            delta = datetime.timedelta()
            x = datetime.timedelta(delta.days,
                                   delta.seconds)  # formatowanie
            # pozostalego czasu pod print
        else:
            print("Your task is not completed yet")
else:
    hours = int(input("How many hours would you like to spend at work? (1-8)"))

    stop = datetime.datetime.now() + datetime.timedelta(0,
                                                        60 * 60 * hours)  #
    # data uplyniecia czasu
    delta = datetime.timedelta()
    x = datetime.timedelta(delta.days,
                           delta.seconds)  # formatowanie pozostalego czasu
    # pod print


# print(stop)    # retest

def delting():
    global delta, x
    delta = stop - datetime.datetime.now()
    x = datetime.timedelta(delta.days, delta.seconds)
    if x > datetime.timedelta():
        print("\r{}".format(x), end="")


def delting_loop():
    global x
    count = 5
    while x > datetime.timedelta() and count > 0:
        delting()
        time.sleep(1)
        count -= 1
    if x <= datetime.timedelta():
        print("\rTIME PASSED", end='')


delting()
delting_loop()

'''print(stop)
print(delta)
print(x)'''

# save()
