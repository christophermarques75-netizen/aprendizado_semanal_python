from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def jogo():

    resultado = ""
    
    if request.method == "POST":

        jogador = request.form.get('jogada').upper()
        computador = random.choice(['PEDRA', 'PAPEL', 'TESOURA'])

        if jogador == computador:
            resultado  = f"empate, ambos escolheram {jogador}."
        elif (jogador == "PEDRA" and computador == "TESOURA") or (jogador == "PAPEL" and computador == "PEDRA") or (jogador == "TESOURA" and computador == "PAPEL"):
            resultado = f"voce ganhou pq computador escolheu {computador}"
        else:
            resultado = f"voce perdeu pq computador escolheu {computador}"
            
    return render_template("interface.html", resultado=resultado)

if __name__ == '__main__':
    app.run(port=5000)
