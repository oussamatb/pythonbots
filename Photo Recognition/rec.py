
from pyautogui import * 
import pyautogui 
import time 
import keyboard 
import random
import win32api, win32con
#grayscale=True, confidence=0.8
#Region
while 1:
    if pyautogui.locateOnScreen("Ali.png", confidence=0.7) != None:
        print("I can see Ali")
        time.sleep(0.5)
    elif pyautogui.locateOnScreen("A.png") != None:
        print("I can see The lettre A")
        time.sleep(0.5)
    elif pyautogui.locateOnScreen("car.png") != None:
        print("I can see a car")
        time.sleep(0.5)
    elif pyautogui.locateOnScreen("stickman.png") != None:
        print("I can see stickman")
        time.sleep(0.5)
    #elif pyautogui.locateOnScreen("Robot.jpg") != None:
        #print("I can see My cousin ")
        #time.sleep(0.5)
    #elif pyautogui.locateOnScreen("Me.png") != None:
        #print("I can see Oussama")
        #time.sleep(0.5)
    else:
        print("I am unable to see")
        time.sleep(0.5)
