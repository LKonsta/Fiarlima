from application import db
from application.models import Base

class Armylist(Base):

        __tablename__ = "Armylist"

        army_type_id = db.Column(db.Integer, db.ForeignKey('ArmyType.id'),nullable=False)
        name = db.Column(db.String(144), nullable=False)
        points = db.Column(db.Integer, nullable=False)
        done = db.Column(db.Boolean, nullable=False)

        account_id = db.Column(db.Integer, db.ForeignKey('account.id'),nullable=False)

        unitsinlist = db.relationship('Unit_Armylist', backref='Armylist', lazy=True)

        def __init__(self, name, points):
                self.name = name
                self.done = False
                self.points = points


class Unit_Armylist(db.Model):

	__tablename__ = "Unit_Armylist"

	id = db.Column(db.Integer, primary_key=True)
	Armylist_id = db.Column(db.Integer, db.ForeignKey('Armylist.id'), nullable=False)
	Unit_id = db.Column(db.Integer, db.ForeignKey('Unit.id'), nullable=False)
	unit = db.relationship("Unit")
	amount = db.Column(db.Integer, nullable=False)
	Cost = db.Column(db.Integer, nullable=False)

	def __init__(self, Unit_id, amount):
		self.Unit_id = Unit_id
		self.amount = amount
