INSERT INTO Conducteurs VALUES (1, "Claude", "Francois");
INSERT INTO Conducteurs VALUES (2, "Michel", "Sardou");
INSERT INTO Conducteurs VALUES (3, "Johnny", "Hallyday");

INSERT INTO Modeles VALUES ("Tram", 300);
INSERT INTO Modeles VALUES ("Bus", 60);

INSERT INTO ConducteursModeles VALUES (1, "Tram");
INSERT INTO ConducteursModeles VALUES (1, "Bus");
INSERT INTO ConducteursModeles VALUES (2, "Tram");
INSERT INTO ConducteursModeles VALUES (3, "Tram");
INSERT INTO ConducteursModeles VALUES (3, "Bus");

INSERT INTO Tarifs VALUES (1, "Tram", 1, 2.10);
INSERT INTO Tarifs VALUES (2, "Tram", 3, 5.50);
INSERT INTO Tarifs VALUES (3, "Bus", 1, 1.70);

INSERT INTO Arrets VALUES ("Victor Hugo", "Place Victor Hugo");
INSERT INTO Arrets VALUES ("Hubert Dubedout", "Rue Raoul Blanchard");
INSERT INTO Arrets VALUES ("Verdun Prefecture", "Place de Verdun");
INSERT INTO Arrets VALUES ("Chavant", "Rue Bistesi");
INSERT INTO Arrets VALUES ("Albert 1er de Belgique", "Avenue General Champon");
INSERT INTO Arrets VALUES ("Mounier", "Avenue Marcellin Berthelot");
INSERT INTO Arrets VALUES ("MC2 Maison de la Culture", "Avenue Marcellin Berthelot");
INSERT INTO Arrets VALUES ("Flandrin Valmy", "Rue Jules Flandrin");
INSERT INTO Arrets VALUES ("Hotel de Ville", "Boulevard Jean Pain");
INSERT INTO Arrets VALUES ("Gustave Rivet", "Boulevard Marechal Joffre");
INSERT INTO Arrets VALUES ("Foch-Ferrie", "Boulevard Marechal Foch");

INSERT INTO LignesBase VALUES ('A', "06:30:00", "22:30:00", 5);
INSERT INTO LignesBase VALUES ('C', "05:45:00", "22:45:00", 7);

INSERT INTO Vehicules VALUES (1, "Tram", 'A');
INSERT INTO Vehicules VALUES (2, "Tram", 'A');
INSERT INTO Vehicules VALUES (3, "Tram", 'C');
INSERT INTO Vehicules VALUES (4, "Tram", 'C');

INSERT INTO EtapesBase VALUES ('A', "Victor Hugo", 1);
INSERT INTO EtapesBase VALUES ('A', "Hubert Dubedout", 2);
INSERT INTO EtapesBase VALUES ('A', "Verdun Prefecture", 3);
INSERT INTO EtapesBase VALUES ('A', "Chavant", 4);
INSERT INTO EtapesBase VALUES ('A', "Albert 1er de Belgique", 5);
INSERT INTO EtapesBase VALUES ('A', "Mounier", 6);
INSERT INTO EtapesBase VALUES ('A', "MC2 Maison de la Culture", 7);
INSERT INTO EtapesBase VALUES ('C', "Flandrin Valmy", 1);
INSERT INTO EtapesBase VALUES ('C', "Hotel de Ville", 2);
INSERT INTO EtapesBase VALUES ('C', "Chavant", 3);
INSERT INTO EtapesBase VALUES ('C', "Gustave Rivet", 4);
INSERT INTO EtapesBase VALUES ('C', "Foch-Ferrie", 5);