import PySimpleGUI as sg
import sqlite3

from utils.requete import Requete


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
                    requete: Requete = Requete(conn)
                    cur = requete.select_min_mat_conducteur()
                    rows = cur.fetchall()
                    mat = str(rows[0][0])
                    # Execution du SQL
                    requete.insert_conducteur(mat, nom, prenom, bus, tram)
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
                if (bus or tram):
                    # Récuperation du premier numéro de bus disponible
                    requete: Requete = Requete(conn)
                    cur = requete.select_min_num_vehicule()
                    rows = cur.fetchall()
                    num = str(rows[0][0])
                    requete.insert_vehicule(num, bus, tram, ligne)
                    sg.Popup("Ajout validé !")
                    conn.commit()
                else:
                    sg.Popup("Erreur : le type de véhicule doit être définit")
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
    window = sg.Window('ADMIN PANEL', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Retour': # quit
            break
        if event == 'Valider':
            print(values)
            nom,adr = values["-IMPUT_NOM-"],values["-IMPUT_ADR-"]
            if not nom.strip() == '':
                if not adr.strip() == '':
                    requete: Requete = Requete(conn)
                    valide = requete.insert_arret(nom, adr)
                    if not valide:
                        sg.popup("Erreur : l'arrêt existe déjà.")
                    else: 
                        sg.popup("Ajout validé !")
                        conn.commit()
                else:
                    sg.Popup("Erreur :  l'adresse ne doit pas être vide")
            else:
                sg.Popup("Erreur : le nom de l'arrêt de doit pas être vide")
    window.close()


def Afficher_table(cur: sqlite3.Cursor) -> None:
    """
    Affiche la table obtenu par la requete

    :param conn: Connexion à la base de données
    :param requete: requete à executer
    """
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
    requete: Requete = Requete(conn)
    cur = requete.select_all_from(table)
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
                requete.delete_conducteur(string_data[event[2][0]][0])
                # DELETE Conducteurs
                conn.commit()
                # Mise à jour visuelle
                window.close()
                return True
        if table == "Vehicules" and event[0] == '-TABLE-' and event[2][0] != None and event[2][0] >= 0:
            popup_str = "Voulez-vous supprimer la ligne du véhicule numéro " + string_data[event[2][0]][0] + " ?"
            button = sg.popup(popup_str, button_type=1)
            if button == 'Yes':
                # DELETE Vehicules
                requete.delete_vehicule(string_data[event[2][0]][0])
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
                requete.delete_arret(nom_arret)
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
    requete: Requete = Requete(conn)
    cur = requete.select_from_etapesbase_nom_arret_rang_etape_where_nom_ligne(nom_ligne)
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
                requete.update_etapesbase_rang_etape_where_ligne_and_rang_etape_greater_or_equal(nom_ligne, rang_etape)
                requete.delete_etapesbase_where_nom_arret_and_nom_ligne(nom_arret, nom_ligne)
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
    requete: Requete = Requete(conn)
    cur = requete.select_from_etapes_max_rang_etape_where_nom_ligne(nom_ligne)
    rang_max = cur.fetchall()[0][0]
    # Récuperer les arrêts disponibles
    cur = requete.select_from_arrets_nom_arret_exept_in_etapes_where_nom_ligne(nom_ligne)
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
                    requete.update_etapesbase_rang_etape_where_ligne_and_rang_etape_greater_or_equal(nom_ligne, rang_etape)
                    requete.insert_etapesbase(nom_ligne, nom_arret, rang_etape)
                    conn.commit()
                    sg.popup("Ajout validé !")
                    window.close()
                    return True 
                else:
                    sg.popup("Le rang doit être un entier de la liste proposée")
            else:
                sg.popup("Séléctionnez l'arrêt à ajouter")
    window.close()
    return False

def Modifier_une_ligne(conn:sqlite3.Connection):
    requete: Requete = Requete(conn)
    cur = requete.select_from_lignes_nom_ligne()
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