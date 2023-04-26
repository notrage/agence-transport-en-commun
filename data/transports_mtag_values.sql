/* Creation des conducteurs de tram/bus */
INSERT INTO Conducteurs VALUES (1, "Jean-Jacques", "Goldman");
INSERT INTO Conducteurs VALUES (2, "Johnny", "Hallyday");
INSERT INTO Conducteurs VALUES (3, "Michel", "Sardou");
INSERT INTO Conducteurs VALUES (4, "Jacques", "Brel");
INSERT INTO Conducteurs VALUES (5, "Claude", "Francois");
INSERT INTO Conducteurs VALUES (6, "Laurent", "Voulzy");
INSERT INTO Conducteurs VALUES (7, "Serge", "Gainsbourg");
INSERT INTO Conducteurs VALUES (8, "Florent", "Pagny");
INSERT INTO Conducteurs VALUES (9, "Joe", "Dassin");
INSERT INTO Conducteurs VALUES (10, "Pascal", "Obispo");
INSERT INTO Conducteurs VALUES (11, "Charles", "Aznavour");
INSERT INTO Conducteurs VALUES (12, "Francis", "Cabrel");
INSERT INTO Conducteurs VALUES (13, "Patrick", "Bruel");
INSERT INTO Conducteurs VALUES (14, "Jacques", "Dutronc");
INSERT INTO Conducteurs VALUES (15, "Michel", "Polnareff");
INSERT INTO Conducteurs VALUES (16, "Alain", "Bashung");
INSERT INTO Conducteurs VALUES (17, "Marc", "Lavoine");
INSERT INTO Conducteurs VALUES (18, "Georges", "Brassens");
INSERT INTO Conducteurs VALUES (19, "Jean", "Ferrat");
INSERT INTO Conducteurs VALUES (20, "Nino", "Ferrer");


/* Creation des modeles de vehicules */
INSERT INTO Modeles VALUES ("Tram", 300);
INSERT INTO Modeles VALUES ("Bus", 60);


/* Affectation des conducteurs aux modeles de vehicules */
INSERT INTO ConducteursModeles VALUES (1, "Tram");
INSERT INTO ConducteursModeles VALUES (1, "Bus");
INSERT INTO ConducteursModeles VALUES (2, "Tram");
INSERT INTO ConducteursModeles VALUES (2, "Bus");
INSERT INTO ConducteursModeles VALUES (3, "Tram");
INSERT INTO ConducteursModeles VALUES (3, "Bus");
INSERT INTO ConducteursModeles VALUES (4, "Tram");
INSERT INTO ConducteursModeles VALUES (5, "Bus");
INSERT INTO ConducteursModeles VALUES (6, "Tram");
INSERT INTO ConducteursModeles VALUES (6, "Bus");
INSERT INTO ConducteursModeles VALUES (7, "Tram");
INSERT INTO ConducteursModeles VALUES (7, "Bus");
INSERT INTO ConducteursModeles VALUES (8, "Tram");
INSERT INTO ConducteursModeles VALUES (9, "Tram");
INSERT INTO ConducteursModeles VALUES (10, "Bus");
INSERT INTO ConducteursModeles VALUES (11, "Bus");
INSERT INTO ConducteursModeles VALUES (12, "Tram");
INSERT INTO ConducteursModeles VALUES (12, "Bus");
INSERT INTO ConducteursModeles VALUES (13, "Tram");
INSERT INTO ConducteursModeles VALUES (13, "Bus");
INSERT INTO ConducteursModeles VALUES (14, "Tram");
INSERT INTO ConducteursModeles VALUES (14, "Bus");
INSERT INTO ConducteursModeles VALUES (15, "Tram");
INSERT INTO ConducteursModeles VALUES (16, "Bus");
INSERT INTO ConducteursModeles VALUES (17, "Bus");
INSERT INTO ConducteursModeles VALUES (18, "Tram");
INSERT INTO ConducteursModeles VALUES (19, "Bus");
INSERT INTO ConducteursModeles VALUES (20, "Tram");


/* Creation des Tarifs */
INSERT INTO Tarifs VALUES (1, "Tram", "1H", 2.10);
INSERT INTO Tarifs VALUES (2, "Bus", "1H", 1.70);
INSERT INTO Tarifs VALUES (3, "Tram", "3H", 5.50);
INSERT INTO Tarifs VALUES (4, "Bus", "3H", 4.80);
INSERT INTO Tarifs VALUES (5, "Tram", "1J", 8);
INSERT INTO Tarifs VALUES (6, "Bus", "1J", 7);
INSERT INTO Tarifs VALUES (7, "Tram", "1S", 11);
INSERT INTO Tarifs VALUES (8, "Bus", "1S", 10);
INSERT INTO Tarifs VALUES (9, "Tram", "1M", 20);
INSERT INTO Tarifs VALUES (10, "Bus", "1M", 15);


