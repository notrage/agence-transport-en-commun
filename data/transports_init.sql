DROP TABLE IF EXISTS EtapesBase;
DROP TABLE IF EXISTS ConducteursModeles;
DROP TABLE IF EXISTS Vehicules;
DROP TABLE IF EXISTS Tarifs;
DROP TABLE IF EXISTS Conducteurs;
DROP TABLE IF EXISTS Modeles;
DROP TABLE IF EXISTS LignesBase;
DROP TABLE IF EXISTS Arrets;
DROP VIEW IF EXISTS Lignes;
DROP VIEW IF EXISTS Etapes;


CREATE TABLE Conducteurs (
    matricule_conducteur INTEGER PRIMARY KEY,
    nom_conducteur TEXT NOT NULL,
    prenom_conducteur TEXT NOT NULL,
    CONSTRAINT CK_conducteur_mat CHECK (matricule_conducteur > 0)
);

CREATE TABLE Modeles (
    type_modele TEXT PRIMARY KEY,
    capacite_modele INT NOT NULL,
    CONSTRAINT CK_modeles_type CHECK (type_modele IN ("Bus","Tram")),
    CONSTRAINT CK_modeles_capacite CHECK (capacite_modele > 0)
);

CREATE TABLE Tarifs (
    numero_tarif INT PRIMARY KEY,
    type_modele TEXT, 
    duree_tarif REAL NOT NULL,
    prix_tarif REAL NOT NULL,
    CONSTRAINT FK_tarifs_type FOREIGN KEY (type_modele)
        REFERENCES Modeles(type_modele),
    CONSTRAINT CK_numero_tarif CHECK (numero_tarif > 0),
    CONSTRAINT CK_numero_duree CHECK (duree_tarif > 0),
    CONSTRAINT CK_numero_prix CHECK (prix_tarif > 0)
);

CREATE TABLE Arrets (
    nom_arret TEXT PRIMARY KEY NOT NULL,
    adresse_arret TEXT NOT NULL
);

CREATE TABLE LignesBase (
    nom_ligne TEXT PRIMARY KEY NOT NULL,
    premier_depart_ligne DATE NOT NULL,
    dernier_depart_ligne DATE NOT NULL,
    minute_intervalle_ligne INT NOT NULL,
    CONSTRAINT CK_lignes_intervalle CHECK (minute_intervalle_ligne > 0),
    CONSTRAINT CK_lignes_premierdep CHECK (premier_depart_ligne >= TIME('05:00:00'))
    CONSTRAINT CK_lignes_dernierdep CHECK (dernier_depart_ligne <= TIME('23:00:00'))
);

CREATE TABLE Vehicules (
    numero_vehicule INT PRIMARY KEY,
    type_modele TEXT,
    nom_ligne TEXT,
    CONSTRAINT FK_vehicules_type FOREIGN KEY (type_modele)
        REFERENCES Modeles(type_modele),
    CONSTRAINT FK_vehicules_ligne FOREIGN KEY (nom_ligne)
        REFERENCES LignesBase(nom_ligne),
    CONSTRAINT CK_vehicules_num CHECK (numero_vehicule > 0)
);

CREATE TABLE EtapesBase (
    nom_ligne TEXT,
    nom_arret TEXT,
    rang_etape INT,
    CONSTRAINT PK_etapesBase_lignearret PRIMARY KEY (nom_ligne,nom_arret),
    CONSTRAINT FK_etapesBase_ligne FOREIGN KEY (nom_ligne)
        REFERENCES LignesBase(nom_ligne),
    CONSTRAINT FK_etapesBase_arret FOREIGN KEY (nom_arret)
        REFERENCES Arrets(nom_arret),
    CONSTRAINT CK_etapesBase_rang CHECK (rang_etape > 0)
);

CREATE TABLE ConducteursModeles(
    matricule_conducteur INT,
    type_modele TEXT, 
    CONSTRAINT PK_conducteursmodeles_mattype PRIMARY KEY (matricule_conducteur,type_modele)
    CONSTRAINT FK_conducteurmodele_matricule FOREIGN KEY (matricule_conducteur)
        REFERENCES Conducteurs(matricule_conducteur),
    CONSTRAINT FK_conducteurmodele_type FOREIGN KEY (type_modele)
        REFERENCES Modeles(type_modele)   
);

-- View pour afficher l'arrêt de départ et de fin de chaque ligne
CREATE VIEW Lignes AS 
WITH LigneRangMax AS (
    SELECT nom_ligne, MAX(rang_etape) AS rang_max
    FROM EtapesBase
    GROUP BY nom_ligne ),
DernierArretParLigne AS (
    SELECT E.nom_ligne, nom_arret AS arrive_ligne
    FROM EtapesBase E 
    JOIN LigneRangMax L ON (E.nom_ligne = L.nom_ligne AND rang_etape = rang_max))
SELECT nom_ligne, premier_depart_ligne, dernier_depart_ligne, minute_intervalle_ligne, nom_arret AS depart_ligne,D.arrive_ligne AS arrive_ligne
FROM LignesBase JOIN EtapesBase USING(nom_ligne) JOIN DernierArretParLigne D USING(nom_ligne)
WHERE rang_etape = 1;

-- View pour afficher le prochain départ de chaque étape
CREATE VIEW Etapes AS 
WITH LignesTemps AS (
	SELECT 
		nom_ligne,
		CAST(strftime('%H', premier_depart_ligne) AS INTEGER) * (60*60) +
		CAST(strftime('%M', premier_depart_ligne) AS INTEGER) * 60 +
		CAST(strftime('%S', premier_depart_ligne) AS INTEGER) AS depart_en_sec,
		CAST(strftime('%H', 'now', 'localtime') AS INTEGER) * (60*60) +
		CAST(strftime('%M', 'now', 'localtime') AS INTEGER) * 60 +
		CAST(strftime('%S', 'now', 'localtime') AS INTEGER) AS actual_time_en_sec,
		minute_intervalle_ligne * 60 AS interval_en_sec
	FROM lignes),
	LigneProchainDepart AS (
	SELECT nom_ligne,interval_en_sec - ((actual_time_en_sec - depart_en_sec) % interval_en_sec) AS prochain_depart_en_sec, interval_en_sec
	FROM LignesTemps)
SELECT nom_ligne,nom_arret,rang_etape ,((prochain_depart_en_sec + 2 * 60 * rang_etape) / 60) % minute_intervalle_ligne AS prochain_depart_en_minute
FROM LigneProchainDepart JOIN EtapesBase USING(nom_ligne) JOIN Lignes USING(nom_ligne)
ORDER BY nom_ligne, rang_etape;
