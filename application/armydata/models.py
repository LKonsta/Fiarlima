from application import db

from sqlalchemy.sql import text

class ArmyType(db.Model):

        __tablename__="ArmyType"

        id = db.Column(db.Integer, primary_key=True)

        name = db.Column(db.String(144), nullable=False)
        tag = db.Column(db.String(144), nullable=False)

        armylist = db.relationship('Armylist', backref='army_type', lazy=True)
        unittypes = db.relationship('UnitType', backref='army_type', lazy=True)
        units = db.relationship('Unit', backref='army_type', lazy=True)


        def __init__(self, name, tag):
                self.name = name
                self.tag = tag

        @staticmethod
        def is_army_type_empty():
                q = text("SELECT COUNT(id) FROM ArmyType;")
                value = (db.engine.execute(q))
                for row in value:
                        return row[0]

        @staticmethod
        def army_type_data_fill():
                data = text("INSERT INTO ArmyType (name, tag) VALUES ('Beast Herds','BH');")
                db.engine.execute(data)
                data = text("INSERT INTO ArmyType (name, tag) VALUES ('Daemon Legions','DL');")
                db.engine.execute(data)
                data = text("INSERT INTO ArmyType (name, tag) VALUES ('Dread Elves','DE');")
                db.engine.execute(data)
                data = text("INSERT INTO ArmyType (name, tag) VALUES ('Dwarven Holds','DH');")
                db.engine.execute(data)
                data = text("INSERT INTO ArmyType (name, tag) VALUES ('Empire of Sonnsthal','EoS');")
                db.engine.execute(data)
                data = text("INSERT INTO ArmyType (name, tag) VALUES ('Highborn Elves','HE');")
                db.engine.execute(data)
                data = text("INSERT INTO ArmyType (name, tag) VALUES ('Infernal Dwarves','ID');")
                db.engine.execute(data)
                data = text("INSERT INTO ArmyType (name, tag) VALUES ('Kingdom of Equitaine','KoE');")
                db.engine.execute(data)
                data = text("INSERT INTO ArmyType (name, tag) VALUES ('Ogre Khans','OK');")
                db.engine.execute(data)
                data = text("INSERT INTO ArmyType (name, tag) VALUES ('Orcs and Goblins','OG');")
                db.engine.execute(data)
                data = text("INSERT INTO ArmyType (name, tag) VALUES ('Saurian Ancients','SA');")
                db.engine.execute(data)
                data = text("INSERT INTO ArmyType (name, tag) VALUES ('Sylvan Elves','SE');")
                db.engine.execute(data)
                data = text("INSERT INTO ArmyType (name, tag) VALUES ('The Vermin Swarm','VS');")
                db.engine.execute(data)
                data = text("INSERT INTO ArmyType (name, tag) VALUES ('Undying Dynasties','UD');")
                db.engine.execute(data)
                data = text("INSERT INTO ArmyType (name, tag) VALUES ('Vampire Covenant','VC');")
                db.engine.execute(data)
                data = text("INSERT INTO ArmyType (name, tag) VALUES ('Warriors of the Dark Gods','WDK');")
                db.engine.execute(data)