/* Creation des arrets */
-- Arrets de la ligne A
INSERT INTO Arrets VALUES ("L'Etoile", "Avenue General de Gaulle");
INSERT INTO Arrets VALUES ("Edmee Chandon", "Avenue General de Gaulle");
INSERT INTO Arrets VALUES ("Denis Papin", "Avenue General de Gaulle");
INSERT INTO Arrets VALUES ("Auguste Delaune", "Avenue General de Gaulle");
INSERT INTO Arrets VALUES ("Marie Curie", "Avenue du 8 Mai 1945");
INSERT INTO Arrets VALUES ("La Rampe - Cantre-Ville", "Avenue du 8 mai 1945");
INSERT INTO Arrets VALUES ("Echirolles Gare", "Avenue des Etats Generaux");
INSERT INTO Arrets VALUES ("Essarts - La Butte", "Avenue des Etats Generaux");
INSERT INTO Arrets VALUES ("Surieux", "Rue de Normandie");
INSERT INTO Arrets VALUES ("Les Granges", "Rue d'Alsace");
INSERT INTO Arrets VALUES ("Polesud - Alpexpo", "Rue Salvador Allende");
INSERT INTO Arrets VALUES ("Grand'Place", "Avenue de l'Europe");
INSERT INTO Arrets VALUES ("Arlequin", "Rue Maurice Dodero");
INSERT INTO Arrets VALUES ("La Bruyere - Parc Jean Verlhac", "Avenue la Bruyere");
INSERT INTO Arrets VALUES ("Malherbe", "Avenue Marcellin Berthelot");
INSERT INTO Arrets VALUES ("MC2 Maison de la Culture", "Avenue Marcellin Berthelot");
INSERT INTO Arrets VALUES ("Mounier", "Avenue Marcellin Berthelot");
INSERT INTO Arrets VALUES ("Albert 1er de Belgique", "Avenue General Champon");
INSERT INTO Arrets VALUES ("Chavant", "Rue Bistesi");
INSERT INTO Arrets VALUES ("Verdun Prefecture", "Place de Verdun");
INSERT INTO Arrets VALUES ("Hubert Dubedout - Maison du Tourisme", "Rue Raoul Blanchard");
INSERT INTO Arrets VALUES ("Victor Hugo", "Place Victor Hugo");
INSERT INTO Arrets VALUES ("Alsace-Lorraine", "Avenue Alsace-Lorraine");
INSERT INTO Arrets VALUES ("Gares", "Place de la Gare");
INSERT INTO Arrets VALUES ("St-Bruno", "Cours Berriat");
INSERT INTO Arrets VALUES ("Berriat - Le Magasin", "Cours Berriat");
INSERT INTO Arrets VALUES ("Les Fontainades - Le Vog",  "Avenue Aristide Briand");
INSERT INTO Arrets VALUES ("Louis Maisonnat", "Avenue Aristide Briand");
INSERT INTO Arrets VALUES ("Fontaine Hotel de Ville La Source", "Avenue Aristide Briand");
INSERT INTO Arrets VALUES ("Charles Michels", "Avenue Ambroise Croizat");
INSERT INTO Arrets VALUES ("La Poya", "Boulevard Paul Langevin");

-- Arrets de la ligne B
INSERT INTO Arrets VALUES ("Plaine des Sports", "Mail des Sports");
INSERT INTO Arrets VALUES ("Gieres Gare - Universites", "Passage de la Gare");
INSERT INTO Arrets VALUES ("Mayencin - Champ Roman", "Rue de l'Etang");
INSERT INTO Arrets VALUES ("Condillac - Universites", "Rue des Residences");
INSERT INTO Arrets VALUES ("Blibliotheques Universitaires", "Avenue Centrale");
INSERT INTO Arrets VALUES ("Gabriel Faure", "Avenue Centrale");
INSERT INTO Arrets VALUES ("Les Taillees - Universites", "Rue de la Houille Blanche");
INSERT INTO Arrets VALUES ("Grand Sablon", "Avenue du grand Sablon");
INSERT INTO Arrets VALUES ("Michallon", "Allee du Noyer d'Amerique");
INSERT INTO Arrets VALUES ("Hopital", "Avenue des Marquis du Gresivaudan");
INSERT INTO Arrets VALUES ("Ile Verte", "Place Docteur Girard");
INSERT INTO Arrets VALUES ("Notre-Dame Musee", "Rue Frederic Taulier");
INSERT INTO Arrets VALUES ("Ste-Claire - Les Halles", "Rue Jean-François Hache");
INSERT INTO Arrets VALUES ("Palais de Justice Gare", "Rue Pierre Semard");
INSERT INTO Arrets VALUES ("Cite Internationale", "Rue Felix Esclangon");
INSERT INTO Arrets VALUES ("Marie-Louise Paris - CEA", "Avenue des Martyrs");
INSERT INTO Arrets VALUES ("Oxford", "Avenue des Martyrs");

-- Arrets de la ligne C
INSERT INTO Arrets VALUES ("Le Prisme", "Avenue du General de Gaulle");
INSERT INTO Arrets VALUES ("Mas des oles", "Avenue Louis Armand");
INSERT INTO Arrets VALUES ("Grand Pre", "Avenue Victor Hugo");
INSERT INTO Arrets VALUES ("Fauconniere", "Avenue Victor Hugo");
INSERT INTO Arrets VALUES ("Seyssinet-Pariset - Hotel de Ville", "Boulevard de l'Europe");
INSERT INTO Arrets VALUES ("Vallier - Catane", "Boulevard Joseph Vallier");
INSERT INTO Arrets VALUES ("Vallier Docteur Calmette", "Boulevard Joseph Vallier");
INSERT INTO Arrets VALUES ("Vallier - Liberation", "Boulevard Joseph Vallier");
INSERT INTO Arrets VALUES ("Foch-Ferrie", "Boulevard Marechal Foch");
INSERT INTO Arrets VALUES ("Gustave Rivet", "Boulevard Marechal Joffre");
INSERT INTO Arrets VALUES ("Grenoble Hotel de Ville", "Boulevard Jean Pain");
INSERT INTO Arrets VALUES ("Flandrin Valmy", "Rue Jules Flandrin");
INSERT INTO Arrets VALUES ("Peri - Brossolette", "Avenue Gabriel Peri");
INSERT INTO Arrets VALUES ("Neyrpic - Belledonne", "Avenue Gabriel Peri");
INSERT INTO Arrets VALUES ("Hector Berlioz - Universites", "Rue des Residences");

