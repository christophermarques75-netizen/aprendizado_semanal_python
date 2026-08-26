import pyautogui
import time
import keyboard
import sys
from webbrowser import open

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

def automatizar_o_salafuturo():
    open("https://saladofuturo.educacao.sp.gov.br/login-alunos")
    keyboard.wait("esc")
    pyautogui.press("tab", presses=19)
    pyautogui.write("seu ra")
    pyautogui.press("tab")
    pyautogui.write("seu digito")
    pyautogui.press("tab", presses=2)
    pyautogui.write("s")
    pyautogui.press("enter")