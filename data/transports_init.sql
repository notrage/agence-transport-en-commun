DROP TABLE IF EXISTS Etapes;
DROP TABLE IF EXISTS ConducteursModeles;
DROP TABLE IF EXISTS Vehicules;
DROP TABLE IF EXISTS Tarifs;
DROP TABLE IF EXISTS Conducteurs;
DROP TABLE IF EXISTS Modeles;
DROP TABLE IF EXISTS Lignes;
DROP TABLE IF EXISTS Arrets;

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

CREATE TABLE Lignes (
    nom_ligne TEXT PRIMARY KEY NOT NULL,
    premier_depart_ligne DATE NOT NULL,
    dernier_depart_ligne DATE NOT NULL,
    minute_intervalle_ligne INT NOT NULL,
    depart_ligne TEXT,
    arrive_ligne TEXT,
    CONSTRAINT FK_lignes_depart FOREIGN KEY (depart_ligne)
        REFERENCES Arrets(nom_arret),
    CONSTRAINT FK_lignes_arret FOREIGN KEY (arrive_ligne)
        REFERENCES Arrets(nom_arret),
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
        REFERENCES Lignes(nom_ligne),
    CONSTRAINT CK_vehicules_num CHECK (numero_vehicule > 0)
);

CREATE TABLE Etapes (
    nom_ligne TEXT,
    nom_arret TEXT,
    rang_etape INT,
    CONSTRAINT PK_etapes_lignearret PRIMARY KEY (nom_ligne,nom_arret),
    CONSTRAINT FK_etapes_ligne FOREIGN KEY (nom_ligne)
        REFERENCES Lignes(nom_ligne),
    CONSTRAINT FK_etapes_arret FOREIGN KEY (nom_arret)
        REFERENCES Arrets(nom_arret),
    CONSTRAINT CK_etapes_rang CHECK (rang_etape > 0)
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