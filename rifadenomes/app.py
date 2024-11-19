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
    return jsonify({
        "all_names": [f"{i + 1}. {name}" for i, name in enumerate(all_names)],
        "taken_names": list(nomes_usados)
    })

@app.route('/dicionario', methods=['GET'])
def dicionario():
    # Build the dictionary of selected names and the person who selected them
    selection_dict = {}
    for entry in dados:
        for nome in entry['nomes']:
            selection_dict[nome] = entry['nome']
    return jsonify(selection_dict)

@app.route('/salvar', methods=['POST'])
def salvar():
    nome_usuario = request.form['nome']
    escolhas = request.form['escolhas']
    if not escolhas:  # Handle cases where no names are chosen
        return "Erro: Nenhum nome escolhido.", 400
    nomes = escolhas.split(',')

    # Check if any name is already chosen
    nomes_usados = {nome for d in dados for nome in d['nomes']}
    if any(nome in nomes_usados for nome in nomes):
        return "Erro: Alguns nomes já foram escolhidos.", 400

    # Save the data
    dados.append({'nome': nome_usuario, 'nomes': nomes})
    return "Dados salvos com sucesso!", 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
