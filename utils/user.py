import PySimpleGUI as sg
import sqlite3
from utils.admin import *

class ArretNodes:
    def  __init__(self, arret, ligne):
        self.arret = arret
        self.voisin = list()
        self.ligne = ligne
        # Evite les répétitions dans les DFS
        self.marque = False 
    def __str__(self):
        return self.arret + " " + self.ligne
    def ajouter_voisin(self,v):
        self.voisin.append(v)
    def voisins(self):
        return self.voisin
    def marquer(self):
        self.marque = True
    def est_marque(self):
        return self.marque 

class File:
    def  __init__(self):
        self.file = []
        self.curseur = 0
    def enfiler(self,valeur):
        self.file.append(valeur)
    def defiler(self):
        self.curseur += 1
        return self.file[self.curseur - 1]
    def est_vide(self):
        return self.curseur == len(self.file)

def Trouver_un_chemin(conn:sqlite3.Connection):
    """
    Formulaire de selection de 2 arrêt afin de trouver un parcours entre

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    # récuperation de la liste des arrêts et de leurs adresses 
    requete = """
                    SELECT nom_arret, adresse_arret
                    FROM Arrets;"""
    print(requete)
    cur.execute(requete)
    rows = cur.fetchall()
    # Récuperation des noms des attributs
    header = [col[0] for col in cur.description]
    # Formatage des données
    data = [list(t) for t in rows]
    string_data = [[str(element) for element in row] for row in data]
    layout = [  [sg.Text("Départ",font=("_",12)),sg.Push(),sg.Text("Arrivée",font=("_",12))],
                [sg.Table(values = string_data,
                    headings=header,
                    justification='center',
                    font=("_",12),
                    key='-DEP-',
                    enable_events=True,
                    auto_size_columns=True),
                sg.Table(values = string_data,
                    headings=header,
                    justification='center',
                    font=("_",12),
                    key='-ARR-',
                    enable_events=True,
                    auto_size_columns=True)],
                [sg.Submit('Valider',size=(10,1)), sg.Cancel('Retour',size=(10,1))]]
    window = sg.Window("RESULT", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Retour': # quit
            break
        # Vérification de la validité des données
        if event == 'Valider':
            if values['-DEP-'] != [] and values['-ARR-']:
                ArretDepart = string_data[values['-DEP-'][0]][0]
                ArretArrivee = string_data[values['-ARR-'][0]][0]
                NodeDepart,NodeArrivee = Construire_graph(conn,ArretDepart,ArretArrivee)
                chemin = Parcours_en_largeur(NodeDepart,NodeArrivee)
                # Formatage des donnees 
                str_chemin = ""
                for arret in chemin:
                    str_chemin += arret.arret + " -> "
                str_chemin = str_chemin[:-3] + "\nTemps estimé : " + str(len(chemin) * 2) + "min"
                sg.popup(str_chemin)
            else:
                sg.popup("Séléctionnez un départ et une arrivée")
    window.close()


def Parcours_en_largeur(NodeDepart:ArretNodes, NodeArrivee:ArretNodes):
    """
    Parcours dans le graphe de nodes afin de trouver un chemin entre NodeDepart et NodeArrivee

    :param NodeDepart: ArretNodes de départ
    :param NodeArrivee: ArretNodes d'arrivée
    """
    f = File()
    f.enfiler([NodeDepart,0,[NodeDepart]])
    NodeDepart.marquer()
    while not f.est_vide():
        [s,dist,chemin] = f.defiler()
        for v in s.voisins():
            if v.arret == NodeArrivee.arret:
                print("Chemin trouvé")
                return chemin + [NodeArrivee]
            if not v.est_marque():
                f.enfiler([v,dist+1,chemin+[v]])
                v.marquer()
    print("Pas de chemin trouvé")
    return []

def Construire_graph(conn:sqlite3.Connection, ArretDepart:str, ArretArrivee:str):
    """
    Méthode de construction du graphe des arrêts et récuperation des Nodes de départ et d'arrivée

    :param conn: Connexion à la base de données
    :param ArretDepart: Nom de l'arrêt point de départ
    :param ArretArrivee: Nom de l'arrêt arrivée
    """
    node_dict = {}
    cur = conn.cursor()
    NodeDepart = None
    NodeArrivee = None
    # On récupere la liste des arrêt pour créer toutes les nodes 
    requete = """   
                    SELECT nom_arret, nom_ligne
                    FROM Etapes;"""
    print(requete)
    cur.execute(requete)
    # Construction de toute les nodes
    for arret in cur.fetchall():
        a = arret[0]
        ligne = arret[1]
        if not node_dict.get(arret,False):
            node_dict[a] = ArretNodes(a,ligne)
            if a == ArretDepart:
                NodeDepart = node_dict[a]
            if a == ArretArrivee:
                NodeArrivee = node_dict[a]
    # Ajout des voisins 
    # Pour des soucis de performances (la librairie sqlite a beaucoup de mal à recuperer une grande quantité de données d'un coup)
    # Nous divisons pour chaque ligne les requetes

    requete = """   
                    SELECT nom_ligne
                    FROM Lignes;"""
    print(requete)
    cur.execute(requete)
    liste_ligne = cur.fetchall()
    for ligne in liste_ligne:
        nom_ligne = ligne[0]
        requete = f"""   
                    SELECT A.nom_arret, B.nom_arret 
                    FROM Etapes A 
                    JOIN Etapes B ON (A.nom_ligne = B.nom_ligne AND 
                                    (A.rang_etape = B.rang_etape - 1 OR A.rang_etape = B.rang_etape + 1))
                    WHERE A.nom_ligne = "{nom_ligne}";"""
        cur.execute(requete)
        for arrets in cur.fetchall():
            node_a = node_dict[arrets[0]]
            node_b = node_dict[arrets[1]]
            node_a.ajouter_voisin(node_b)
    return NodeDepart,NodeArrivee

def Information_sur_un_arret(conn:sqlite3.Connection):
    """
    Formulaire de selection d'un arrêt pour recevoir des informations supplémentaires

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    # récuperation de la liste des arrêts et de leurs adresses 
    requete = """
                    SELECT nom_arret, adresse_arret
                    FROM Arrets;"""
    print(requete)
    cur.execute(requete)
    rows = cur.fetchall()
    # Récuperation des noms des attributs
    header = [col[0] for col in cur.description]
    # Formatage des données
    data = [list(t) for t in rows]
    string_data = [[str(element) for element in row] for row in data]
    layout = [[sg.Text("Cliquez sur un arrêt pour recevoir des informations")],
                [sg.Table(values = string_data,
                headings=header,
                justification='center',
                font=("_",12),
                key='-TABLE-',
                enable_click_events=True,
                auto_size_columns=True)],
            [sg.Cancel('Retour',size=(10,1))]]
    window = sg.Window("RESULT", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Retour': # quit
            break
        # Vérification de la validité des données
        if event[0] == '-TABLE-' and event[2][0] != None and event[2][0] >= 0:
            nom_arret = string_data[event[2][0]][0]
            requete = f"""
                    SELECT A.nom_ligne, CASE WHEN A.prochain_depart_en_minute == 0 THEN 'IMMINENT'
                        ELSE A.prochain_depart_en_minute END AS prochain_depart_en_minute, 
                        IFNULL(B.nom_arret,'TERMINUS') AS prochain_arret,
                        arrive_ligne AS en_direction_de
                    FROM Etapes A LEFT JOIN Etapes B ON(A.nom_ligne = B.nom_ligne AND A.rang_etape = B.rang_etape - 1)
                    JOIN Lignes USING(nom_ligne)
                    WHERE  A.nom_arret = "{nom_arret}";"""
            window.Hide()
            Afficher_table(conn,requete)
            window.UnHide()
    window.close()



def Information_sur_un_tarif(conn:sqlite3.Connection):
    """
    Formulaire de selection d'un tarif

    :param conn: Connexion à la base de données
    """ 
    cur = conn.cursor()
    # récuperation de la liste de type de véhicule présente dans les tarifs
    requete = """
                    SELECT DISTINCT(type_modele)
                    FROM Tarifs;"""
    print(requete)
    cur.execute(requete)
    liste_type_vehicule = [str(t[0]) for t in cur.fetchall()]
    radio_liste_type_vehicule = [sg.Radio(x,'R1',key=f"{x}") for x in liste_type_vehicule]
    requete = """
                    SELECT DISTINCT(duree_tarif)
                    FROM Tarifs;"""
    print(requete)
    cur.execute(requete)
    liste_duree = [str(t[0]) for t in cur.fetchall()]
    radio_liste_duree = [sg.Radio(x,'R2',key=f"{x}") for x in liste_duree]
    layout =   [radio_liste_type_vehicule,
                radio_liste_duree,
                [sg.Submit('Valider',size=(15,1)), sg.Cancel('Retour',size=(15,1))]]
    window = sg.Window('ADMIN PANEL', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Retour': # quit
            break
        if event == 'Valider':
            type_vehicule = None 
            duree = None 
            for key,value in values.items():
                if value and key in liste_type_vehicule:
                    type_vehicule = key
                if value and key in liste_duree:
                    duree = key
            requete = f"""
                    SELECT DISTINCT nom_ligne AS liste_ligne_desservie, prix_tarif AS prix
                    FROM Tarifs JOIN Vehicules USING(type_modele)
                    WHERE type_modele = "{type_vehicule}" AND duree_tarif = "{duree}";"""
            print(requete)
            window.Hide()
            Afficher_table(conn,requete)
            window.UnHide()
    window.close()
    
def Verifier_les_effectifs(conn:sqlite3.Connection):
    """
    Récuperation des informations sur les effectifs

    :param conn: Connection la bdd sqlite
    """
    requete = """WITH Effectifs AS (
                            SELECT type_modele, COUNT(DISTINCT numero_vehicule) AS nombre_de_vehicules, COUNT(DISTINCT matricule_conducteur) AS nombre_de_conducteurs
                            FROM Vehicules JOIN ConducteursModeles USING(type_modele)
                            GROUP BY type_modele)
                        SELECT type_modele, nombre_de_vehicules, nombre_de_conducteurs, 
                            CASE WHEN nombre_de_vehicules > nombre_de_conducteurs THEN 'SOUS-EFFECTIF DE CONDUCTEURS'
                                WHEN nombre_de_vehicules < nombre_de_conducteurs THEN 'SUR-EFFECTIF DE CONDUCTEURS'
                                ELSE 'EFFECTIF IDEAL' END AS verficiation_effectif,
                            nombre_de_vehicules - nombre_de_conducteurs AS difference
                        FROM Effectifs"""
    print(requete)
    cur = conn.cursor()
    cur.execute(requete)
    Afficher_table(cur)