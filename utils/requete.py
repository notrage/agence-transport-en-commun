import PySimpleGUI as sg
import sqlite3


def Ajouter_un_conducteur(conn:sqlite3.Connection):
    """
    Ajouter un conducteur à la DB 

    :param conn: Connexion à la base de données
    """
    layout =   [[sg.Text("Matricule du conducteur",size=(20,1)),sg.Input(key='-IMPUT_MAT-')],
                [sg.Text("Nom du conducteur",size=(20,1)),sg.Input(key='-IMPUT_NOM-')],
                [sg.Text("Prenom du conducteur",size=(20,1)),sg.Input(key='-IMPUT_PRENOM-')],
                [sg.CB('Bus',key="-CK_BUS-"), sg.CB('Tram',key="-CK_TRAM-")],
                [sg.Submit('Valider',size=(15,1),pad=((5,0), (150, 10))), sg.Cancel('Retour',size=(15,1),pad=((5,0), (150, 10)))]]

    # Create the window
    window = sg.Window('ADMIN PANEL', layout,size=(400, 300))
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

def Ajouter_un_vehicule(conn:sqlite3.Connection):
    """
    Ajouter un vehicule à la DB 

    :param conn: Connexion à la base de données
    """
    layout =   [[sg.Text("Numéro du véhicule",size=(20,1)),sg.Input(key='-IMPUT_NUM-')],
                [sg.Text("Nom de la ligne desservie",size=(20,1)),sg.Input(key='-IMPUT_LIGNE-')],
                [sg.Text("Type de véhicule",size=(20,1)),sg.CB('Bus',key="-CK_BUS-"), sg.CB('Tram',key="-CK_TRAM-")],
                [sg.Text("",size=(0,1))],
                [sg.Submit('Valider',size=(15,1),pad=((5,0), (150, 10))), sg.Cancel('Retour',size=(15,1),pad=((5,0), (150, 10)))]]
    window = sg.Window('ADMIN PANEL', layout,size=(400, 300))
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


def Afficher_table_menu(conn:sqlite3.Connection):
    """
    Menu d'affichage des tables de la DB

    :param conn: Connexion à la base de données
    """
    layout =  [[sg.Button("Conducteurs",size=(50,1))],
                [sg.Button("Modeles",size=(50,1))],
                [sg.Button("Tarifs",size=(50,1))],
                [sg.Button("Lignes",size=(50,1))],
                [sg.Button("Arrets",size=(50,1))],
                [sg.Button("Vehicules",size=(50,1))],
                [sg.Button("Etapes",size=(50,1))],
                [sg.Button("ConducteursModeles",size=(50,1))],
                [sg.Text("")],
                [sg.Button("Retour",size=(15,1),pad=((5,0), (70, 10)))]]
    window = sg.Window('ADMIN PANEL', layout,size=(400, 400))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Retour': # quit
            break
        elif event != None:
            Afficher_table(conn,event)
    window.close()


def Afficher_table(conn:sqlite3.Connection,nom_table: str):
    """
    Affiche la table nom_table

    :param conn: Connexion à la base de données
    :param nom_table: Nom de la table à afficher
    """
    cur = conn.cursor()
    requete = "SELECT * FROM " + nom_table + ";"
    print(requete)
    cur.execute(requete)
    rows = cur.fetchall()
    # Récuperation des noms des attributs
    header = [col[0] for col in cur.description]
    # Formatage des données
    data = [list(t) for t in rows]
    string_data = [[str(element) for element in row] for row in data]
    layout = [[sg.Table(values = string_data,
                        headings=header,
                        justification='center',
                        font=("_",12),
                        auto_size_columns=True)],
              [sg.Button("Retour")]]

    window = sg.Window(nom_table, layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Retour': # quit
            break
    window.close()