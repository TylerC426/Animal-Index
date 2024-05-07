import numpy as np
import cv2

cap = cv2.VideoCapture(0)

running = False

while running:
    ret, frame = cap.read()


def turnOn():
    """Turns on camera to scan for animal."""
    running = True

def turnOff():
    """Turns camera back off when scanning has been completed."""
    running = False

def getImage():
    """This will take an image from the camera of whats being scanned after it has been identified."""
    pass
