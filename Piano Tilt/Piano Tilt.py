from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con



def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.05) 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    
    if pyautogui.pixel(775, 564)[0] == 0:
        click(778, 564)
    if pyautogui.pixel(919, 564)[0] == 0:
        click(919, 564)
    if pyautogui.pixel(1040, 564)[0] == 0:
        click(1040, 564)
    if pyautogui.pixel(1134, 564)[0] == 0:
        click(1134, 564)
