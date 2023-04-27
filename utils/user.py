import PySimpleGUI as sg
import sqlite3

class ArretNodes:
    def  __init__(self, arret):
        self.arret = arret
        self.voisin = list()
        # Evite les répétitions dans les DFS
        self.marque = False 
    def __str__(self):
        return self.arret
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

def Trouver_un_chemin(conn,ArretDepart,ArretArrivee):
    NodeDepart,NodeArrivee = Construire_graph(conn,ArretDepart,ArretArrivee)
    Parcours_en_largeur(NodeDepart,NodeArrivee)


def Parcours_en_largeur(NodeDepart:ArretNodes, NodeArrivee:ArretNodes):
    f = File()
    f.enfiler([NodeDepart,0,[NodeDepart.arret]])
    NodeDepart.marquer()
    while not f.est_vide():
        [s,dist,chemin] = f.defiler()
        for v in s.voisins():
            if v.arret == NodeArrivee.arret:
                print("FINI : ",chemin + [NodeArrivee.arret])
                return chemin + [NodeArrivee.arret]
            if not v.est_marque():
                f.enfiler([v,dist+1,chemin+[v.arret]])
                v.marquer()

    print("Pas de chemin trouvé")

def Construire_graph(conn:sqlite3.Connection, ArretDepart:str, ArretArrivee:str):
    node_dict = {}
    cur = conn.cursor()
    NodeDepart = None
    NodeArrivee = None
    # On récupere la liste des arrêt pour créer toutes les nodes 
    requete = """   
                    SELECT nom_arret 
                    FROM Arrets;"""
    print(requete)
    cur.execute(requete)
    # Construction de toute les nodes
    for arret in cur.fetchall():
        a = arret[0]
        if not node_dict.get(arret,False):
            node_dict[a] = ArretNodes(a)
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
        print(requete)
        cur.execute(requete)
        for arrets in cur.fetchall():
            node_a = node_dict[arrets[0]]
            node_b = node_dict[arrets[1]]
            node_a.ajouter_voisin(node_b)
    return NodeDepart,NodeArrivee