-- Arrets de la ligne D
INSERT INTO Arrets VALUES ("Etienne Grappe", "Rue Henri Wallon");
INSERT INTO Arrets VALUES ("Parc Jo Blanchon", "Avenue Elise Grappe");
INSERT INTO Arrets VALUES ("Edouard Vaillant", "Avenue Benoit Frachon");
INSERT INTO Arrets VALUES ("Maison Communale", "Avenue Benoit Frachon");

-- Arrets de la ligne E
INSERT INTO Arrets VALUES ("Louise Michel", "Avenue Ronsard");
INSERT INTO Arrets VALUES ("Allies", "Cours de la Liberation et du General de Gaulle");
INSERT INTO Arrets VALUES ("Vallier - Liberation (ligne E)", "Boulevard Joseph Vallier");
INSERT INTO Arrets VALUES ("Condorcet", "Cours Jean Jaures");
INSERT INTO Arrets VALUES ("Alsace-Lorraine (ligne E)", "Avenue Alsace-Lorraine");
INSERT INTO Arrets VALUES ("Annie Fratellini-Esplanade", "Boulevard de l'Esplanade");
INSERT INTO Arrets VALUES ("Casamaures - Village", "Route de Lyon");
INSERT INTO Arrets VALUES ("Hotel de Ville (ligne E)", "Avenue General Leclerc");
INSERT INTO Arrets VALUES ("Horloge", "Avenue General Leclerc");
INSERT INTO Arrets VALUES ("Neron", "Avenue General Leclerc");
INSERT INTO Arrets VALUES ("Fiancey - Predieu", "Route de Grenoble");
INSERT INTO Arrets VALUES ("Muret", "Route de Grenoble");
INSERT INTO Arrets VALUES ("Pont de Vence", "Avenue General de Gaulle");
INSERT INTO Arrets VALUES ("La Pinea - St-Robert", "Avenue General de Gaulle");
INSERT INTO Arrets VALUES ("Karben", "Route de Lyon");
INSERT INTO Arrets VALUES ("Rafour", "Route de Lyon");
INSERT INTO Arrets VALUES ("Palluel", "Route de Lyon");

-- Arrets de la ligne C1
INSERT INTO Arrets VALUES ("Pre de l'Eau", "Route de la Doux");
INSERT INTO Arrets VALUES ("Pre Millet", "Avenue de l'Europe");
INSERT INTO Arrets VALUES ("INRIA", "Avenue de l'Europe");
INSERT INTO Arrets VALUES ("Baudonniere", "Avenue de l'Europe");
INSERT INTO Arrets VALUES ("Busserolles", "Avenue de l'Europe");
INSERT INTO Arrets VALUES ("Norbert Segard", "Chemin du Vieux Chene");
INSERT INTO Arrets VALUES ("Les Bealieres", "Avenue du Granier");
INSERT INTO Arrets VALUES ("Malacher", "Avenue du Granier");
INSERT INTO Arrets VALUES ("Granier", "Avenue du Granier");
INSERT INTO Arrets VALUES ("Meylan Mairie", "Avenue du Vercors");
INSERT INTO Arrets VALUES ("Piscine des Buclos", "Avenue du Vercors");
INSERT INTO Arrets VALUES ("Le Bret", "Avenue du Vercors");
INSERT INTO Arrets VALUES ("La Reviree", "Avenue de Verdun");
INSERT INTO Arrets VALUES ("Aiguinards-Hexagone", "Avenue de Verdun");
INSERT INTO Arrets VALUES ("Plaine Fleurie", "Avenue de Verdun");
INSERT INTO Arrets VALUES ("Carronnerie - Ile d'Amour", "Avenue de Verdun");
INSERT INTO Arrets VALUES ("Sablons", "Avenue de Verdun");
INSERT INTO Arrets VALUES ("Docteur Martin", "Boulevard Agutte Sembat");
INSERT INTO Arrets VALUES ("Docteur Mazet", "Avenue Felix Viallet");
INSERT INTO Arrets VALUES ("Arago", "Rue Henri Tarze");
INSERT INTO Arrets VALUES ("Cite Jean Mace", "Rue Henri Tarze");

-- Arrets de la ligne C2
INSERT INTO Arrets VALUES ("Pont Rouge", "Avenue de la liberation");
INSERT INTO Arrets VALUES ("Pont-de-Claix Mairie", "Place du 8 Mai");
INSERT INTO Arrets VALUES ("Marcelline", "Cours Saint André");
INSERT INTO Arrets VALUES ("Irene Joliot-Curie", "Cours Saint André");
INSERT INTO Arrets VALUES ("L'Amphi", "Cours Saint André");
INSERT INTO Arrets VALUES ("Iles de Mars", "Cours Saint André");
INSERT INTO Arrets VALUES ("Clos Dominique", "Cours Saint André");
INSERT INTO Arrets VALUES ("Ecureuil", "Cours Jean Jaures");
INSERT INTO Arrets VALUES ("Bayard", "Cours Jean Jaures");
INSERT INTO Arrets VALUES ("Quinzaine", "Cours Jean Jaures");
INSERT INTO Arrets VALUES ("Navis", "Cours Jean Jaures");
INSERT INTO Arrets VALUES ("Marielle Franco Rondeau", "Cours de la Liberation et du General de Gaulle");
INSERT INTO Arrets VALUES ("Stade Lesdiguière", "Cours de la Liberation et du General de Gaulle");