class UnitType(db.Model):

        __tablename__ = "UnitType"

        id = db.Column(db.Integer, primary_key=True)

        ArmyType_id = db.Column(db.Integer,db.ForeignKey('ArmyType.id'),nullable=False)

        name = db.Column(db.String(144), nullable=False)
        MaxPoints = db.Column(db.Integer(), nullable=True)
        MinPoints = db.Column(db.Integer(), nullable=True)

        units = db.relationship('Unit', backref='unit_type', lazy=True)

        def __init__(self, name, Army_id, MaxPoints, MinPoints):
                self.name = name
                self.Army = Army_id
                self.MaxPoints = MaxPoints
                self.MinPoints = MinPoints

        @staticmethod
        def is_unit_type_empty():
                q = text("SELECT COUNT(id) FROM UnitType;")
                value = (db.engine.execute(q))
                for row in value:
                        return row[0]

        @staticmethod
        def unit_type_data_fill():
                data = text("INSERT INTO UnitType (name, ArmyType_id, MaxPoints)" 
                            "VALUES ('Characters',1,40);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MaxPoints)" 
                            "VALUES ('Characters',2,40);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MaxPoints)" 
                            "VALUES ('Characters',3,40);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MaxPoints)" 
                            "VALUES ('Characters',4,40);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MaxPoints)" 
                            "VALUES ('Characters',5,40);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MaxPoints)" 
                            "VALUES ('Characters',6,40);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MaxPoints)" 
                            "VALUES ('Characters',7,40);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MaxPoints)" 
                            "VALUES ('Characters',8,40);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MaxPoints)" 
                            "VALUES ('Characters',9,40);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MaxPoints)" 
                            "VALUES ('Characters',10,40);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MaxPoints)" 
                            "VALUES ('Characters',11,40);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MaxPoints)" 
                            "VALUES ('Characters',12,40);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MaxPoints)" 
                            "VALUES ('Characters',13,40);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MaxPoints)" 
                            "VALUES ('Characters',14,40);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MaxPoints)" 
                            "VALUES ('Characters',15,40);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MaxPoints)" 
                            "VALUES ('Characters',16,40);")
                db.engine.execute(data)

                data = text("INSERT INTO UnitType (name, ArmyType_id, MinPoints)" 
                            "VALUES ('Core',1,20);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MinPoints)" 
                            "VALUES ('Core',2,25);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MinPoints)" 
                            "VALUES ('Core',3,25);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MinPoints)" 
                            "VALUES ('Core',4,25);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MinPoints)" 
                            "VALUES ('Core',5,25);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MinPoints)" 
                            "VALUES ('Core',6,25);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MinPoints)" 
                            "VALUES ('Core',7,25);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MinPoints)" 
                            "VALUES ('Core',8,25);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MinPoints)" 
                            "VALUES ('Core',9,25);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MinPoints)" 
                            "VALUES ('Core',10,25);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MinPoints)" 
                            "VALUES ('Core',11,25);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MinPoints)" 
                            "VALUES ('Core',12,25);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MinPoints)" 
                            "VALUES ('Core',13,25);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MinPoints)" 
                            "VALUES ('Core',14,25);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MinPoints)" 
                            "VALUES ('Core',15,25);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MinPoints)" 
                            "VALUES ('Core',16,25);")
                db.engine.execute(data)

                data = text("INSERT INTO UnitType (name, ArmyType_id)" 
                            "VALUES ('Special',1);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id)" 
                            "VALUES ('Special',2);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id)" 
                            "VALUES ('Special',3);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id)" 
                            "VALUES ('Special',4);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id)" 
                            "VALUES ('Special',5);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id)" 
                            "VALUES ('Special',6);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id)" 
                            "VALUES ('Special',7);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id)" 
                            "VALUES ('Special',8);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id)" 
                            "VALUES ('Special',9);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id)" 
                            "VALUES ('Special',10);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id)" 
                            "VALUES ('Special',11);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id)" 
                            "VALUES ('Special',12);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id)" 
                            "VALUES ('Special',13);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id)" 
                            "VALUES ('Special',14);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id)" 
                            "VALUES ('Special',15);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id)" 
                            "VALUES ('Special',16);")
                db.engine.execute(data)

                data = text("INSERT INTO UnitType (name, ArmyType_id, MaxPoints)" 
                            "VALUES ('Terrors of the Wild',1, 40);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MaxPoints)" 
                            "VALUES ('Ambush Predators',1, 60);")
                db.engine.execute(data)

                data = text("INSERT INTO UnitType (name, ArmyType_id, MaxPoints)" 
                            "VALUES ('Aves',2, 35);")
                db.engine.execute(data)

                data = text("INSERT INTO UnitType (name, ArmyType_id, MaxPoints)" 
                            "VALUES ('Raiders',3, 30);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MaxPoints)" 
                            "VALUES ('Destroyers',3, 15);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MaxPoints)" 
                            "VALUES ('The Menagerie',3, 30);")
                db.engine.execute(data)

                data = text("INSERT INTO UnitType (name, ArmyType_id, MaxPoints)" 
                            "VALUES ('Clans` Thunder',4, 35);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MaxPoints)" 
                            "VALUES ('Engines of War',4, 20);")
                db.engine.execute(data)

