from gpiozero import LED, Button
from signal import pause
import tm1637
import time
import numpy as np
import random

led=LED(16)
button=Button(18)
tm=tm1637.TM1637(clk=4,dio=17)
clear=[0,0,0,0]


def slots_roll():
    roll=""
    for i in range(4):
        digit=random.randint(0,9)
        roll+=str(digit)
        #There's probably a far less clunky way to do this, but I can't be bothered.
    return roll

def winch(roll):
    #"Winch" for "win check". I'm sometimes too clever for my own good.
    for digit in roll:
        if digit!=roll[0]:
            return False
    return True

def display_roll():
    roll=slots_roll()
    win=winch(roll)
    tm.show(roll)
    if win:
        for i in range(5):    
            led.on()
            time.sleep(0.5)
            led.off()
            time.sleep(0.5)
    else:
        time.sleep(1)
    tm.write(clear)


button.when_pressed=display_roll
led.off()
pause()
