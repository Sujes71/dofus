import pyautogui as pa
import keyboard

while True:
    if keyboard.is_pressed('f3'):
        print(str(pa.position()))
    if keyboard.is_pressed('escape'):
        break;