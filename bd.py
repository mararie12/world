import sqlite3

def afficher_contenu_table_users():
    try:
        # Connexion à la base de données
        conn = sqlite3.connect('blog.db')
        cursor = conn.cursor()

        # Exécution d'une requête SELECT pour récupérer toutes les données de la table users
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()

        # Affichage des données de la table users
        print("Contenu de la table 'users':")
        for row in rows:
            print(row)

    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")

    finally:
        # Fermeture de la connexion
        conn.close()

def afficher_contenu_table_posts():
    try:
        # Connexion à la base de données
        conn = sqlite3.connect('blog.db')
        cursor = conn.cursor()

        # Exécution d'une requête SELECT pour récupérer toutes les données de la table posts
        cursor.execute('SELECT * FROM posts')
        rows = cursor.fetchall()

        # Affichage des données de la table posts
        print("\nContenu de la table 'posts':")
        for row in rows:
            print(row)

    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")

    finally:
        # Fermeture de la connexion
        conn.close()

if __name__ == '__main__':
    afficher_contenu_table_users()
    afficher_contenu_table_posts()
