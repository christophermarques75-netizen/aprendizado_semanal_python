import tkinter as tk
from tkinter import font
from valores_para_calculo import *
import keyboard

janela = tk.Tk()
janela.title("automatização do chris")
##acima cria a janela
janela.geometry("900x500")
##tamanho da janela
fonte_em_negrito = font.Font(family="arial", size=12, weight="bold")
##fonte pra desenvolvimento futuro
janela.config(bg="#1e1e1e")

separador0 = tk.Label(janela,bg="black", fg="white",font=12, text="digite o seu salario liquido")
separador0.pack()

entrada2 = tk.Entry(janela, font=fonte_em_negrito, bg="black",  fg="white", insertbackground="white")
entrada2.pack()

entrada2.focus_set()

janela.bind("<Return>", lambda event: calcular_imposto(entrada2.get(), label_resultado))

label_resultado = tk.Label(janela, text="",bg="#1e1e1e", fg="white", font=fonte_em_negrito,)
label_resultado.pack(pady=10)

janela.mainloop()