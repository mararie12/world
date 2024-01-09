import sqlite3

def create_database():
    # Connexion à la base de données (crée un fichier 'blog.db' si non existant)
    conn = sqlite3.connect('blog.db')

    # Création d'un curseur pour exécuter des commandes SQL
    cursor = conn.cursor()

    # Exécution des commandes SQL depuis le fichier schema.sql
    with open('schema.sql', 'r') as file:
        sql_commands = file.read()
        cursor.executescript(sql_commands)

    # Commit pour sauvegarder les changements
    conn.commit()

    # Fermeture de la connexion
    conn.close()

if __name__ == '__main__':
    create_database()
    print('Database created successfully.')
