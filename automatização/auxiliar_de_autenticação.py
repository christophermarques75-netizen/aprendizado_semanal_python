import pyautogui
import time
import keyboard
import sys
from webbrowser import open
import subprocess

def automatizar_001():
    caminho = r"C:\Users\CHRISTOPHERGABRIELMA\Desktop\tudo\pyautogui"
    subprocess.run(["code", caminho], shell=True)

def automatizar_002():
    caminho = r"C:\Users\CHRISTOPHERGABRIELMA\Desktop\tudo\pasta_do_pi"
    subprocess.run(["code", caminho], shell=True)


def automatizar_003():
    caminho = r"C:\Users\CHRISTOPHERGABRIELMA\Documents\versionamento\terceiro bimestre"
    subprocess.run(["code", caminho], shell=True)


def automatizar_o_salafuturo():
    open("https://saladofuturo.educacao.sp.gov.br/login-alunos")
    keyboard.wait("esc")
    pyautogui.press("tab", presses=19)
    pyautogui.write("seu ra")
    pyautogui.press("tab")
    pyautogui.write("seu digito")
    pyautogui.press("tab", presses=2)
    pyautogui.write("sua senha")
    pyautogui.press("enter")