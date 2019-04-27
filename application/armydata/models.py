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


class UnitType(db.Model):

        __tablename__ = "UnitType"

        id = db.Column(db.Integer, primary_key=True)

        ArmyType_id = db.Column(db.Integer,db.ForeignKey('ArmyType.id'),nullable=False)

        name = db.Column(db.String(144), nullable=False)
        MaxPoints = db.Column(db.Integer(), nullable=True)
        MinPoints = db.Column(db.Integer(), nullable=True)

        units = db.relationship('Unit', backref='unit_type', lazy=True)


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



	@staticmethod
	def unit_data_fill():

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
