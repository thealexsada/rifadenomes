from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulando armazenamento em memória (use um banco real em produção)
dados = []

@app.route('/salvar', methods=['POST'])
def salvar():
    nome = request.form['nome']
    escolhas = request.form['escolhas']
    numeros = list(map(int, escolhas.split(',')))

    # Verifica se algum número já foi escolhido
    numeros_usados = {num for d in dados for num in d['numeros']}
    if any(num in numeros_usados for num in numeros):
        return "Erro: Alguns números já foram escolhidos.", 400

    # Salva os dados
    dados.append({'nome': nome, 'numeros': numeros})
    return "Dados salvos com sucesso!", 200

if __name__ == '__main__':
    app.run(debug=True)
