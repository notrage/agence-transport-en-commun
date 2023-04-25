/* Conducteurs */
-- CK_conducteur_mat
INSERT INTO Conducteurs VALUES (0, "Jean", "Eude");
INSERT INTO Conducteurs VALUES (-1, "Jean", "Eude");


/* Modeles */
-- CK_modeles_type
INSERT INTO Modeles VALUES ("Train", 600);
INSERT iNTO Modeles VALUES ("Avion", 450);

-- CK_modeles_capacite
INSERT INTO Modeles VALUES ("Tram", 0);
INSERT INTO Modeles VALUES ("Bus", -1);


/* Tarifs */
-- CK_numero_tarif
INSERT INTO Tarifs VALUES (0, "Tram", 1.5, 5);
INSERT INTO Tarifs VALUES (-1, "Bus", 3, 7);

-- CK_numero_duree
INSERT INTO Tarifs VALUES (1, "Tram", 0, 5);
INSERT INTO Tarifs VALUES (2, "Bus", -1, 7);

-- CK_numero_prix
INSERT INTO Tarifs VALUES (1, "Tram", 1.5, 0);
INSERT INTO Tarifs VALUES (2, "Bus", 3, -1);


/* Lignes */
-- CK_lignes_intervalle
INSERT INTO Lignes VALUES ('A', "06:30:00", "22:30:00", 0);
INSERT INTO Lignes VALUES ('C', "05:45:00", "22:45:00", -1);


/* Vehicules */
-- CK_vehicules_num
INSERT INTO Vehicules VALUES (0, "Tram", 'A');
INSERT INTO Vehicules VALUES (-1, "Bus", 'C1');


/* Etapes */
-- CK_etapes_rang
INSERT INTO Etapes VALUES ('A', "Victor Hugo", 0);
INSERT INTO Etapes VALUES ('C', "Chavant", -1);