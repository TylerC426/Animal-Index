import pineworkslabs.RPi as GPIO
from time import sleep
import GUI

YELLOW_BUTTON = 16
RED_BUTTON = 13
BLUE_BUTTON = 12
GREEN_BUTTON = 6

GPIO.setmode(GPIO.LE_POTATO_LOOKUP)
GPIO.setup(YELLOW_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(RED_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BLUE_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(GREEN_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

LED = 25
GPIO.setup(LED, GPIO.OUT)

while True:
    if GPIO.input(YELLOW_BUTTON) == GPIO.HIGH:
        print("closed!")
        GPIO.output(LED, GPIO.HIGH)
        pass

    elif GPIO.input(RED_BUTTON) == GPIO.HIGH:
        print("closed!")
        GPIO.output(LED, GPIO.HIGH)
        pass

    elif GPIO.input(BLUE_BUTTON) == GPIO.HIGH:
        print("closed!")
        GPIO.output(LED, GPIO.HIGH)
        pass

    elif GPIO.input(GREEN_BUTTON) == GPIO.HIGH:
        print("closed!")
        GPIO.output(LED, GPIO.HIGH)
        pass

    else:
        print("open!")
        GPIO.output(LED, GPIO.LOW)
        pass
    sleep(1)