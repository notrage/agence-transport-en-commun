# Public Transit Agency
This is a university (in collaboration with [Thomas Civade](https://github.com/Luminosaa)) project that aim to create manage a public transit agency using the database in a python gui.
## Installation
To run the Public Transit Agency on your local machine, make sure you have Python 3.8.10 with the booksellers sqllite 2.6.0 and pysimplegui 4.60.4 installed.
1. Clone this git repository :
```bash
git clone git@github.com:notrage/public-transit-agency.git
```
2. Run the Public Transit Agency : 
```bash
python3 public_transit_agency.py
```
or
```bash
python public_transit_agency.py
```
If you only have one Python version on your machine.
## All these features
The features are divided into 2 categories: administrator, who will modify the DB and/or access 'confidential' data, and a user category, which references the data accessible to all.
### Administrator:
- Visualize a table: view any table or view of the DB, we will not be able to view the so-called basic tables, i.e. the one for which there is a view that does not omit data from the initial table.
- Add a driver: via a form, check the validity of the data entered by the administrator (name, surname, bus and/or tram driver) before trying to execute the request, assign the first available number to the new driver to avoid primary key errors, then execute an insert request in Drivers and then DriversModels parameterized with the values of the form.
- Delete Driver: Displays the list of drivers, and allows you to click on a conductor to remove it from the DriversModels table and then from the Drivers table to respect the referential integrity constraints.
- Add a vehicle: via a form, check the validity of the data entered by the administrator (tram or bus, line served) before trying to execute the request, assign the first available number himself to avoid primary key errors, then execute an insert request in Vehicles parameterized with the values of the form.
- Delete Vehicle: Displays the list of vehicles, and allows you to click on a vehicle to remove it from the Vehicles table
- Add a stop: via a form, via a form, check the validity of the data entered by the administrator (name of the available stop, address) and then execute an insert query parameterized with the values of the form.
- Delete Stop: Displays the list of stops, and allows you to click on a stop in order to remove it from the Steps table, decrementing all the ranks of the steps that are on the same row as the Delete stop and have a higher rank than that stop, and then remove from the stop from the Stops table.
- Edit a line: via a form, select the line to be modified, and if you want to add or remove a stop from the line. Add: lists the stops that do not yet appear in the row, and the list of available step ranks, and allows the addition of the selected stop to the desired rank by incrementing all the other order of stops in the same row greater than the one added. Deletion: lists the stops in the row and their ranks, and allows you to click on the desired stop to remove it from the Steps table, then decrements all other rows of stops in the same row less than the deleted one.
- Check the workforce: query displaying the number of vehicles and drivers by type of vehicle, then tell us if there is a shortage or a surplus of staff, and their difference.
- Reset database: resets the entire database and inserts the initial values, i.e. the value of the transports_mtag_values.sql file
### Users:
- Find a route: allows the user to select a start stop and an arrival stop, then construct the graph with all the stops linked only to their neighbour of stages, then performs a journey in width in order to find the shortest path between the start and end stop. Limit: we don't have the distance/duration between stops, so the graph is not weighted, so we don't calculate the fastest path, but the shortest in number of stops.
- Stop Information: displays the list of stops and their addresses, and allows the user to click on one of them in order to have additional information such as:
	- the names of the lines that serve it,
	- the time before the next departure from this stop,
	- the next stop,
	- the terminus of the line
- Rate Information: Generates a form to select the desired rate based on different vehicle models and rate duration, then displays the price and the lines available with that rate