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
    global stop_threads, isFight, end
    stop_threads = False
    isFight = False
    end = False
    count = 0
    while True:
        if stop_threads:
            pass
        elif fight():
            print("Let's Fight!")
            isFight = True
        elif end:
            print("Finalized!")
            break
        else:
            for image in image_list:
                count += 1
                pos = pg.locateOnScreen(path + "./" + image, confidence = 0.55)
                if pos == None:
                    print("Resources not found!")
                    continue
                pg.moveTo(pos[0] + imageOffSet, pos[1]+imageOffSet)
                pg.click()   
            if count == len(image_list):
                count = 0
                if pg.locateOnScreen( "./Others./fail.png", confidence=0.5) != None:
                    pg.moveTo(500, 0)
                if pg.locateOnScreen( "./Others./fail2.png", confidence=0.5) != None:
                    me = pg.locateOnScreen( "./Others./fail2.png", confidence=0.55)
                    if me == None:
                        continue
                    pg.moveTo(me[0] + imageOffSet, me[1]+imageOffSet - 60)
                    pg.click()
                    
                    
def fight():
    try:
        if pg.locateOnScreen( "./Others./fight.png") != None:
            os.startfile('Others\\ring.mp3')
            return True
    except:
        return False
        
        
def finalize():
    global stop_threads
    global end
    while True:
        if keyboard.is_pressed("f2") or isFight :
            stop_threads = True
        if keyboard.is_pressed("f1"):
            stop_threads = False
        if keyboard.is_pressed("esc"):
            end = True
            stop_threads = False
            break
            
        
         
imageSelector()
x = threading.Thread(target=checkNettle)
y = threading.Thread(target=finalize)

time.sleep(5)

x.start()
y.start()  
   
   