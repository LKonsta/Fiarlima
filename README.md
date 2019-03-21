# Fiarlima

A simple web application for making Figure army lists aka Figure army list maker.

The database will consist of three tables for the army point listing and two tables for the making of the lists. The three army tables will be for army type, unit type and the last will be for the units themself. The two tables for making the army lists will consist a table for the making an army and a connecting table with the army making table and the unit type table.

In the table top game for which this listing is made for there are 16 diffrent army types, such as humans, elfs and dwarfs. They all have at least 4 diffrent types of unit types, such as Characters, core, special and from 1 to 3 armies specific own type of unit. These unit types also have a maximum amount of points you can spend on them so the listing will have a system for determining if a list is legal with these limitations. Fro each unit type there will aslo be roughly 5 to 10 diffrent units which have a cost and amount of figures in that unit and the possibility to get more figures into that unit to make it bigger.

Link to currently working [Heroku](https://fiarlima-python-demo.herokuapp.com/) version.

Link to planned [database diagram](../master/documentation/Fiarlima.pdf) and to [use cases](../master/documentation/UseCases.md) .


## Planned list

+ better interface
+ able to choose an army type and make a list, and delete them
+ army type, unit type and unit tables created
+ SQL join type of a deal figured out between diffrent tables
+ ability to have 2 of the same units in the same army list
+ ...


