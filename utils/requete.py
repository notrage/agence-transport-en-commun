import sqlite3

class Requete:
    
    def __init__(self, db_conn) -> None:
        
        self.conn: sqlite3.Connection = db_conn
    

    def select_all_from(self, table: str) -> sqlite3.Cursor:
        
        cur: sqlite3.Cursor = self.conn.cursor()
        req: str = f"SELECT * FROM {table};"
        print(req)
        cur.execute(req)
        return cur
        

    def select_min_mat_conducteur(self) -> sqlite3.Cursor:
        
        cur: sqlite3.Cursor = self.conn.cursor()
        req: str = f"""
                WITH FreeMat AS (
                    SELECT A.matricule_conducteur AS matricule_conducteur,B.matricule_conducteur AS NullMat
                    FROM Conducteurs A LEFT JOIN Conducteurs B ON (A.matricule_conducteur = B.matricule_conducteur - 1)
                    )
                SELECT MIN(matricule_conducteur + 1)	
                FROM FreeMat
                WHERE NullMat IS NULL;"""
        print(req)
        cur.execute(req)
        return cur
    

    def select_min_num_vehicule(self) -> sqlite3.Cursor:
        
        cur: sqlite3.Cursor = self.conn.cursor()
        req: str = f"""
                WITH FreeNum AS (
                    SELECT A.numero_vehicule AS numero_vehicule,B.numero_vehicule AS NullNum
                    FROM Vehicules A LEFT JOIN Vehicules B ON (A.numero_vehicule = B.numero_vehicule - 1)
                    )
                SELECT MIN(numero_vehicule + 1)	
                FROM FreeNum
                WHERE NullNum IS NULL;"""
        print(req)
        cur.execute(req)
        return cur
    

    def insert_conducteur(self, mat: int, nom: str, prenom: str, bus: bool, tram: bool) -> None:
        
        cur: sqlite3.Cursor = self.conn.cursor()
        req: str = f"""INSERT INTO Conducteurs VALUES ({mat},"{nom}","{prenom}");"""
        print(req)
        cur.execute(req)
        
        if bus: 
            req: str = f"""INSERT INTO ConducteursModeles VALUES ({mat},"Bus");"""
            print(req)
            cur.execute(req)
        if tram:
            req: str = f"""INSERT INTO ConducteursModeles VALUES ({mat},"Tram");"""
            print(req)
            cur.execute(req)
         
            
    def insert_vehicule(self, num: int, bus: bool, tram: bool, ligne: str) -> None:
        
        if bus: type_modele: str = "Bus"
        else: type_modele: str = "Tram"
        cur: sqlite3.Cursor = self.conn.cursor()
        req: str = f"""INSERT INTO Vehicules VALUES ({num},"{type_modele}","{ligne}");"""
        print(req)
        cur.execute(req)
        

    def insert_arret(self, nom: str, adr: str) -> bool:
        
        cur: sqlite3.Cursor = self.conn.cursor()
        req: str = f"""INSERT INTO Arrets VALUES ("{nom}","{adr}");"""
        print(req)
        try:
            cur.execute(req)
        except sqlite3.IntegrityError:
            return False
        else:
            return True
        

    def delete_conducteur(self, mat: int) -> None:
        
        cur: sqlite3.Cursor = self.conn.cursor()
        req: str = f"""DELETE FROM ConducteursModeles WHERE matricule_conducteur == {mat};"""
        print(req)
        cur.execute(req)
        
        req: str = f"""DELETE FROM Conducteurs WHERE matricule_conducteur == {mat};"""
        print(req)
        cur.execute(req)
        

    def delete_vehicule(self, num: int) -> None:
        
        cur: sqlite3.Cursor = self.conn.cursor()
        req: str = f"""DELETE FROM Vehicules WHERE numero_vehicule == {num};"""
        print(req)
        cur.execute(req)
        

    def select_from_etapesbase_nom_ligne_rang_etape_where(self, nom_arret: str) -> sqlite3.Cursor:
    
        cur: sqlite3.Cursor = self.conn.cursor()
        req: str = f"""
                SELECT nom_ligne, rang_etape 
                FROM Etapes 
                WHERE nom_arret == "{nom_arret}";"""
        print(req)
        cur.execute(req)
        return cur
    

    def update_etapesbase_rang_etape_where_ligne_and_rang_etape_greater(self, ligne: str, etape: int) -> None:

        cur: sqlite3.Cursor = self.conn.cursor()
        req: str = f"""
                UPDATE EtapesBase 
                SET rang_etape = rang_etape - 1 
                WHERE nom_ligne == "{ligne}" AND rang_etape > {etape};"""
        print(req)
        cur.execute(req)
        

    def delete_etapesbase_where_nom_arret(self, nom_arret: str) -> None:
        
        cur: sqlite3.Cursor = self.conn.cursor()
        req: str = f"""
                DELETE FROM EtapesBase 
                WHERE nom_arret == "{nom_arret}";"""
        print(req)
        cur.execute(req)
        

    def delete_arrets_where_nom_arret(self, nom_arret: str) -> None:
        
        cur: sqlite3.Cursor = self.conn.cursor()
        req: str = f"""
                DELETE FROM Arrets 
                WHERE nom_arret == "{nom_arret}";"""
        print(req)
        cur.execute(req)   


    def delete_arret(self, nom_arret: str) -> None:
        
        # Recuperation des lignes concernés ainsi que des rang :
        cur = self.select_from_etapesbase_nom_ligne_rang_etape_where(nom_arret)
        rows = cur.fetchall()
        # Décalage des numéros d"etapes sur chaque ligne
        for (ligne,etape) in rows:
            self.update_etapesbase_rang_etape_where_ligne_and_rang_etape_greater(ligne, etape)
        self.delete_etapesbase_where_nom_arret(nom_arret)
        self.delete_arrets_where_nom_arret(nom_arret)  
    

    def select_from_etapesbase_nom_arret_rang_etape_where_nom_ligne(self, nom_ligne: str) -> sqlite3.Cursor:
        
        cur: sqlite3.Cursor = self.conn.cursor()
        req: str = f"""
                SELECT nom_arret,rang_etape
                FROM Etapes 
                WHERE nom_ligne = "{nom_ligne}"
                ORDER BY rang_etape;"""
        print(req)
        cur.execute(req) 
        return cur  
    

    def delete_etapesbase_where_nom_arret_and_nom_ligne(self, nom_arret: str, nom_ligne: str) -> None:
        
        cur: sqlite3.Cursor = self.conn.cursor()
        req: str = f"""
                DELETE FROM EtapesBase 
                WHERE nom_arret == "{nom_arret}" AND nom_ligne == "{nom_ligne}";"""
        print(req)
        cur.execute(req)
        

    def select_from_etapes_max_rang_etape_where_nom_ligne(self, nom_ligne: str) -> sqlite3.Cursor:
        
        cur: sqlite3.Cursor = self.conn.cursor()
        req: str = f"""  
                SELECT MAX(rang_etape)
                FROM Etapes
                WHERE nom_ligne = "{nom_ligne}";"""
        print(req)
        cur.execute(req)
        return cur


    def select_from_arrets_nom_arret_exept_in_etapes_where_nom_ligne(self, nom_ligne: str) -> sqlite3.Cursor:
        
        cur: sqlite3.Cursor = self.conn.cursor()
        req: str =f"""
            SELECT nom_arret 
            FROM Arrets
            EXCEPT
            SELECT nom_arret
            FROM Etapes
            WHERE nom_ligne = "{nom_ligne}";"""
        print(req)
        cur.execute(req)
        return cur
    

    def update_etapesbase_rang_etape_where_ligne_and_rang_etape_greater_or_equal(self, nom_ligne: str, rang_etape: int) -> None:
        
        cur: sqlite3.Cursor = self.conn.cursor()
        req: str = f"""
                UPDATE EtapesBase 
                SET rang_etape = rang_etape + 1 
                WHERE nom_ligne == "{nom_ligne}" AND rang_etape >= {rang_etape};"""
        print(req)
        cur.execute(req)
        

    def insert_etapesbase(self, nom_ligne: str, nom_arret: str, rang_etape: int) -> None:
        
        cur: sqlite3.Cursor = self.conn.cursor()
        req: str = f"""INSERT INTO EtapesBase VALUES ("{nom_ligne}","{nom_arret}",{rang_etape});"""
        print(req)
        cur.execute(req)
        

    def select_from_lignes_nom_ligne(self) -> sqlite3.Cursor:
        
        cur: sqlite3.Cursor = self.conn.cursor()
        req: str = f"""
            SELECT nom_ligne 
            FROM Lignes;"""
        print(req)
        cur.execute(req)
        return cur
    

    def select_effectif(self) -> sqlite3.Cursor:

        cur: sqlite3.Cursor = self.conn.cursor()
        req: str = f"""
                        WITH Effectifs AS (
                            SELECT type_modele, COUNT(DISTINCT numero_vehicule) AS nombre_de_vehicules, COUNT(DISTINCT matricule_conducteur) AS nombre_de_conducteurs
                            FROM Vehicules JOIN ConducteursModeles USING(type_modele)
                            GROUP BY type_modele)
                        SELECT type_modele, nombre_de_vehicules, nombre_de_conducteurs, 
                            CASE WHEN nombre_de_vehicules > nombre_de_conducteurs THEN 'SOUS-EFFECTIF DE CONDUCTEURS'
                                WHEN nombre_de_vehicules < nombre_de_conducteurs THEN 'SUR-EFFECTIF DE CONDUCTEURS'
                                ELSE 'EFFECTIF IDEAL' END AS verficiation_effectif,
                            nombre_de_vehicules - nombre_de_conducteurs AS difference
                        FROM Effectifs;"""
        print(req)
        cur.execute(req)
        return cur
    

    def select_nom_arret_nom_ligne_from_etapes(self) -> sqlite3.Cursor:

        cur: sqlite3.Cursor = self.conn.cursor()
        req: str = f"""
                SELECT nom_arret, nom_ligne
                FROM Etapes;"""
        print(req)
        cur.execute(req)
        return cur
    

    def select_voisin_arret(self,nom_ligne) -> sqlite3.Cursor:

        cur: sqlite3.Cursor = self.conn.cursor()
        req: str = f"""
                SELECT A.nom_arret, B.nom_arret 
                FROM Etapes A 
                JOIN Etapes B ON (A.nom_ligne = B.nom_ligne AND 
                                 (A.rang_etape = B.rang_etape - 1 OR A.rang_etape = B.rang_etape + 1))
                WHERE A.nom_ligne = "{nom_ligne}";"""
        print(req)
        cur.execute(req)
        return cur
    

    def select_distinct_from_tarifs(self,attribut) -> sqlite3.Cursor:

        cur: sqlite3.Cursor = self.conn.cursor()
        req: str = f"""
                SELECT DISTINCT({attribut})
                FROM Tarifs;"""
        print(req)
        cur.execute(req)
        return cur
    

    def select_info_arret(self,nom_arret) -> sqlite3.Cursor:
        cur: sqlite3.Cursor = self.conn.cursor()
        req: str = f"""
                SELECT A.nom_ligne, CASE WHEN A.prochain_depart_en_minute == 0 THEN 'IMMINENT'
                        ELSE A.prochain_depart_en_minute END AS prochain_depart_en_minute, 
                        IFNULL(B.nom_arret,'TERMINUS') AS prochain_arret,
                        arrive_ligne AS en_direction_de
                FROM Etapes A LEFT JOIN Etapes B ON(A.nom_ligne = B.nom_ligne AND A.rang_etape = B.rang_etape - 1)
                JOIN Lignes USING(nom_ligne)
                WHERE  A.nom_arret = "{nom_arret}";"""
        print(req)
        cur.execute(req)
        return cur
    
    def select_info_tarif(self,type_vehicule,duree) -> sqlite3.Cursor:
        cur: sqlite3.Cursor = self.conn.cursor()
        req: str = f"""
                SELECT DISTINCT nom_ligne AS liste_ligne_desservie, prix_tarif AS prix
                FROM Tarifs JOIN Vehicules USING(type_modele)
                WHERE type_modele = "{type_vehicule}" AND duree_tarif = "{duree}";"""
        print(req)
        cur.execute(req)
        return cur