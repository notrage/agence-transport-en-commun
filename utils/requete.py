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
                [sg.Text("Peut conduire",size=(20,1)),sg.CB('Bus',key="-CK_BUS-"), sg.CB('Tram',key="-CK_TRAM-")],
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
                [sg.Text("Type de véhicule",size=(20,1)),sg.Radio('Bus','R1',key="-CK_BUS-"), sg.Radio('Tram','R1',key="-CK_TRAM-")],
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

def Ajouter_un_arret(conn:sqlite3.Connection):
    """
    Formulaire pour creer un nouvel arret

    :param conn: Connexion à la base de données
    """
    layout =    [[sg.Text("Nom de l'arret",size=(20,1)),sg.Input(key='-IMPUT_NOM-')],
                [sg.Text("Adresse de l'arret*",size=(20,1)),sg.Input(key='-IMPUT_ADR-')],
                [sg.Text("* Entrez le nom de la place/rue où se trouve l'arrêt, \nconsulter les arrêts déjà existant en cas de doutes",font=("_",8))],
                [sg.Submit('Valider',size=(15,1),pad=((5,0), (160, 10))), sg.Cancel('Retour',size=(15,1),pad=((5,0), (160, 10)))]]
    window = sg.Window('ADMIN PANEL', layout,size=(400, 300))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Retour': # quit
            break
        if event == 'Valider':
            print(values)
            nom,adr = values["-IMPUT_NOM-"],values["-IMPUT_ADR-"]
            if not nom.strip() == '':
                if not adr.strip() == '':
                    cur = conn.cursor()
                    requete = f'INSERT INTO Arrets VALUES ("{nom}","{adr}");'
                    print(requete)
                    try:
                        cur.execute(requete)
                    except sqlite3.IntegrityError:
                        sg.popup("Erreur : l'arrêt existe déjà.")
                    else:
                        sg.Popup("Ajout validé !")
                else:
                    sg.Popup("Erreur :  l'adresse ne doit pas être vide")
            else:
                sg.Popup("Erreur : le nom de l'arrêt de doit pas être vide")
    window.close()


def Afficher_table(conn:sqlite3.Connection,requete: str) -> None:
    """
    Affiche la table obtenu par la requete

    :param conn: Connexion à la base de données
    :param requete: requete à executer
    """
    cur = conn.cursor()
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

    window = sg.Window("RESULT", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Retour': # quit
            break
    window.close()

def Supprimer_une_valeur(conn:sqlite3.Connection,table:str) -> bool:
    """
    Affiche une table et permet d'en surpprimer les valeurs. 
    Dans le cas ou la table a des attributs dependants d'autres table,
    ces differentes valeurs sont supprimées aussi. 

    :param conn: Connexion à la base de données
    :param table: nom de la table. 

    :return bool: Indique si il faut recharger la page pour mettre à jour les données en cas de supression.
    """
    "Recuperation des donnees"
    cur = conn.cursor()
    requete = "SELECT * FROM " + table + ";"
    cur.execute(requete)
    rows = cur.fetchall()
    # Récuperation des noms des attributs
    header = [col[0] for col in cur.description]
    # Formatage des données
    data = [list(t) for t in rows]
    string_data = [[str(element) for element in row] for row in data]
    layout = [[sg.Text("Cliquez sur la ligne à supprimer")],
        [sg.Table(values = string_data,
                    headings=header,
                    justification='center',
                    font=("_",12),
                    key='-TABLE-',
                    enable_click_events=True,
                    auto_size_columns=True)],
            [sg.Button("Retour")]]
    
    window = sg.Window("RESULT", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Retour': # quit
            break
        
        # Supprimer un conducteur de Conducteurs et ModelesConducteurs
        if table == "Conducteurs" and event[0] == '-TABLE-' and event[2][0] != None and event[2][0] >= 0:
            popup_str = "Voulez-vous supprimer la ligne de matricule " + string_data[event[2][0]][0] + " ? \n\nLa suppression sera aussi effective dans la ligne ConducteursModeles."
            button = sg.popup(popup_str, button_type=1)
            if button == 'Yes':
                # DELETE ConducteursModeles
                requete = "DELETE FROM ConducteursModeles WHERE matricule_conducteur == " + string_data[event[2][0]][0] + ";"
                print(requete)
                cur.execute(requete)
                # DELETE Conducteurs
                requete = "DELETE FROM Conducteurs WHERE matricule_conducteur == " + string_data[event[2][0]][0] + ";"
                print(requete)
                cur.execute(requete)
                # Mise à jour visuelle
                window.close()
                return True
        if table == "Vehicules" and event[0] == '-TABLE-' and event[2][0] != None and event[2][0] >= 0:
            popup_str = "Voulez-vous supprimer la ligne du véhicule numéro " + string_data[event[2][0]][0] + " ?"
            button = sg.popup(popup_str, button_type=1)
            if button == 'Yes':
                # DELETE Vehicules
                requete = "DELETE FROM Vehicules WHERE numero_vehicule == " + string_data[event[2][0]][0] + ";"
                print(requete)
                cur.execute(requete)
                # Mise à jour visuelle
                window.close()
                return True
        if table == "Arrets" and event[0] == '-TABLE-' and event[2][0] != None and event[2][0] >= 0:
            popup_str = "Voulez-vous supprimer l'arret " + string_data[event[2][0]][0] + " ?\nCela affectera les étapes des lignes concernées par l'arrêt."
            button = sg.popup(popup_str, button_type=1)
            if button == 'Yes':
                # DELETE Etapes + Décalage des etapes concernées 
                return
    window.close()
    return False 