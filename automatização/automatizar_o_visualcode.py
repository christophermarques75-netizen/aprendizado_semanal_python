import tkinter as tk
from auxiliar_de_autenticação import *
from tkinter import font

janela = tk.Tk()
janela.title("automatização do chris")
##acima cria a janela
janela.geometry("900x500")
##tamanho da janela

fonte_em_negrito = font.Font(family="arial", size=12, weight="bold")
##fonte pra desenvolvimento futuro

janela.config(bg="#1e1e1e")

separador0 = tk.Label(janela,bg="#1e1e1e", fg="white", text="--------------------------------------------------------")
separador0.pack()
#
botao1 = tk.Button(janela,  text="Repositório do GitHub", font=fonte_em_negrito, bg="black",  fg="white", command=automatizar_001)

botao1.pack()

##localização do botão e o que é o botão e o comando dele
separador1 = tk.Label(janela,bg="#1e1e1e", fg="white", text="--------------------------------------------------------")
separador1.pack()
##separador por estilização

botao2 = tk.Button(janela, text="Pasta do Projeto Para o TCC", font=fonte_em_negrito, bg="black", fg="white", command=automatizar_002)
botao2.pack()

separador2 = tk.Label(janela,bg="#1e1e1e", fg="white", text="--------------------------------------------------------")
separador2.pack()

botao3 = tk.Button(janela, text="automatizar o sala do futuro", bg="black", fg="white", font=fonte_em_negrito, command=automatizar_o_salafuturo)
botao3.pack()

janela.mainloop()