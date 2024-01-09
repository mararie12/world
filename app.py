# app.py

from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

class DatabaseManager:
    def __init__(self, database_path='blog.db'):
        self.database_path = database_path

    def execute_query(self, query, params=None):
        with sqlite3.connect(self.database_path) as conn:
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchall()

db_manager = DatabaseManager()

@app.route('/')
def index():
    try:
        users = db_manager.execute_query('SELECT * FROM users')
        return render_template('index.html', users=users)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return render_template('error.html')

@app.route('/register', methods=['POST'])
def register():
    try:
        if request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')
            password = request.form.get('password')
            confirm_password = request.form.get('confirm_password')

            # Ajout de la logique de vérification du mot de passe
            if password != confirm_password:
                error_message = "Passwords do not match. Please try again."
                return render_template('index.html', error=error_message)

            # Vérifier si l'e-mail existe déjà dans la base de données
            existing_user = db_manager.execute_query('SELECT * FROM users WHERE email = ?', (email,))
            if existing_user:
                error_message = "Email already exists. Please use a different email."
                return render_template('index.html', error=error_message)

            # Insertion dans la base de données
            db_manager.execute_query('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', (name, email, password))

            return render_template('index.html', name=name, email=email, password=password)
    except Exception as e:
        print(f"An error occurred during registration: {str(e)}")
        return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)

