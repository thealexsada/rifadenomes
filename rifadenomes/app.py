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
    # Fetch registered names
    registrants = db.execute("SELECT name FROM registrants")
    taken_names = {row["name"] for row in registrants}

    # Pass names and registration status to the frontend
    return render_template("index.html", names=NAMES, taken_names=taken_names)


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
    names = request.form.get("names")  # Comma-separated list of names

    if not registrant or not names:
        return render_template("failure.html", message="Nome ou registrante inválido!")

    # Split the names into a list
    selected_names = names.split(',')

    # Validate names
    invalid_names = [name for name in selected_names if name not in NAMES]
    if invalid_names:
        return render_template("failure.html", message=f"Nomes inválidos: {', '.join(invalid_names)}")

    # Check if any name is already registered
    existing = db.execute(
        "SELECT name FROM registrants WHERE name IN (?)",
        ",".join(selected_names)  # Join the names for SQL query
    )
    if existing:
        taken = [row['name'] for row in existing]
        return render_template("failure.html", message=f"Nomes já registrados: {', '.join(taken)}")

    # Register all valid names
    for name in selected_names:
        db.execute("INSERT INTO registrants (registrant, name) VALUES(?, ?)", registrant, name)

    # Redirect to the list of registrants
    return redirect("/registrants")


@app.route("/registrants")
def registrants():
    registrants = db.execute("SELECT * FROM registrants ORDER BY name ASC")
    return render_template("registrants.html", registrants=registrants)

