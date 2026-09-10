from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/receber-dados', methods=['POST'])
def receber_dados():
    dados = request.get_json()
    print("Dados recebidos:", dados)
    return jsonify({"status": "sucesso", "mensagem": "Dados salvos!"})

if __name__ == '__main__':
    app.run(port=5000)
