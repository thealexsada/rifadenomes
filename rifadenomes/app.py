# Implements a registration form, storing registrants in a SQLite database, with support for deregistration

from cs50 import SQL
from flask import Flask, redirect, request, jsonify, render_template

app = Flask(__name__)

db = SQL("sqlite:///rifadenomes.db")

# List of names to display with indices
NAMES = [
    "Alex", "Alice", "Bob", "Charlie", "Diana", "Edward", "Fiona", "George",
    "Hannah", "Ivy", "Jack", "Katherine", "Leo", "Mona", "Nathan",
    "Olivia", "Paul", "Quincy", "Rachel", "Sophia", "Thomas", "Ursula",
    "Victor", "Wendy", "Xander", "Yvonne", "Zane"
]


@app.route('/')
def index():
    return render_template("index.html", names=NAMES)

@app.route("/deregister", methods=["POST"])
def deregister():

    # Forget registrant
    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM registrants WHERE id = ?", id)
    return redirect("/registrants")


@app.route("/register", methods=["POST"])
def register():

    # Validate submission
    registrant = request.form.get("registrant")
    name = request.form.get("name")
    if not registrant or name not in NAMES:
        return render_template("failure.html")

    # Remember registrant
    db.execute("INSERT INTO registrants (registrant, name) VALUES(?, ?)", registrant, name)

    # Confirm registration
    return redirect("/registrants")

@app.route("/registrants")
def registrants():
    registrants = db.execute("SELECT * FROM registrants")
    return render_template("registrants.html", registrants=registrants)


@app.route('/nomes', methods=['GET'])
def nomes():
    # Extract all names already chosen
    nomes_usados = set(selection_dict.keys())
    return jsonify({
        "NAMES": [f"{str(i + 1).zfill(2)}. {name}" for i, name in enumerate(NAMES)],  # Zero-padded indices
        "taken_names": list(nomes_usados)
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
