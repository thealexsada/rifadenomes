from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# In-memory data storage (use a real database in production)
dados = []


@app.route('/')
def index():
    return render_template('index.html')  # HTML file served from the templates folder


@app.route('/numeros', methods=['GET'])
def numeros():
    # Extract all numbers already chosen
    numeros_usados = {num for d in dados for num in d['numeros']}
    return jsonify(list(numeros_usados))  # Return the chosen numbers as JSON


@app.route('/salvar', methods=['POST'])
def salvar():
    nome = request.form['nome']
    escolhas = request.form['escolhas']
    if not escolhas:  # Handle cases where no numbers are chosen
        return "Erro: Nenhum número escolhido.", 400
    numeros = list(map(int, escolhas.split(',')))

    # Check if any number is already chosen
    numeros_usados = {num for d in dados for num in d['numeros']}
    if any(num in numeros_usados for num in numeros):
        return "Erro: Alguns números já foram escolhidos.", 400

    # Save the data
    dados.append({'nome': nome, 'numeros': numeros})
    return "Dados salvos com sucesso!", 200


if __name__ == '__main__':
    app.run(debug=True)
