from PIL import ImageGrab
import pytesseract as pt
import numpy as np
from pynput import keyboard
import time


def read(screen):
    text = None
    try:
        image = np.array(ImageGrab.grab(screen))
        text = pt.image_to_string(image)
    except FileNotFoundError:
        print("Error occurred trying to open image!")
    finally:
        return text


def Typer(words=50):
    wordCounter = 0
    left, up, right, down = 480, 470, 1422, 549
    sim = keyboard.Controller()
    text = read((left, up, right, down))
    moveDownLine = 40
    up = up + moveDownLine
    down = down + moveDownLine
    while wordCounter < words:
        for letter in text:
            if "\n" in letter or " " in letter:
                wordCounter += 1
            if "\n" in letter:
                sim.press(keyboard.Key.space)
                sim.release(keyboard.Key.space)
            sim.type(letter)
            time.sleep(0.002)
        time.sleep(0.0001)
        text = read((left, up, right, down))
    else:
        print("done")


def on_press(key):
    try:
        if key == keyboard.Key.up:
            Typer()
    except AttributeError:
        pass


def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False


if __name__ == '__main__':
    print("hello world")
