import keyboard
import sys
user = input("aperte j para sair do codigo")
while True:
    if keyboard.is_pressed("j"):
        print("abcf")
    elif user == "437":
        sys.exit()
    else:
        print("b")