class Unit(db.Model):

	__tablename__ = "Unit"

	id = db.Column(db.Integer, primary_key=True)

	Army_id = db.Column(db.Integer,db.ForeignKey('ArmyType.id'),nullable=False)
	UnitType_id = db.Column(db.Integer,db.ForeignKey('UnitType.id'),nullable=False)

	name = db.Column(db.String(144), nullable=False)
	start_cost = db.Column(db.Integer, nullable=False)
	cost_per = db.Column(db.Integer, nullable=True)
	start_number = db.Column(db.Integer, nullable=False)
	max_amount = db.Column(db.Integer, nullable=False)

	def __init__(self, name, start_cost, cost_per, start_number, max_amount):
		self.name = name
		self.start_cost = start_cost
		self.cost_per = cost_per
		self.start_number = start_number
		self.max_amount = max_amount


	@staticmethod
	def is_unit_empty():
		q = text("SELECT COUNT(id) FROM Unit;")
		value = (db.engine.execute(q))
		for row in value:
			return row[0]

	@staticmethod
	def unit_data_fill():
                data = text("INSERT INTO Unit (name, Army_id, UnitType_id, start_cost, start_number, max_amount)"
                        "VALUES ('Beast Lord', 1, 1, 215, 1, 1);")
                db.engine.execute(data)
                data = text("INSERT INTO Unit (name, Army_id, UnitType_id, start_cost, start_number, max_amount)"
                        "VALUES ('Beast Chieftain', 1, 1, 120, 1, 1);")
                db.engine.execute(data)
                data = text("INSERT INTO Unit (name, Army_id, UnitType_id, start_cost, start_number, max_amount)"
                        "VALUES ('Soothsayer', 1, 1, 155, 1, 1);")
                db.engine.execute(data)
                data = text("INSERT INTO Unit (name, Army_id, UnitType_id, start_cost, start_number, max_amount)"
                        "VALUES ('Minotaur Warlord', 1, 1, 490, 1, 1);")
                db.engine.execute(data)
                data = text("INSERT INTO Unit (name, Army_id, UnitType_id, start_cost, start_number, max_amount)"
                        "VALUES ('Minotaur Chieftain', 1, 1, 220, 1, 1);")
                db.engine.execute(data)
                data = text("INSERT INTO Unit (name, Army_id, UnitType_id, start_cost, start_number, max_amount)"
                        "VALUES ('Centaur Chieftain', 1, 1, 220, 1, 1);")
                db.engine.execute(data)

                data = text("INSERT INTO Unit (name, Army_id, UnitType_id, start_cost, cost_per, start_number, max_amount)"
                        "VALUES ('Wildhorn Herd', 1, 17, 150, 10, 15, 50);")
                db.engine.execute(data)
                data = text("INSERT INTO Unit (name, Army_id, UnitType_id, start_cost, cost_per, start_number, max_amount)"
                        "VALUES ('Mongrel Herd', 1, 17, 140, 8, 20, 50);")
                db.engine.execute(data)
                data = text("INSERT INTO Unit (name, Army_id, UnitType_id, start_cost, cost_per, start_number, max_amount)"
                        "VALUES ('Mongrel Raiders', 1, 17, 95, 7, 10, 20);")
                db.engine.execute(data)

                data = text("INSERT INTO Unit (name, Army_id, UnitType_id, start_cost, cost_per, start_number, max_amount)"
                        "VALUES ('Feral Hounds', 1, 33, 80, 8, 5, 20);")
                db.engine.execute(data)
                data = text("INSERT INTO Unit (name, Army_id, UnitType_id, start_cost, cost_per, start_number, max_amount)"
                        "VALUES ('Longhorn Herd', 1, 33, 155, 23, 10, 40);")
                db.engine.execute(data)
                data = text("INSERT INTO Unit (name, Army_id, UnitType_id, start_cost, cost_per, start_number, max_amount)"
                        "VALUES ('Minotaurs', 1, 33, 235, 78, 3, 10);")
                db.engine.execute(data)
                data = text("INSERT INTO Unit (name, Army_id, UnitType_id, start_cost, cost_per, start_number, max_amount)"
                        "VALUES ('Centaurs', 1, 33, 165, 25, 5, 15);")
                db.engine.execute(data)
                data = text("INSERT INTO Unit (name, Army_id, UnitType_id, start_cost, cost_per, start_number, max_amount)"
                        "VALUES ('Riding Chariot', 1, 33, 110, 110, 1, 3);")
                db.engine.execute(data)
                data = text("INSERT INTO Unit (name, Army_id, UnitType_id, start_cost, cost_per, start_number, max_amount)"
                        "VALUES ('Razortusk Herd', 1, 33, 100, 62, 1, 10);")
                db.engine.execute(data)
                data = text("INSERT INTO Unit (name, Army_id, UnitType_id, start_cost, start_number, max_amount)"
                        "VALUES ('Razortusk Chariot', 1, 33, 230, 1, 1);")
                db.engine.execute(data)
                data = text("INSERT INTO Unit (name, Army_id, UnitType_id, start_cost, start_number, max_amount)"
                        "VALUES ('Briar Beast', 1, 33, 120, 1, 1);")
                db.engine.execute(data)
                data = text("INSERT INTO Unit (name, Army_id, UnitType_id, start_cost, cost_per, start_number, max_amount)"
                        "VALUES ('Gragoyles', 1, 33, 135, 17, 5, 10);")
                db.engine.execute(data)

                data = text("INSERT INTO Unit (name, Army_id, UnitType_id, start_cost, start_number, max_amount)"
                        "VALUES ('Cyclops', 1, 49, 355, 1, 1);")
                db.engine.execute(data)
                data = text("INSERT INTO Unit (name, Army_id, UnitType_id, start_cost, start_number, max_amount)"
                        "VALUES ('Gortach', 1, 49, 475, 1, 1);")
                db.engine.execute(data)
                data = text("INSERT INTO Unit (name, Army_id, UnitType_id, start_cost, start_number, max_amount)"
                        "VALUES ('Jabberwock', 1, 49, 340, 1, 1);")
                db.engine.execute(data)
                data = text("INSERT INTO Unit (name, Army_id, UnitType_id, start_cost, start_number, max_amount)"
                        "VALUES ('Beast Giant', 1, 49, 300, 1, 1);")
                db.engine.execute(data)

                data = text("INSERT INTO Unit (name, Army_id, UnitType_id, start_cost, start_number, max_amount)"
                        "VALUES ('Harbringer of Father Chaos', 2, 2, 150, 1, 1);")
                db.engine.execute(data)
                data = text("INSERT INTO Unit (name, Army_id, UnitType_id, start_cost, start_number, max_amount)"
                        "VALUES ('Kuulima´s Deceiver', 2, 2, 335, 1, 1);")
                db.engine.execute(data)
                data = text("INSERT INTO Unit (name, Army_id, UnitType_id, start_cost, start_number, max_amount)"
                        "VALUES ('Maw of Akaan', 2, 2, 565, 1, 1);")
                db.engine.execute(data)
                data = text("INSERT INTO Unit (name, Army_id, UnitType_id, start_cost, start_number, max_amount)"
                        "VALUES ('Miser of Sugulag', 2, 2, 670, 1, 1);")
                db.engine.execute(data)
                data = text("INSERT INTO Unit (name, Army_id, UnitType_id, start_cost, start_number, max_amount)"
                        "VALUES ('Courtesan of Cibaresh', 2, 2, 575, 1, 1);")
                db.engine.execute(data)
                data = text("INSERT INTO Unit (name, Army_id, UnitType_id, start_cost, start_number, max_amount)"
                        "VALUES ('Omen of Savar', 2, 2, 490, 1, 1);")
                db.engine.execute(data)
                data = text("INSERT INTO Unit (name, Army_id, UnitType_id, start_cost, start_number, max_amount)"
                        "VALUES ('Sentinel of Nukuja', 2, 2, 620, 1, 1);")
                db.engine.execute(data)
                data = text("INSERT INTO Unit (name, Army_id, UnitType_id, start_cost, start_number, max_amount)"
                        "VALUES ('Vanadra´s Scourge', 2, 2, 705, 1, 1);")
                db.engine.execute(data)
