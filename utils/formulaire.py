import PySimpleGUI as sg
import sqlite3


def Ajouter_un_conducteur(conn:sqlite3.Connection):
    """
    Ajouter un conducteur à la DB 

    :param conn: Connexion à la base de données
    """
    layout =   [[sg.Text("Nom du conducteur",size=(20,1)),sg.Input(key='-IMPUT_NOM-')],
                [sg.Text("Prenom du conducteur",size=(20,1)),sg.Input(key='-IMPUT_PRENOM-')],
                [sg.Text("Peut conduire",size=(20,1)),sg.CB('Bus',key="-CK_BUS-"), sg.CB('Tram',key="-CK_TRAM-")],
                [sg.Text("")],
                [sg.Submit('Valider',size=(15,1)), sg.Cancel('Retour',size=(15,1))]]

    # Create the window
    window = sg.Window('ADMIN PANEL', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Retour': # quit
            break
        # Vérification de la validité des données
        if event == 'Valider':
            nom,prenom,bus,tram = str(values['-IMPUT_NOM-']),str(values['-IMPUT_PRENOM-']),values['-CK_BUS-'],values['-CK_TRAM-']
            # Nom/prenom non vide
            if not nom.strip() == '' and not prenom.strip() == '':
                # Verification que bus et/ou tram est coché
                if bus or tram:
                    cur = conn.cursor()

                    # Récuperation du premier matricule disponible
                    requete = """WITH FreeMat AS (
                                    SELECT A.matricule_conducteur AS matricule_conducteur,B.matricule_conducteur AS NullMat
                                    FROM Conducteurs A LEFT JOIN Conducteurs B ON (A.matricule_conducteur = B.matricule_conducteur - 1)
                                )
                                SELECT MIN(matricule_conducteur + 1)	
                                FROM FreeMat
                                WHERE NullMat IS NULL;"""
                    print(requete)
                    cur.execute(requete)
                    rows = cur.fetchall()
                    mat = str(rows[0][0])
                    # Execution du SQL 
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
                        conn.commit()
                else:
                    sg.Popup("Erreur : le conducteur doit pouvoir conduire un tram et/ou un bus")
            else:
                sg.Popup("Erreur : le nom et le prenom ne peuvent pas être vide")
    window.close()

def Ajouter_un_vehicule(conn:sqlite3.Connection):
    """
    Ajouter un vehicule à la DB 

    :param conn: Connexion à la base de données
    """
    layout =   [[sg.Text("Nom de la ligne desservie",size=(20,1)),sg.Input(key='-IMPUT_LIGNE-')],
                [sg.Text("Type de véhicule",size=(20,1)),sg.Radio('Bus','R1',key="-CK_BUS-"), sg.Radio('Tram','R1',key="-CK_TRAM-")],
                [sg.Text("")],
                [sg.Submit('Valider',size=(15,1)), sg.Cancel('Retour',size=(15,1))]]
    window = sg.Window('ADMIN PANEL', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Retour': # quit
            break
        # Vérification de la validité des données
        if event == 'Valider':
            ligne,bus,tram = values['-IMPUT_LIGNE-'],values['-CK_BUS-'],values['-CK_TRAM-']
            if not ligne.strip() == '':
                if (bus or tram) and not (bus and tram):
                    # Récuperation du premier numéro de bus disponible
                    cur = conn.cursor()
                    requete = """WITH FreeNum AS (
                                    SELECT A.numero_vehicule AS numero_vehicule,B.numero_vehicule AS NullNum
                                    FROM Vehicules A LEFT JOIN Vehicules B ON (A.numero_vehicule = B.numero_vehicule - 1)
                                )
                                SELECT MIN(numero_vehicule + 1)	
                                FROM FreeNum
                                WHERE NullNum IS NULL;"""
                    print(requete)
                    cur.execute(requete)
                    rows = cur.fetchall()
                    num = str(rows[0][0])
                    if bus:
                        requete = f"INSERT INTO Vehicules VALUES ({num},'Bus','{ligne}');"
                    if tram:
                        requete = "INSERT INTO Vehicules VALUES (" + num +",'Tram','" + ligne + "');"
                    print(requete)
                    try:
                        cur.execute(requete)
                    except sqlite3.IntegrityError:
                        sg.popup("Erreur : le numéro de véhicule n'est pas disponible et/ou la ligne n'existe pas.")
                    else:
                        sg.Popup("Ajout validé !")
                        conn.commit()
                else:
                    sg.Popup("Erreur : le véhicule doit être un bus OU un tram")
            else:
                sg.Popup("Erreur : le nom de la ligne ne doit pas être vide")
    window.close()

def Ajouter_un_arret(conn:sqlite3.Connection):
    """
    Formulaire pour creer un nouvel arret

    :param conn: Connexion à la base de données
    """
    layout =    [[sg.Text("Nom de l'arret",size=(20,1)),sg.Input(key='-IMPUT_NOM-')],
                [sg.Text("Adresse de l'arret*",size=(20,1)),sg.Input(key='-IMPUT_ADR-')],
                [sg.Text("* Entrez le nom de la place/rue où se trouve l'arrêt, \nconsulter les arrêts déjà existant en cas de doutes",font=("_",8))],
                [sg.Text("")],
                [sg.Submit('Valider',size=(15,1)), sg.Cancel('Retour',size=(15,1))]]
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
                        conn.commit()
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
    # Récuperation des données
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
            popup_str = "Voulez-vous supprimer la ligne de matricule " + string_data[event[2][0]][0] + " ? \n\nLa suppression sera aussi effective dans la table ConducteursModeles."
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
                conn.commit()
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
                conn.commit()
                window.close()
                return True
        if table == "Arrets" and event[0] == '-TABLE-' and event[2][0] != None and event[2][0] >= 0:
            nom_arret = string_data[event[2][0]][0]
            popup_str = "Voulez-vous supprimer l'arret " + nom_arret + " ?\nCela affectera les étapes des lignes concernées par l'arrêt et décalera au besoin le rang des autres arrêts."
            button = sg.popup(popup_str, button_type=1)
            if button == 'Yes':
                # DELETE Etapes + Décalage des etapes concernées 
                # Recuperation des lignes concernés ainsi que des rang :
                requete = f"""  
                                SELECT nom_ligne, rang_etape FROM 
                                Etapes WHERE nom_arret == "{nom_arret}";"""
                print(requete)
                cur.execute(requete)
                rows = cur.fetchall()
                # Décalage des numéros d'etapes sur chaque ligne
                for (ligne,etape) in rows:
                    requete = f"""  
                                    UPDATE Etapes 
                                    SET rang_etape = rang_etape - 1 
                                    WHERE nom_ligne == "{ligne}" AND rang_etape > {etape};"""
                    print(requete)
                    cur.execute(requete)
                requete = f"""  
                                DELETE FROM Etapes 
                                WHERE nom_arret == "{nom_arret}";"""
                print(requete)
                cur.execute(requete)
                requete = f"""  
                                DELETE FROM Arrets 
                                WHERE nom_arret == "{nom_arret}";"""
                print(requete)
                cur.execute(requete)    
                conn.commit()
                window.close()
                return True
    window.close()
    return False 

def Supprimer_etape_ligne(conn:sqlite3.Connection,nom_ligne:str):
    """
    Affiche la table des etapes relative a la ligne nom_ligne 
    et permet de supprimer une etape en decalant tout les rang

    :param conn: Connexion à la base de données
    :param nom_ligne: nom de la ligne. 

    :return bool: Indique si il faut recharger la page pour mettre à jour les données en cas de supression.
    """
    # Récuperation des arret de la ligne voulue
    cur = conn.cursor()
    requete = f"""
                SELECT nom_arret,rang_etape
                FROM Etapes 
                WHERE nom_ligne = "{nom_ligne}"
                ORDER BY rang_etape;"""
    print(requete)
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
        if event[0] == '-TABLE-' and event[2][0] != None and event[2][0] >= 0:
            nom_arret = string_data[event[2][0]][0]
            rang_etape = string_data[event[2][0]][1]
            popup_str = f"Voulez-vous supprimer l'arret {nom_arret} de la ligne {nom_ligne} ?"
            button = sg.popup(popup_str, button_type=1)
            if button == 'Yes':
                requete = f"""  
                                UPDATE Etapes 
                                SET rang_etape = rang_etape - 1 
                                WHERE nom_ligne == "{nom_ligne}" AND rang_etape > {rang_etape};"""
                print(requete)
                cur.execute(requete)
                requete = f"""  
                                DELETE FROM Etapes 
                                WHERE nom_arret == "{nom_arret}" AND nom_ligne == "{nom_ligne}";"""
                print(requete)
                cur.execute(requete)
                conn.commit()
                window.close()
                return True
    window.close()
    return False

def Ajouter_etape_ligne(conn:sqlite3.Connection,nom_ligne:str):
    """
    Affiche la table de la liste des arret disponible poru la ligne, et permet de chosir un rang à cet arrêt
    :param conn: Connexion à la base de données
    :param nom_ligne: nom de la ligne. 

    :return bool: Indique si il faut recharger la page pour mettre à jour les données en cas d'ajout.
    """
    cur = conn.cursor()
    # Récuperer le rang d'etape max de la ligne
    requete = f"""  SELECT MAX(rang_etape)
                    FROM Etapes
                    WHERE nom_ligne = "{nom_ligne}";
                """
    print(requete)
    cur.execute(requete)
    rang_max = cur.fetchall()[0][0]
    # Récuperer les arrêts disponibles
    
    requete = f"""
                    SELECT nom_arret 
                    FROM Arrets
                    EXCEPT
                    SELECT nom_arret
                    FROM Etapes
                    WHERE nom_ligne = "{nom_ligne}";
                """

    print(requete)
    cur.execute(requete)
    rows = cur.fetchall()
    # Récuperation des noms des attributs
    header = [col[0] for col in cur.description]
    # Formatage des données
    data = [list(t) for t in rows]
    string_data = [[str(element) for element in row] for row in data]
    layout = [  [sg.Text("Sélectionnez l'arrêt à ajouter")],
                [sg.Table(values = string_data,
                    headings=header,
                    justification='center',
                    font=("_",12),
                    key='-TABLE-',
                    enable_events=True,
                    auto_size_columns=True)],
                [sg.Text("Rang de l'etape:") ,sg.Combo([str(x) for x in range(1,rang_max+2)],default_value='1',size=(5,1),key='-RANG-')],
                [sg.Submit('Valider',size=(10,1)), sg.Cancel('Retour',size=(10,1))]]
    window = sg.Window("RESULT", layout)
    while True:
        event, values = window.read()
        print(event)
        if event == sg.WIN_CLOSED or event == 'Retour': # quit
            break
        if event == "Valider":
            if values['-TABLE-'] != []:
                if values['-RANG-'].isdigit() and int(values['-RANG-']) >= 1 and int(values['-RANG-']) <= rang_max+1:
                    nom_arret = string_data[values['-TABLE-'][0]][0]
                    rang_etape = values['-RANG-']
                    requete = f"""
                                UPDATE Etapes 
                                SET rang_etape = rang_etape + 1 
                                WHERE nom_ligne == "{nom_ligne}" AND rang_etape >= {rang_etape};"""
                    print(requete)
                    cur.execute(requete)
                    requete = f"""
                                INSERT INTO Etapes VALUES ("{nom_ligne}","{nom_arret}",{rang_etape});"""
                    print(requete)
                    cur.execute(requete)
                    conn.commit()
                    sg.popup("Ajout validé !")
                else:
                    sg.popup("Le rang doit être un entier de la liste proposée")
            else:
                sg.popup("Séléctionnez l'arrêt à ajouter")
    window.close()

def Modifier_une_ligne(conn:sqlite3.Connection):
    cur = conn.cursor()
    requete = """
                    SELECT nom_ligne 
                    FROM Lignes;"""
    cur.execute(requete)
    rows = cur.fetchall()
    ligne_liste = [x[0] for x in rows]
    layout = [[]]
    key_list = []
    for ligne in ligne_liste:
        key_list.append(ligne)
        layout[0].append(sg.Radio(ligne,"R1",key=ligne))
    layout+=[[sg.Radio("Ajouter un arrêt","R2",key="ADD"), sg.Radio("Supprimer un arrêt","R2",key="DEL")],
            [sg.Text("")],
            [sg.Submit('Valider',size=(15,1)), sg.Cancel('Retour',size=(15,1))]]
    window = sg.Window("MODIFIER UNE LIGNE", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Retour': # quit
            break
        if event == "Valider":
            ligne,commande = None, None 
            for key,val in values.items():
                if val and key in key_list:
                    ligne = key
                elif val:
                    commande = key
            if not ligne:
                sg.popup("Selectionnez une ligne")
            elif not commande:
                sg.popup("Selectionnez une action à effectuer")
            else:
                if commande == "DEL":
                    window.Hide()
                    relancer = Supprimer_etape_ligne(conn,ligne)
                    while relancer:
                        relancer = Supprimer_etape_ligne(conn,ligne)
                    window.UnHide()  
                else:
                    window.Hide()
                    relancer = Ajouter_etape_ligne(conn,ligne)
                    while relancer:
                        relancer = Ajouter_etape_ligne(conn,ligne)
                    window.UnHide()  

    window.close()
    