-- Arrets de la ligne C3
INSERT INTO Arrets VALUES ("Centre du Graphisme", "Rue de Stalingrad");
INSERT INTO Arrets VALUES ("Le Village", "Rue Paul Langevin");
INSERT INTO Arrets VALUES ("Paul Langevin", "Rue Paul Langevin");
INSERT INTO Arrets VALUES ("Guy Mocquet", "Rue Paul Langevin");
INSERT INTO Arrets VALUES ("Le Chateau", "Rue de la Liberte"); 
INSERT INTO Arrets VALUES ("Ecoles Hospitalieres", "Avenue de Kimberley");
INSERT INTO Arrets VALUES ("Hopital Sud", "Avenue de Kimberley");
INSERT INTO Arrets VALUES ("Francois Quesnay", "Avenue de Kimberley");
INSERT INTO Arrets VALUES ("Alpexpo", "Avenue d'Innsbruck");
INSERT INTO Arrets VALUES ("Edmond Esmonin", "Avenue Edmond Esmonin");
INSERT INTO Arrets VALUES ("Christophe Turc", "Rue Aime Pupin");
INSERT INTO Arrets VALUES ("Village Olympique", "Rue Aime Pupin");
INSERT INTO Arrets VALUES ("Vigny", "Rue de Stalingrad");
INSERT INTO Arrets VALUES ("Clos d’Or", "Rue de Stalingrad");
INSERT INTO Arrets VALUES ("Eugène Sue", "Rue de Stalingrad");
INSERT INTO Arrets VALUES ("Capuche", "Rue de Stalingrad");
INSERT INTO Arrets VALUES ("Marceau Jardin des Vallons", "Rue de Marceau");
INSERT INTO Arrets VALUES ("Championnet", "Rue Lesdiguieres");

-- Arrets de la lignes C4
INSERT INTO Arrets VALUES ("Driant", "Avenue Jean Perrot");
INSERT INTO Arrets VALUES ("Malifaud", "Avenue Jean Perrot");
INSERT INTO Arrets VALUES ("Bajatiere", "Avenue Jean Perrot");
INSERT INTO Arrets VALUES ("Ponsard", "Avenue Jean Perrot");
INSERT INTO Arrets VALUES ("Paul Claudel", "Avenue Jean Perrot");
INSERT INTO Arrets VALUES ("Teisseire", "Avenue Jean Perrot");
INSERT INTO Arrets VALUES ("Jean Racine", "Avenue Jean Perrot");
INSERT INTO Arrets VALUES ("Maisons Neuves", "Avenue Jean Jaures");
INSERT INTO Arrets VALUES ("General de Gaulle", "Avenue Jean Jaures");
INSERT INTO Arrets VALUES ("Val d’Eybens", "Avenue Jean Jaures");
INSERT INTO Arrets VALUES ("Odyssee", "Avenue Jean Jaures");
INSERT INTO Arrets VALUES ("Les Javaux", "Avenue Jean Jaures");
INSERT INTO Arrets VALUES ("Le Bourg", "Avenue Jean Jaures");
INSERT INTO Arrets VALUES ("Le Verderet", "Avenue de la Republique");

-- Arrets de la ligne C5
INSERT INTO Arrets VALUES ("Esclangon", "Rue Felix Esclangon");
INSERT INTO Arrets VALUES ("Cemoi", "Rue Ampere");
INSERT INTO Arrets VALUES ("Rosa Parks", "Avenue Rhin de Danube");
INSERT INTO Arrets VALUES ("Docteur Schweitzer", "Rue Anatole France");
INSERT INTO Arrets VALUES ("Lys Rouge", "Rue Anatole France");
INSERT INTO Arrets VALUES ("Marché d'Intérêt National", "Rue des Allies");
INSERT INTO Arrets VALUES ("Stalingrad Allies", "Rue des Allies");
INSERT INTO Arrets VALUES ("Flaubert - Clos d'Or", "Rue des Allies");
INSERT INTO Arrets VALUES ("Louis Jouvet", "Avenue Malherbe");
INSERT INTO Arrets VALUES ("Paul Cocat", "Avenue Paul Cocat");
INSERT INTO Arrets VALUES ("Andre Argouges", "Rue Leon Jouhaux");
INSERT INTO Arrets VALUES ("Saint-Augustin", "Rue Andre Argouges");
INSERT INTO Arrets VALUES ("Bon Pasteur", "Avenue Jules Valles");
INSERT INTO Arrets VALUES ("Pierre Semard", "Avenue Pierre Semard");
INSERT INTO Arrets VALUES ("Clinique Belledonne", "Avenue Gabriel Peri");
INSERT INTO Arrets VALUES ("Champ Roman", "Avenue Gabriel Peri");
INSERT INTO Arrets VALUES ("Les Alpilles", "Rue des Universites");
INSERT INTO Arrets VALUES ("Universites Biologie", "Avenue Centrale");

