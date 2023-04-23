#!/usr/bin/python3

from utils import db
from utils.requete import *
import os 
try:
    import PySimpleGUI as sg
except:
    print("ATTENTION : vous n'avez pas la librairie PySimpleGUI")
    print("py -m pip install pysimplegui")

############################### GLOBAL VALUES ##################################
size=(400, 300)


def main_screen(conn:sqlite3.Connection):
    """
    Menu de base

    :param conn: Connexion à la base de données
    """
    layout = [  [sg.Button("Connexion en tant qu'Administrateur",size=(50,1))],
                [sg.Button("Connexion en tant qu'Utilisateur",size=(50,1))],
                [sg.Text("",size=(0,1))],
                [sg.Button("Quitter",size=(15,1),pad=((5,0), (155, 10)))]
            ]

    # Create the Window
    window = sg.Window('LOGIN', layout,size=size)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Quitter': # if user closes window or clicks cancel
            break
        if event == "Connexion en tant qu'Administrateur":
            admin_panel(conn)
        if event == "Connexion en tant qu'Utilisateur":
            user_panel(conn)
    window.close()

def admin_panel(conn:sqlite3.Connection):
    """
    Menu administrateur

    :param conn: Connexion à la base de données
    """
    # All the stuff inside your window.
    layout = [  [sg.Button("Visualiser une table",size=(50,1))],
                [sg.Button("Ajouter un conducteur",size=(50,1))],
                [sg.Button("Supprimer un conducteur",size=(50,1))],
                [sg.Button("Ajouter un véhicule",size=(50,1))],
                [sg.Button("Supprimer un véhicule",size=(50,1))],
                [sg.Button("Déconnexion",size=(15,1),pad=((5,0), (90, 10)))]
            ]
    window = sg.Window('ADMIN PANEL', layout,size=size)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Déconnexion': # if user closes window or clicks cancel
            break
        if event == "Ajouter un conducteur":
            Ajouter_un_conducteur(conn)
        if event == "Supprimer un conducteur":
            relancer = Supprimer_une_valeur(conn,"Conducteurs")
            while relancer:
                relancer = Supprimer_une_valeur(conn,"Conducteurs")
        if event == "Ajouter un véhicule":
            Ajouter_un_vehicule(conn)
        if event == "Supprimer un véhicule":
            relancer = Supprimer_une_valeur(conn,"Vehicules")
            while relancer:
                relancer = Supprimer_une_valeur(conn,"Vehicules")
        if event == "Visualiser une table":
            Afficher_table_menu(conn)
        
    window.close()

def user_panel(conn:sqlite3.Connection):
    """
    Menu utilisateur

    :param conn: Connexion à la base de données
    """
    # All the stuff inside your window.
    layout = [  [sg.Button("...",size=(50,1))],
                [sg.Button("...",size=(50,1))],
                [sg.Button("...",size=(50,1))],
                [sg.Button("Déconnexion",size=(15,1),pad=((5,0), (150, 10)))]
            ]
    window = sg.Window('USER', layout,size=size)
        # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Déconnexion': # if user closes window or clicks cancel
            break
    window.close()


def main():
    # Nom de la BD à créer
    db_file = "data/transports.db"

    # Créer une connexion a la BD
    conn = db.creer_connexion(db_file)
    # initiation de la db 
    db.mise_a_jour_bd(conn,"data/transports_init.sql")
    db.mise_a_jour_bd(conn, "data/insert_mtag.sql")
    #db.mise_a_jour_bd(conn,"data/transports_init_values.sql")

    # theme des UI
    sg.theme('DarkAmber')
    
    main_screen(conn)
    conn.commit()
    print("Données mises à jour")
    conn.close()
    print("Connection fermée")


if __name__ == "__main__":
    main()
