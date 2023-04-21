#!/usr/bin/python3

from utils import db
from utils.requete import *
import os 
try:
    import PySimpleGUI as sg
except:
    print("ATTENTION : vous n'avez pas la librairie PySimpleGUI")
    print("py -m pip install pysimplegui")


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
    layout = [  [sg.Button("Connexion en tant qu'Administrateur")],
                [sg.Button("Connexion en tant qu'Utilisateur")],
                [sg.Button("Quitter")]
            ]

    # Create the Window
    window = sg.Window('Connection', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Quitter': # if user closes window or clicks cancel
            break
        if event == "Connexion en tant qu'Administrateur":
            admin_panel(conn)

def admin_panel(conn):
    # All the stuff inside your window.
    layout = [  [sg.Button("Ajouter un conducteur")],
                [sg.Button("Ajouter un véhicule")],
                [sg.Button("Déconnexion")]
            ]
    window = sg.Window('ADMIN PANEL', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Déconnexion': # if user closes window or clicks cancel
            break
        if event == "Ajouter un conducteur":
            Ajouter_un_conducteur(conn)
        if event == "Ajouter un véhicule":
            Ajouter_un_vehicule(conn)
    window.close()


def main():
    # Nom de la BD à créer
    db_file = "data/transports.db"

    # Créer une connexion a la BD
    conn = db.creer_connexion(db_file)
    # initiation de la db 
    db.mise_a_jour_bd(conn,"data/transports_init.sql")
    db.mise_a_jour_bd(conn,"data/transports_init_values.sql")
    sg.theme('DarkAmber') # GUI theme
    main_screen(conn)
    conn.commit()
    print("Données mises à jour")
    conn.close()
    print("Connexion fermée")


if __name__ == "__main__":
    main()