/* Creation des lignes */
INSERT INTO LignesBase VALUES ('A', "05:00:00", "23:00:00", 3);
INSERT INTO LignesBase VALUES ('B', "05:00:00", "23:00:00", 5);
INSERT INTO LignesBase VALUES ('C', "05:00:00", "23:00:00", 5);
INSERT INTO LignesBase VALUES ('D', "05:15:00", "22:45:00", 7);
INSERT INTO LignesBase VALUES ('E', "05:15:00", "22:45:00", 7);
INSERT INTO LignesBase VALUES ("C1", "05:30:00", "22:30:00", 5);
INSERT INTO LignesBase VALUES ("C2", "05:30:00", "22:30:00", 5);
INSERT INTO LignesBase VALUES ("C3", "06:00:00", "22:00:00", 7);
INSERT INTO LignesBase VALUES ("C4", "06:00:00", "22:00:00", 7);
INSERT INTO LignesBase VALUES ("C5", "05:15:00", "22:35:00", 7);


/* Creation des vehicules */
INSERT INTO Vehicules VALUES (1, "Tram", 'A');
INSERT INTO Vehicules VALUES (2, "Tram", 'A');
INSERT INTO Vehicules VALUES (3, "Tram", 'A');
INSERT INTO Vehicules VALUES (4, "Tram", 'A');
INSERT INTO Vehicules VALUES (5, "Tram", 'B');
INSERT INTO Vehicules VALUES (6, "Tram", 'B');
INSERT INTO Vehicules VALUES (7, "Tram", 'B');
INSERT INTO Vehicules VALUES (8, "Tram", 'B');
INSERT INTO Vehicules VALUES (9, "Tram", 'B');
INSERT INTO Vehicules VALUES (10, "Tram", 'B');
INSERT INTO Vehicules VALUES (11, "Tram", 'C');
INSERT INTO Vehicules VALUES (12, "Tram", 'C');
INSERT INTO Vehicules VALUES (13, "Tram", 'C');
INSERT INTO Vehicules VALUES (14, "Tram", 'C');
INSERT INTO Vehicules VALUES (15, "Tram", 'C');
INSERT INTO Vehicules VALUES (16, "Tram", 'D');
INSERT INTO Vehicules VALUES (17, "Tram", 'D');
INSERT INTO Vehicules VALUES (18, "Tram", 'D');
INSERT INTO Vehicules VALUES (19, "Tram", 'D');
INSERT INTO Vehicules VALUES (20, "Tram", 'D');
INSERT INTO Vehicules VALUES (21, "Tram", 'E');
INSERT INTO Vehicules VALUES (22, "Tram", 'E');
INSERT INTO Vehicules VALUES (23, "Tram", 'E');
INSERT INTO Vehicules VALUES (24, "Tram", 'E');
INSERT INTO Vehicules VALUES (25, "Tram", 'E');
INSERT INTO Vehicules VALUES (26, "Bus", "C1");
INSERT INTO Vehicules VALUES (27, "Bus", "C1");
INSERT INTO Vehicules VALUES (28, "Bus", "C1");
INSERT INTO Vehicules VALUES (29, "Bus", "C1");
INSERT INTO Vehicules VALUES (30, "Bus", "C1");
INSERT INTO Vehicules VALUES (31, "Bus", "C2");
INSERT INTO Vehicules VALUES (32, "Bus", "C2");
INSERT INTO Vehicules VALUES (33, "Bus", "C2");
INSERT INTO Vehicules VALUES (34, "Bus", "C2");
INSERT INTO Vehicules VALUES (35, "Bus", "C2");
INSERT INTO Vehicules VALUES (36, "Bus", "C3");
INSERT INTO Vehicules VALUES (37, "Bus", "C3");
INSERT INTO Vehicules VALUES (38, "Bus", "C3");
INSERT INTO Vehicules VALUES (39, "Bus", "C3");
INSERT INTO Vehicules VALUES (40, "Bus", "C3");
INSERT INTO Vehicules VALUES (41, "Bus", "C4");
INSERT INTO Vehicules VALUES (42, "Bus", "C4");
INSERT INTO Vehicules VALUES (43, "Bus", "C4");
INSERT INTO Vehicules VALUES (44, "Bus", "C4");
INSERT INTO Vehicules VALUES (45, "Bus", "C4");
INSERT INTO Vehicules VALUES (46, "Bus", "C5");
INSERT INTO Vehicules VALUES (47, "Bus", "C5");
INSERT INTO Vehicules VALUES (48, "Bus", "C5");
INSERT INTO Vehicules VALUES (49, "Bus", "C5");
INSERT INTO Vehicules VALUES (50, "Bus", "C5");


