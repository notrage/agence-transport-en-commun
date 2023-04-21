import PySimpleGUI as sg
import sqlite3

def Ajouter_un_conducteur(conn):
    """
    Ajouter un conducteur à la DB 

    :param conn: Connexion à la base de données
    """
    layout =   [[sg.Text("Matricule du conducteur"),sg.Input(key='-IMPUT_MAT-')],
                [sg.Text("Nom du conducteur"),sg.Input(key='-IMPUT_NOM-')],
                [sg.Text("Prenom du conducteur"),sg.Input(key='-IMPUT_PRENOM-')],
                [sg.CB('Bus',key="-CK_BUS-"), sg.CB('Tram',key="-CK_TRAM-")],
                [sg.Submit('Valider'), sg.Cancel('Retour')]]

    # Create the window
    window = sg.Window('ADMIN PANEL', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Retour': # quit
            break
        # Vérification de la validité des données
        if event == 'Valider':
            print(values)
            mat,nom,prenom,bus,tram = values['-IMPUT_MAT-'],str(values['-IMPUT_NOM-']),str(values['-IMPUT_PRENOM-']),values['-CK_BUS-'],values['-CK_TRAM-']
            # Matricule est un entier
            if mat.isdigit():
                # Matricule positif
                if int(mat) > 0:
                    # Nom/prenom non vide
                    if not nom.strip() == '' and not prenom.strip() == '':
                        # Verification que bus et/ou tram est coché
                        if bus or tram:
                            # Execution du SQL 
                            cur = conn.cursor()
                            requete = "INSERT INTO Conducteurs VALUES (" + mat +",'" + nom + "','" + prenom +"');"
                            print(requete)
                            try:
                                cur.execute(requete)
                            except sqlite3.IntegrityError:
                                sg.Popup("Erreur : matricule non disponible")
                            else:
                                if bus: 
                                    requete = "INSERT INTO ConducteursModeles VALUES (" + mat +",'Bus');"
                                    print(requete)
                                    cur.execute(requete)
                                if tram: 
                                    requete = "INSERT INTO ConducteursModeles VALUES (" + mat +",'Tram');"
                                    print(requete)
                                    cur.execute(requete)
                                sg.Popup("Ajout validé !")
                        else:
                            sg.Popup("Erreur : le conducteur doit pouvoir conduire un tram et/ou un bus")
                    else:
                        sg.Popup("Erreur : le nom et le prenom ne peuvent pas être vide")
                else:
                    sg.Popup("Erreur : le matricule doit être un positif")
            else:
                sg.Popup("Erreur : le matricule doit être un nombre entier positif")
    window.close()

def Ajouter_un_vehicule(conn):
    """
    Ajouter un vehicule à la DB 

    :param conn: Connexion à la base de données
    """
    layout =   [[sg.Text("Numéro du véhicule"),sg.Input(key='-IMPUT_NUM-')],
                [sg.Text("Nom de la ligne desservie"),sg.Input(key='-IMPUT_LIGNE-')],
                [sg.Text("Type de véhicule"),sg.CB('Bus',key="-CK_BUS-"), sg.CB('Tram',key="-CK_TRAM-")],
                [sg.Submit('Valider'), sg.Cancel('Retour')]]
    window = sg.Window('ADMIN PANEL', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Retour': # quit
            break
        # Vérification de la validité des données
        if event == 'Valider':
            print(values)
            num,ligne,bus,tram = values['-IMPUT_NUM-'],values['-IMPUT_LIGNE-'],values['-CK_BUS-'],values['-CK_TRAM-']
            if num.isdigit() and int(num) > 0:
                if not ligne.strip() == '':
                    if (bus or tram) and not (bus and tram):
                        cur = conn.cursor()
                        if bus:
                            requete = "INSERT INTO Vehicules VALUES (" + num +",'Bus','" + ligne + "');"
                        if tram:
                            requete = "INSERT INTO Vehicules VALUES (" + num +",'Tram','" + ligne + "');"
                        print(requete)
                        try:
                            cur.execute(requete)
                        except sqlite3.IntegrityError:
                            sg.popup("Erreur : le numéro de véhicule n'est pas disponible et/ou la ligne n'existe pas.")
                        else:
                            sg.Popup("Ajout validé !")
                    else:
                        sg.Popup("Erreur : le véhicule doit être un bus OU un tram")
                else:
                    sg.Popup("Erreur : le nom de la ligne ne doit pas être vide")
            else:
                sg.Popup("Erreur : le numéro du vehicule doit être un nombre positif")
    window.close()

