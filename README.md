# Fiarlima

A simple web application for making Figure army lists aka Figure army list maker.

So as it is said the program is used for making figure army lists, for a table top game called Warhammer.
Except that the points and rules are from a diffrent source, because of a major rule changes within the real warhammer fantasy game.

In the table top game for which this listing system is made for there are 16 diffrent army types, such as humans, elfs and dwarfs. 
They all have at least 4 diffrent types of unit types, such as Characters, core, special and from 1 to 3 armies specific own type of unit. 
These unit types also have a maximum amount of points you can spend on them so the listing will have a system for determining if a list is legal with these limitations. 
For each unit type there will aslo be roughly 5 to 10 diffrent units which have a cost and amount of figures in that unit and the possibility to get more figures into that unit to make it bigger.

Link to currently working [Heroku](https://fiarlima-python-demo.herokuapp.com/) version 
(unfortunately without the data from lists.db). 

Link to planned [database diagram](../master/documentation/Fiarlima.pdf) and to [use cases](../master/documentation/UseCases.md) .

The site checks if the tables are empty when opening army data and if they are it fills them.

looking in the armydata/models.py file you can see what it is supposed to fill it with. [Picture1](../master/documentation/armydata1.png)  [picture2](../master/documentation/armydata2.png) 

How to use [Tutorial](../master/documentation/howdo.md)

## How to set up

First time setup

1 . <code>python3 -m venv venv</code>

2 . <code>source venv/bin/activate</code>

3 . <code>pip install Flask</code>

4 . <code>pip install flask-sqlalchemy</code>

5 . <code>pip install flask-wtf</code>

6 . <code>pip install flask-login</code>

To initialize database use command

<code>FLASK_APP=application flask init-db-test2</code> 

To drop the database if there is any problems use command

<code>FLASK_APP=application flask drop-db</code>

To start the app use command

<code>python run.py</code>

## Planned list

+ ~~better interface~~
+ ~~able to choose an army type and make a list~~ 
+ ~~able to delete lists~~
+ ~~army type, unit type and unit tables created~~
+ ~~SQL join type of a deal figured out between diffrent tables~~
+ ~~ability to create users (for now the heroku version is pretty useless)~~
+ ~~have the armydata tables filled when the program is opened~~
+ ~~ability to have 2 of the same units in the same army list~~
+ ~~working point counter and maximum point restrictions on diffrent unittype categories~~
+ ~~simple unit updates~~