/* Creation des Etapes */
-- Etapes de la ligne A
INSERT INTO Etapes VALUES ('A', "L'Etoile", 1);
INSERT INTO Etapes VALUES ('A', "Edmee Chandon", 2);
INSERT INTO Etapes VALUES ('A', "Denis Papin", 3);
INSERT INTO Etapes VALUES ('A', "Auguste Delaune", 4);
INSERT INTO Etapes VALUES ('A', "Marie Curie", 5);
INSERT INTO Etapes VALUES ('A', "La Rampe - Cantre-Ville", 6);
INSERT INTO Etapes VALUES ('A', "Echirolles Gare", 7);
INSERT INTO Etapes VALUES ('A', "Essarts - La Butte", 8);
INSERT INTO Etapes VALUES ('A', "Surieux", 9);
INSERT INTO Etapes VALUES ('A', "Les Granges", 10);
INSERT INTO Etapes VALUES ('A', "Polesud - Alpexpo", 11);
INSERT INTO Etapes VALUES ('A', "Grand'Place", 12);
INSERT INTO Etapes VALUES ('A', "Arlequin", 13);
INSERT INTO Etapes VALUES ('A', "La Bruyere - Parc Jean Verlhac", 14);
INSERT INTO Etapes VALUES ('A', "Malherbe", 15);
INSERT INTO Etapes VALUES ('A', "MC2 Maison de la Culture", 16);
INSERT INTO Etapes VALUES ('A', "Mounier", 17);
INSERT INTO Etapes VALUES ('A', "Albert 1er de Belgique", 18);
INSERT INTO Etapes VALUES ('A', "Chavant", 19);
INSERT INTO Etapes VALUES ('A', "Verdun Prefecture", 20);
INSERT INTO Etapes VALUES ('A', "Hubert Dubedout - Maison du Tourisme", 21);
INSERT INTO Etapes VALUES ('A', "Victor Hugo", 22);
INSERT INTO Etapes VALUES ('A', "Alsace-Lorraine", 23);
INSERT INTO Etapes VALUES ('A', "Gares", 24);
INSERT INTO Etapes VALUES ('A', "St-Bruno", 25);
INSERT INTO Etapes VALUES ('A', "Berriat - Le Magasin", 26);
INSERT INTO Etapes VALUES ('A', "Les Fontainades - Le Vog", 27);
INSERT INTO Etapes VALUES ('A', "Louis Maisonnat", 28);
INSERT INTO Etapes VALUES ('A', "Fontaine Hotel de Ville La Source", 29);
INSERT INTO Etapes VALUES ('A', "Charles Michels", 30);
INSERT INTO Etapes VALUES ('A', "La Poya", 31);

-- Etapes de la ligne B
INSERT INTO Etapes VALUES ('B', "Plaine des Sports", 1);
INSERT INTO Etapes VALUES ('B', "Gieres Gare - Universites", 2);
INSERT INTO Etapes VALUES ('B', "Mayencin - Champ Roman", 3);
INSERT INTO Etapes VALUES ('B', "Condillac - Universites", 4);
INSERT INTO Etapes VALUES ('B', "Blibliotheques Universitaires", 5);
INSERT INTO Etapes VALUES ('B', "Gabriel Faure", 6);
INSERT INTO Etapes VALUES ('B', "Les Taillees - Universites", 7);
INSERT INTO Etapes VALUES ('B', "Grand Sablon", 8);
INSERT INTO Etapes VALUES ('B', "Michallon", 9);
INSERT INTO Etapes VALUES ('B', "Hopital", 10);
INSERT INTO Etapes VALUES ('B', "Ile Verte", 11);
INSERT INTO Etapes VALUES ('B', "Notre-Dame Musee", 12);
INSERT INTO Etapes VALUES ('B', "Ste-Claire - Les Halles", 13);
INSERT INTO Etapes VALUES ('B', "Hubert Dubedout - Maison du Tourisme", 14);
INSERT INTO Etapes VALUES ('B', "Victor Hugo", 15);
INSERT INTO Etapes VALUES ('B', "Alsace-Lorraine", 16);
INSERT INTO Etapes VALUES ('B', "Gares", 17);
INSERT INTO Etapes VALUES ('B', "St-Bruno", 18);
INSERT INTO Etapes VALUES ('B', "Palais de Justice Gare", 19);
INSERT INTO Etapes VALUES ('B', "Cite Internationale", 20);
INSERT INTO Etapes VALUES ('B', "Marie-Louise Paris - CEA", 21);
INSERT INTO Etapes VALUES ('B', "Oxford", 22);

-- Etapes de la ligne C
INSERT INTO Etapes VALUES ('C', "Le Prisme", 1);
INSERT INTO Etapes VALUES ('C', "Mas des oles", 2);
INSERT INTO Etapes VALUES ('C', "Grand Pre", 3);
INSERT INTO Etapes VALUES ('C', "Fauconniere", 4);
INSERT INTO Etapes VALUES ('C', "Seyssinet-Pariset - Hotel de Ville", 5);
INSERT INTO Etapes VALUES ('C', "Vallier - Catane", 6);
INSERT INTO Etapes VALUES ('C', "Vallier Docteur Calmette", 7);
INSERT INTO Etapes VALUES ('C', "Vallier - Liberation", 8);
INSERT INTO Etapes VALUES ('C', "Foch-Ferrie", 9);
INSERT INTO Etapes VALUES ('C', "Gustave Rivet", 10);
INSERT INTO Etapes VALUES ('C', "Grenoble Hotel de Ville", 11);
INSERT INTO Etapes VALUES ('C', "Flandrin Valmy", 13);
INSERT INTO Etapes VALUES ('C', "Peri - Brossolette", 14);
INSERT INTO Etapes VALUES ('C', "Neyrpic - Belledonne", 15);
INSERT INTO Etapes VALUES ('C', "Hector Berlioz - Universites", 16);
INSERT INTO Etapes VALUES ('C', "Gabriel Faure", 17);
INSERT INTO Etapes VALUES ('C', "Blibliotheques Universitaires", 18);
INSERT INTO Etapes VALUES ('C', "Condillac - Universites", 19);

