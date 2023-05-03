# Logiciel développé en Python 3.8.10 avec les libraires sqlite3 2.6.0 et pysimplegui 4.60.4

Les fonctionnalités sont divisés en 2 catégorie : administrateur, qui vont modifier la DB et/ou accéder aux données ‘confidentielles’, et une catégorie utilisateurs, qui références les données accessible à tous. 
## Administrateur :
-Visualiser une table : visualiser n’importe quelle table ou view de la DB, on ne pourra pas visualiser les tables dites de base, soit celle dont il existe une view qui n’omets pas de données de la table initiale.

-Ajouter un conducteur : via un formulaire, vérifie la validité des données entrées par l’administrateur (nom, prenom, conduit bus et/ou tram) avant d’essayer d’exécuter la requête, assigne lui même le premier matricule disponible au nouveau conducteur pour éviter des erreurs de primary key, puis exécute une requête insert dans Conducteurs puis ConducteursModeles paramétrées avec les valeurs du formulaire. 

-Supprimer un conducteur : affiche la liste des conducteurs, et permet de cliquer sur un conducteurs afin de le supprimer de la table ConducteursModeles puis de la table Conducteurs pour respecter les contraintes d’intégrités référentielles. 

-Ajouter un véhicule : via un formulaire , vérifie la validité des données entrées par l’administrateur (tram ou bus, ligne desservie) avant d’essayer d’exécuter la requête, assigne lui même le premier numéro disponible pour éviter des erreurs de primary key, puis exécute une requête insert dans Vehicules paramétrées avec les valeurs du formulaire. 

-Supprimer un véhicule : affiche la liste des véhicules, et permet de cliquer sur un véhicule  afin de le supprimer de la table Vehicules

-Ajouter un arrêt : via un formulaire,  via un formulaire, vérifie la validité des données entrées par l’administrateur (nom de l’arrêt disponible, adresse) puis exécute une requête insert paramétrées avec les valeurs du formulaire. 

-Supprimer un arrêt : affiche la liste des arrêts, et permet de cliquer sur un arrêt afin de le supprimer de la table Etapes, en décrémentant tout les rangs des étapes étant sur la même ligne que l’arrêt supprimer et ayant un rang supérieur à cet arrêt, puis supprimer de l’arrêt de la table Arrets. 

-Modifier une ligne : via un formulaire, sélectionner la ligne à modifier, et si on souhaite ajouter ou supprimer un arrêt de la ligne.
	Ajout : liste les arrêts n’apparaissant pas encore dans la ligne, et la liste 	des rangs d’étapes disponible, et permet l’ajout de l’arrêt sélectionner au 	rang voulu en incrémentant tout les autres rang d’arrêts de la même ligne 	supérieur à celui ajouté.
	Suppression : liste les arrêts de la ligne et leur rang, et permet de cliquer 	sur l’arrêt voulu afin de le supprimer de la table Etapes, puis décrémente 	tout les autres rang d’arrêts de la même ligne inférieur à celui supprimé.

-Vérifier les effectifs : requête affichant le nombre de véhicule et de conducteur par type de véhicule, puis nous dis donc si il y a un manque ou un surplus d’effectif, et leur différence. 

-Réinitialiser la base de donnée : réinitialise toute la base de données et insert les valeurs initiales, soit celle du fichier transports_mtag_values.sql 

## Utilisateurs :
-Trouver un parcours : permet à l’utilisateur de sélectionner un arrêt de départ et un arrêt d’arriver, puis construit le graphe avec tout les arrêts relier uniquement à leur voisin d’étapes, puis effectue un parcours en largeur afin de trouver le chemin le plus court entre l’arrêt de départ et celui d’arrivée. 
Limite : nous n’avons pas la distance/durée entre les arrêts, donc le graphe n’est pas pondéré, donc on ne calcul par le chemin le plus rapide, mais le plus court en nombre d’arrêt. 

-Informations sur un arrêt : affiche la liste des arrêts et leur adresse, et permet à l’utilisateur de cliquer sur l’un d’entre eux afin d’avoir des informations supplémentaires tel que :
	-le nom des lignes qui le desservent, 
	-le temps avant le prochain départ de cet arrêt,
	-le prochain arrêt,
	-le terminus de la ligne
- Informations sur un tarif : génère un formulaire pour sélectionner le tarif souhaiter en fonction des différents modeles de véhicule et durée des tarifs, puis affiche le prix ainsi que les lignes accessibles avec cette tarification