from gpiozero import LED
from gpiozero import Button


import time
#INPUT

led1 = LED(23)
led2 = LED(24)
led3 = LED(18)
clique = 0

button = Button(20)
while True :
    if button.when_pressed:
        clique += 1
    if clique == 0:
        led1.off
        led2.off
        led3.off

    elif clique == 1:
        led1.on
        led2.on
        led3.on
    elif clique == 2:
        led1.on
        led2.on
        led3.on
        time(1)
        led1.off
        led2.off
        led3.off
    elif clique == 3:
        led1.on
        time(1)
        led1.off
        led2.on
        time(1)
        led2.off
        led3.on
        time(1)
        led3.off
    elif clique == 4:
        # sequence1
        led1.on
        led2.on
        led3.on
        time(3)
        # sequence2
        led1.on
        led2.on
        led3.on
        time(1)
        led1.off
        led2.off
        led3.off
        time(3)
        # sequence3
        led1.on
        time(1)
        led1.off
        led2.on
        time(1)
        led2.off
        led3.on
        time(1)
        led3.off
        time(3)
        # sequence4
        clique = 0




