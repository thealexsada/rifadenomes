import os
import sqlite3  # Use sqlite3 to explicitly create the database file
from cs50 import SQL
from flask import Flask, redirect, request, jsonify, render_template

app = Flask(__name__)

# Path to the SQLite database
db_path = "/app/tmp/rifadenomes.db"
db = None  # Global database connection variable


def initialize_db():
    """Ensure the database file and structure exist."""
    global db
    # Ensure the directory exists
    os.makedirs("/app/tmp", exist_ok=True)

    # Create the database file if it doesn't exist
    if not os.path.exists(db_path):
        # Use sqlite3 to create the file explicitly
        with sqlite3.connect(db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS registrants (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    registrant TEXT NOT NULL,
                    name TEXT NOT NULL
                );
            """)
    
    # Connect to the database using cs50.SQL
    db = SQL(f"sqlite:///{db_path}")


@app.before_request
def setup():
    """Run before every request to ensure the database is initialized."""
    global db
    if db is None:
        initialize_db()


# List of names to display with indices
NAMES = [
    "Newton", "Isaque", "Euler", "Thales", "Leonardo", "Theo", "Heitor", "Thomas", "Edson", "Nicolas", "Willian",
    "Diogo", "Otto", "Cesar", "Joseph", "Hermes", "Juan", "Silas", "Henry", "Felipe", "Erick", "Richard", "Alberto",
    "Antony", "Robert", "Estevam", "Jorge", "Mário", "Álvaro", "Augusto", "Kelvin", "Levi", "Murilo", "Sandro",
    "Ian", "Klaus", "Dante", "Otávio", "Hector", "Oliver", "Stephen", "Ivan", "Carlos", "Claudio", "Dylan", "Caleb",
    "Thiago", "Lorenzo", "Fabricio", "Matheus", "Beatriz", "Patrícia", "Berenice", "Olívia", "Érica", "Heloisa",
    "Luna", "Edna", "Nádia", "Cecília", "Vitória", "Camila", "Aurora", "Maia", "Sandra", "Miriam", "Raquel", "Laís",
    "Samantha", "Maria", "Isis", "Laura", "Sophia", "Verônica", "Carla", "Lúcia", "Serena", "Mônica", "Sabrina",
    "Lígia", "Melissa", "Valentina", "Alba", "Renata", "Clara", "Tereza", "Flávia", "Helena", "Lavínia", "Valéria",
    "Luana", "Larissa", "Paula", "Thaís", "Letícia", "Yasmim", "Débora", "Marília", "Diana"
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
    # Get form data
    registrant = request.form.get("registrant")
    names = request.form.get("names")

    # Validate submission
    if not registrant or not names:
        return render_template("failure.html", message="Você precisa selecionar ao menos um nome e fornecer o seu nome.")

    # Split names into a list
    selected_names = names.split(',')

    # Validate names
    invalid_names = [name for name in selected_names if name not in NAMES]
    if invalid_names:
        return render_template("failure.html", message=f"Nomes inválidos: {', '.join(invalid_names)}")

    # Check for already registered names
    placeholders = ', '.join('?' for _ in selected_names)
    query = f"SELECT name FROM registrants WHERE name IN ({placeholders})"
    existing = db.execute(query, *selected_names)

    if existing:
        taken = [row['name'] for row in existing]
        return render_template("failure.html", message=f"Nomes já registrados: {', '.join(taken)}")

    # Register valid names
    for name in selected_names:
        db.execute("INSERT INTO registrants (registrant, name) VALUES(?, ?)", registrant, name)

    return redirect("/registrants")


@app.route("/registrants")
def registrants():
    registrants = db.execute("SELECT * FROM registrants ORDER BY name ASC")
    return render_template("registrants.html", registrants=registrants)


@app.route("/admin/registrants", methods=["GET"])
def view_registrants():
    # Fetch all registrants
    registrants = db.execute("SELECT * FROM registrants ORDER BY name ASC")
    return jsonify(registrants)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
