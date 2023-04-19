#!/usr/bin/python3

from utils import db


def select_tous_les_conducteur(conn):
    """
    Affiche la liste de tous les bateaux.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT * 
                FROM Etapes
                """)

    rows = cur.fetchall()

    for row in rows:
        print(row)


def main():
    # Nom de la BD à créer
    db_file = "data/transports.db"

    # Créer une connexion a la BD
    conn = db.creer_connexion(db_file)

    # Remplir la BD
    print("1. On crée la bd et on l'initialise avec des premières valeurs.")
    db.mise_a_jour_bd(conn, "data/transports_init.sql")
    db.mise_a_jour_bd(conn, "data/transports_validvalues.sql")
    # Lire la BD
    print("2. Liste de tous les conducteurs")
    select_tous_les_conducteur(conn)


if __name__ == "__main__":
    main()
