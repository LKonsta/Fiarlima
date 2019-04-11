from application import db

from sqlalchemy.sql import text

class ArmyType(db.Model):

        __tablename__="ArmyType"

        id = db.Column(db.Integer, primary_key=True)

        name = db.Column(db.String(144), nullable=False)
        tag = db.Column(db.String(144), nullable=False)

        unittypes = db.relationship('UnitType', backref='ArmyType', lazy=True)
        units = db.relationship('Unit', backref='ArmyType', lazy=True)


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


class UnitType(db.Model):

        __tablename__ = "UnitType"

        id = db.Column(db.Integer, primary_key=True)

        ArmyType_id = db.Column(db.Integer,db.ForeignKey('ArmyType.id'),nullable=False)

        name = db.Column(db.String(144), nullable=False)
        MaxPoints = db.Column(db.Integer(), nullable=True)
        MinPoints = db.Column(db.Integer(), nullable=True)

        units = db.relationship('Unit', backref='UnitType', lazy=True)

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

                data = text("INSERT INTO UnitType (name, ArmyType_id, MinPoints)"
                            "VALUES ('Core',1,20);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MinPoints)" 
                            "VALUES ('Core',2,25);")
                db.engine.execute(data)

                data = text("INSERT INTO UnitType (name, ArmyType_id)" 
                            "VALUES ('Special',1);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id)" 
                            "VALUES ('Special',2);")
                db.engine.execute(data)

                data = text("INSERT INTO UnitType (name, ArmyType_id, MaxPoints)" 
                            "VALUES ('Terrors of the Wild',1, 40);")
                db.engine.execute(data)
                data = text("INSERT INTO UnitType (name, ArmyType_id, MaxPoints)" 
                            "VALUES ('Ambush Predators',1, 60);")
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

                data = text("INSERT INTO Unit (name, Army_id, UnitType_id, start_cost, start_number, max_amount)"
                        "VALUES ('Cyclops', 1, 49, 355, 1, 1);")
                db.engine.execute(data)
                data = text("INSERT INTO Unit (name, Army_id, UnitType_id, start_cost, start_number, max_amount)"
                        "VALUES ('Gortach', 1, 49, 475, 1, 1);")
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

