import pyautogui
import time
import keyboard
import sys

def automatizar_001():
    if keyboard.is_pressed("j"):
        sys.exit()
    pyautogui.hotkey("win", "r")
    time.sleep(1)
    pyautogui.press('backspace')
    pyautogui.write(r"code C:\Users\CHRISTOPHERGABRIELMA\Desktop\tudo\pyautogui")
    time.sleep(1)
    pyautogui.press("enter")


def automatizar_002():
    if keyboard.is_pressed("j"):
        sys.exit()
    pyautogui.hotkey("win", "r")
    time.sleep(2)
    pyautogui.press('backspace')
    pyautogui.write(r"code C:\Users\CHRISTOPHERGABRIELMA\Desktop\tudo\hora de codar")
    time.sleep(1)
    pyautogui.press("enter")