-- Etapes de la ligne D
INSERT INTO Etapes VALUES ('D', "Etienne Grappe", 1);
INSERT INTO Etapes VALUES ('D', "Parc Jo Blanchon", 2);
INSERT INTO Etapes VALUES ('D', "Edouard Vaillant", 3);
INSERT INTO Etapes VALUES ('D', "Maison Communale", 4);
INSERT INTO Etapes VALUES ('D', "Neyrpic - Belledonne", 5);
INSERT INTO Etapes VALUES ('D', "Les Taillees - Universites", 6);

-- Etapes de la ligne E
INSERT INTO ETapes VALUES ('E', "Louise Michel", 1);
INSERT INTO ETapes VALUES ('E', "Allies", 2);
INSERT INTO ETapes VALUES ('E', "Vallier - Liberation (ligne E)", 3);
INSERT INTO ETapes VALUES ('E', "Condorcet", 4);
INSERT INTO ETapes VALUES ('E', "Alsace-Lorraine (ligne E)", 5);
INSERT INTO ETapes VALUES ('E', "Annie Fratellini-Esplanade", 6);
INSERT INTO ETapes VALUES ('E', "Casamaures - Village", 7);
INSERT INTO ETapes VALUES ('E', "Hotel de Ville (ligne E)", 8);
INSERT INTO ETapes VALUES ('E', "Horloge", 9);
INSERT INTO ETapes VALUES ('E', "Neron", 10);
INSERT INTO ETapes VALUES ('E', "Fiancey - Predieu", 11);
INSERT INTO ETapes VALUES ('E', "Muret", 12);
INSERT INTO ETapes VALUES ('E', "Pont de Vence", 13);
INSERT INTO ETapes VALUES ('E', "La Pinea - St-Robert", 14);
INSERT INTO ETapes VALUES ('E', "Karben", 15);
INSERT INTO ETapes VALUES ('E', "Rafour", 16);
INSERT INTO ETapes VALUES ('E', "Palluel", 17);

-- Etapes de la ligne C1
INSERT INTO Etapes VALUES ("C1", "Pre de l'Eau", 1);
INSERT INTO Etapes VALUES ("C1", "Pre Millet", 2);
INSERT INTO Etapes VALUES ("C1", "INRIA", 3);
INSERT INTO Etapes VALUES ("C1", "Baudonniere", 4);
INSERT INTO Etapes VALUES ("C1", "Busserolles", 5);
INSERT INTO Etapes VALUES ("C1", "Norbert Segard", 6);
INSERT INTO Etapes VALUES ("C1", "Les Bealieres", 7);
INSERT INTO Etapes VALUES ("C1", "Malacher", 8);
INSERT INTO Etapes VALUES ("C1", "Granier", 9);
INSERT INTO Etapes VALUES ("C1", "Meylan Mairie", 10);
INSERT INTO Etapes VALUES ("C1", "Piscine des Buclos", 11);
INSERT INTO Etapes VALUES ("C1", "Le Bret", 12);
INSERT INTO Etapes VALUES ("C1", "La Reviree", 13);
INSERT INTO Etapes VALUES ("C1", "Aiguinards-Hexagone", 14);
INSERT INTO Etapes VALUES ("C1", "Plaine Fleurie", 15);
INSERT INTO Etapes VALUES ("C1", "Carronnerie - Ile d'Amour", 16);
INSERT INTO Etapes VALUES ("C1", "Sablons", 17);
INSERT INTO Etapes VALUES ("C1", "Grenoble Hotel de Ville", 18);
INSERT INTO Etapes VALUES ("C1", "Chavant", 19);
INSERT INTO Etapes VALUES ("C1", "Docteur Martin", 20);
INSERT INTO Etapes VALUES ("C1", "Victor Hugo", 21);
INSERT INTO Etapes VALUES ("C1", "Docteur Mazet", 22);
INSERT INTO Etapes VALUES ("C1", "Gares", 23);
INSERT INTO Etapes VALUES ("C1", "Arago", 24);
INSERT INTO Etapes VALUES ("C1", "Cite Jean Mace", 25);

-- Etapes de la ligne C2
INSERT INTO Etapes VALUES ("C2", "Pont Rouge", 1);
INSERT INTO Etapes VALUES ("C2", "Pont-de-Claix Mairie", 2);
INSERT INTO Etapes VALUES ("C2", "Marcelline", 3);
INSERT INTO Etapes VALUES ("C2", "Irene Joliot-Curie", 4);
INSERT INTO Etapes VALUES ("C2", "L'Amphi", 5);
INSERT INTO Etapes VALUES ("C2", "Iles de Mars", 6);
INSERT INTO Etapes VALUES ("C2", "Clos Dominique", 7);
INSERT INTO Etapes VALUES ("C2", "L'Etoile", 8);
INSERT INTO Etapes VALUES ("C2", "Ecureuil", 9);
INSERT INTO Etapes VALUES ("C2", "Bayard", 10);
INSERT INTO Etapes VALUES ("C2", "Quinzaine", 11);
INSERT INTO Etapes VALUES ("C2", "Navis", 12);
INSERT INTO Etapes VALUES ("C2", "Marielle Franco Rondeau", 13);
INSERT INTO Etapes VALUES ("C2", "Stade Lesdiguière", 14);
INSERT INTO Etapes VALUES ("C2", "Louise Michel", 15);

