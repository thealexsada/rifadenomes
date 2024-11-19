from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


# List of names to display with indices
all_names = [
    "Alex", "Alice", "Bob", "Charlie", "Diana", "Edward", "Fiona", "George",
    "Hannah", "Ivy", "Jack", "Katherine", "Leo", "Mona", "Nathan",
    "Olivia", "Paul", "Quincy", "Rachel", "Sophia", "Thomas", "Ursula",
    "Victor", "Wendy", "Xander", "Yvonne", "Zane"
]


# In-memory data storage (use a real database in production)
dados = []


@app.route('/')
def index():
    return render_template('index.html')  # HTML file served from the templates folder


@app.route('/nomes', methods=['GET'])
def nomes():
    # Extract all names already chosen
    nomes_usados = {nome for d in dados for nome in d['nomes']}
    # Return all names with indices and taken names
    return jsonify({
        "all_names": [f"{i + 1}. {name}" for i, name in enumerate(all_names)],  # **Format updated here**
        "taken_names": list(nomes_usados)
    })


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
