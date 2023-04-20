#!/usr/bin/python3

from utils import db
from utils.requete import *
import PySimpleGUI as sg

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

def main_screen(conn):
    # All the stuff inside your window.
    layout = [  [sg.Button("Connexion en tant qu'Administrateur")],
                [sg.Button("Connexion en tant qu'Utilisateur")],
                [sg.Button("Déconnexion")]
            ]

    # Create the Window
    window = sg.Window('Connection', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == "Connexion en tant qu'Administrateur":
            window.close()
            Ajouter_un_conducteur(conn)
        if event == sg.WIN_CLOSED or event == 'Déconnexion': # if user closes window or clicks cancel
            break

def main():
    # Nom de la BD à créer
    db_file = "data/transports.db"

    # Créer une connexion a la BD
    conn = db.creer_connexion(db_file)
    sg.theme('DarkAmber') # GUI theme
    main_screen(conn)



if __name__ == "__main__":
    main()