-- Etapes de la ligne C3
INSERT INTO Etapes VALUES ("C3", "Centre du Graphisme", 1);
INSERT INTO Etapes VALUES ("C3", "Le Village", 2);
INSERT INTO Etapes VALUES ("C3", "Paul Langevin", 3);
INSERT INTO Etapes VALUES ("C3", "Guy Mocquet", 4);
INSERT INTO Etapes VALUES ("C3", "Le Chateau", 5);
INSERT INTO Etapes VALUES ("C3", "Ecoles Hospitalieres", 6);
INSERT INTO Etapes VALUES ("C3", "Hopital Sud", 7);
INSERT INTO Etapes VALUES ("C3", "Francois Quesnay", 8);
INSERT INTO Etapes VALUES ("C3", "Alpexpo", 9);
INSERT INTO Etapes VALUES ("C3", "Polesud - Alpexpo", 10);
INSERT INTO Etapes VALUES ("C3", "Grand'Place", 11);
INSERT INTO Etapes VALUES ("C3", "Edmond Esmonin", 12);
INSERT INTO Etapes VALUES ("C3", "Christophe Turc", 13);
INSERT INTO Etapes VALUES ("C3", "Vigny", 14);
INSERT INTO Etapes VALUES ("C3", "Clos d’Or", 15);
INSERT INTO Etapes VALUES ("C3", "Eugène Sue", 16);
INSERT INTO Etapes VALUES ("C3", "Capuche", 17);
INSERT INTO Etapes VALUES ("C3", "Foch-Ferrie", 18);
INSERT INTO Etapes VALUES ("C3", "Marceau Jardin des Vallons", 19);
INSERT INTO Etapes VALUES ("C3", "Championnet", 20);
INSERT INTO Etapes VALUES ("C3", "Victor Hugo", 21);

-- Etapes de la ligne C4
INSERT INTO Etapes VALUES ("C4", "Victor Hugo", 1);
INSERT INTO Etapes VALUES ("C4", "Docteur Martin", 2);
INSERT INTO Etapes VALUES ("C4", "Chavant", 3);
INSERT INTO Etapes VALUES ("C4", "Driant", 4);
INSERT INTO Etapes VALUES ("C4", "Malifaud", 5);
INSERT INTO Etapes VALUES ("C4", "Bajatiere", 6);
INSERT INTO Etapes VALUES ("C4", "Ponsard", 7);
INSERT INTO Etapes VALUES ("C4", "Paul Claudel", 8);
INSERT INTO Etapes VALUES ("C4", "Teisseire", 9);
INSERT INTO Etapes VALUES ("C4", "Jean Racine", 10);
INSERT INTO Etapes VALUES ("C4", "Maisons Neuves", 11);
INSERT INTO Etapes VALUES ("C4", "General de Gaulle", 12);
INSERT INTO Etapes VALUES ("C4", "Val d’Eybens", 13);
INSERT INTO Etapes VALUES ("C4", "Odyssee", 14);
INSERT INTO Etapes VALUES ("C4", "Les Javaux", 15);
INSERT INTO Etapes VALUES ("C4", "Le Bourg", 16);
INSERT INTO Etapes VALUES ("C4", "Le Verderet", 17);

-- Etapes de la ligne C5
INSERT INTO Etapes VALUES ("C5", "Plaine des Sports", 1);
INSERT INTO Etapes VALUES ("C5", "Esclangon", 2);
INSERT INTO Etapes VALUES ("C5", "Berriat - Le Magasin", 3);
INSERT INTO Etapes VALUES ("C5", "Cemoi", 4);
INSERT INTO Etapes VALUES ("C5", "Vallier - Catane", 5);
INSERT INTO Etapes VALUES ("C5", "Rosa Parks", 6);
INSERT INTO Etapes VALUES ("C5", "Docteur Schweitzer", 7);
INSERT INTO Etapes VALUES ("C5", "Lys Rouge", 8);
INSERT INTO Etapes VALUES ("C5", "Allies", 9);
INSERT INTO Etapes VALUES ("C5", "Marché d'Intérêt National", 10);
INSERT INTO Etapes VALUES ("C5", "Stalingrad Allies", 11);
INSERT INTO Etapes VALUES ("C5", "Flaubert - Clos d'Or", 12);
INSERT INTO Etapes VALUES ("C5", "Malherbe", 13);
INSERT INTO Etapes VALUES ("C5", "Louis Jouvet", 14);
INSERT INTO Etapes VALUES ("C5", "Teisseire", 15);
INSERT INTO Etapes VALUES ("C5", "Paul Cocat", 16);
INSERT INTO Etapes VALUES ("C5", "Andre Argouges", 17);
INSERT INTO Etapes VALUES ("C5", "Saint-Augustin", 18);
INSERT INTO Etapes VALUES ("C5", "Bon Pasteur", 19);
INSERT INTO Etapes VALUES ("C5", "Edouard Vaillant", 20);
INSERT INTO Etapes VALUES ("C5", "Pierre Semard", 21);
INSERT INTO Etapes VALUES ("C5", "Neyrpic - Belledonne", 22);
INSERT INTO Etapes VALUES ("C5", "Clinique Belledonne", 23);
INSERT INTO Etapes VALUES ("C5", "Champ Roman", 24);
INSERT INTO Etapes VALUES ("C5", "Les Alpilles", 25);
INSERT INTO Etapes VALUES ("C5", "Blibliotheques Universitaires", 26);
INSERT INTO Etapes VALUES ("C5", "Universites Biologie", 27);