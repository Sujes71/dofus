import pyautogui as pg
import time
from pynput.keyboard import Key
import keyboard
import os


imageOffSet = 25
image_list = []
path = "./Maiz"

def imageSelector():
    directory = os.listdir(path)
    for file in directory:
        if file.endswith('.png') or file.endswith('.jpg'):
            image_list.append(file)

def checkNettle():
    for image in image_list:
        try:
            if keyboard.is_pressed("esc"):
                break
            pos = pg.locateOnScreen(path + "./" + image, confidence = 0.58)
            pg.moveTo(pos[0] + imageOffSet, pos[1]+imageOffSet)
            pg.click()
            time.sleep(3)
           
            
        except:
            print("NO SE HA ENCONTRADO RECURSO")
            pg.moveTo(500, 0)

    time.sleep(0.5)

imageSelector()

while True:
    checkNettle()
    if keyboard.is_pressed("esc"):
        break