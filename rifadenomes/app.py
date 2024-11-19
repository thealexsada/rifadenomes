from flask import Flask, request, jsonify, render_template
from collections import OrderedDict

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
selection_dict = OrderedDict()  # Use OrderedDict to maintain insertion order

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nomes', methods=['GET'])
def nomes():
    # Extract all names already chosen
    nomes_usados = set(selection_dict.keys())
    return jsonify({
        "all_names": [f"{i + 1}. {name}" for i, name in enumerate(all_names)],
        "taken_names": list(nomes_usados)
    })

@app.route('/dicionario', methods=['GET'])
def dicionario():
    # Sort the dictionary keys numerically before returning
    sorted_dict = OrderedDict(sorted(
        selection_dict.items(),
        key=lambda item: extract_numeric_prefix(item[0])  # Extract numeric prefix reliably
    ))
    return jsonify(dict(sorted_dict))

def extract_numeric_prefix(name_with_index):
    """
    Extracts the numeric prefix from a string like "1. Alex" or "12. Katherine".
    """
    try:
        # Split by the first '.' and strip whitespace, then convert to int
        return int(name_with_index.split('.')[0].strip())
    except (ValueError, IndexError):
        # Fallback for unexpected formats: place at the end
        return float('inf')

@app.route('/salvar', methods=['POST'])
def salvar():
    nome_usuario = request.form['nome']
    escolhas = request.form['escolhas']
    if not escolhas:  # Handle cases where no names are chosen
        return "Erro: Nenhum nome escolhido.", 400

    nomes = escolhas.split(',')

    # Validate and preserve format
    nomes_usados = set(selection_dict.keys())
    if any(nome in nomes_usados for nome in nomes):
        return "Erro: Alguns nomes já foram escolhidos.", 400

    # Ensure names are formatted (e.g., "1. Alex") and added in order
    for nome in nomes:
        if nome not in nomes_usados:
            selection_dict[nome] = nome_usuario  # Add in insertion order

    return "Dados salvos com sucesso!", 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
