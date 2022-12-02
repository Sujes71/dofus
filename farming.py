import pyautogui as pg
import time
from pynput.keyboard import Key
import keyboard
import os, sys
import threading


imageOffSet = 25
image_list = []
path = "./Maiz"

def imageSelector():
    directory = os.listdir(path)
    for file in directory:
        if file.endswith('.png') or file.endswith('.jpg'):
            image_list.append(file)

def checkNettle():
    global stop_threads
    stop_threads = False
    while True:
        if stop_threads:
            print("Finalizado satisfactoriamente")
            break
        else:
            for image in image_list:
                try:
                    pos = pg.locateOnScreen(path + "./" + image, confidence = 0.55)
                    pg.moveTo(pos[0] + imageOffSet, pos[1]+imageOffSet)
                    pg.click()
                    
                except:
                    print("NO SE HA ENCONTRADO RECURSO")
                    pg.moveTo(500, 0)

            time.sleep(0.5)
    
def finalize():
    global stop_threads
    global end
    while True:
        if keyboard.is_pressed("esc"):
            stop_threads = True
            break
        
         
imageSelector()
x = threading.Thread(target=checkNettle)
y = threading.Thread(target=finalize)

x.start()
y.start()  
   
   