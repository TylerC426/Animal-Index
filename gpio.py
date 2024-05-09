import pineworkslabs.RPi as GPIO
from time import sleep

YELLOW_BUTTON = 16
RED_BUTTON = 13
BLUE_BUTTON = 12
GREEN_BUTTON = 6

GPIO.setmode(GPIO.LE_POTATO_LOOKUP)
GPIO.setup(YELLOW_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(RED_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BLUE_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(GREEN_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def checkButton():
    if GPIO.input(YELLOW_BUTTON) == GPIO.HIGH:
        return 0

    elif GPIO.input(RED_BUTTON) == GPIO.HIGH:
        return 1

    elif GPIO.input(BLUE_BUTTON) == GPIO.HIGH:
        return 2

    elif GPIO.input(GREEN_BUTTON) == GPIO.HIGH:
        return 3

# THIS IS NO LONGER BEING USED