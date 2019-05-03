from application import db
from application.models import Base

from sqlalchemy.sql import text

class Armylist(Base):
    __tablename__ = "armylist"

    army_type_id = db.Column(db.Integer, db.ForeignKey('armytype.id'), nullable=False)
    name = db.Column(db.String(144), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    done = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    unitsinlist = db.relationship(
        'Unit_Armylist',
        backref='armylist',
        lazy=True,
        cascade="all, delete-orphan"
    )

    def total_cost(self):
        al_id = self.id
        sql_q = text("SELECT sum(unit_armylist.final_cost) FROM unittype JOIN unit ON unittype.id = unit.UnitType_id JOIN unit_armylist ON unit.id = unit_armylist.Unit_id JOIN armylist ON unit_armylist.Armylist_id = armylist.id WHERE unit_armylist.Armylist_id = :al_id").params(al_id=al_id)
        total = db.engine.execute(sql_q)
        for row in total:
            if not row[0]:
                return 0
            else:
                return row[0]

    def legal(self):
        if self.total_cost() > self.points:
            return False
        for ut in self.army_type.unittypes:
            if not self.unit_type_of_army_precent_valid(ut):
                return False
        return True

    def cost_per_unit_type(self, unittype_id):
        al_id = self.id
        sql_q = text("SELECT sum(unit_armylist.final_cost) FROM unittype JOIN unit ON unittype.id = unit.UnitType_id JOIN unit_armylist ON unit.id = unit_armylist.Unit_id JOIN armylist ON unit_armylist.Armylist_id = armylist.id WHERE unittype.id = :ut_id AND unit_armylist.Armylist_id = :al_id").params(ut_id=unittype_id, al_id=al_id)
        total = db.engine.execute(sql_q)
        for row in total:
            if not row[0]:
                return 0
            else:
                return row[0]

    def unit_type_precent_of_army(self, unittype_id):
        cost = self.cost_per_unit_type(unittype_id)
        precent = cost / self.points * 100
        return round(precent, 2)

    def unit_type_of_army_precent_valid(self, unit_type):
        if unit_type.MaxPoints:
            if self.unit_type_precent_of_army(unit_type.id) > unit_type.MaxPoints:
                return False
        if unit_type.MinPoints:
            if self.unit_type_precent_of_army(unit_type.id) < unit_type.MinPoints:
                return False
        return True

    def __init__(self, name, points):
        self.name = name
        self.done = False
        self.points = points


class Unit_Armylist(db.Model):
    __tablename__ = "unit_armylist"

    id = db.Column(db.Integer, primary_key=True)
    Armylist_id = db.Column(db.Integer, db.ForeignKey('armylist.id'), nullable=False)
    Unit_id = db.Column(db.Integer, db.ForeignKey('unit.id'), nullable=False)
    unit = db.relationship("Unit")
    amount = db.Column(db.Integer, nullable=False)
    final_cost = db.Column(db.Integer, nullable=True)
    updates = db.relationship(
        "Unit_Armylistupdate",
        backref='unit_in_army_list',
        lazy=True,
        cascade="all, delete-orphan"
    )

    def __init__(self, Unit_id, amount):
        self.Unit_id = Unit_id
        self.amount = amount

    def cost(self):
        return self.final_cost


class Unit_Armylistupdate(db.Model):
    __tablename__ = "unit_armylist_update"

    unit_army_list_id = db.Column(db.Integer, db.ForeignKey('unit_armylist.id'), nullable=False, primary_key=True)
    update_id = db.Column(db.Integer, db.ForeignKey('unitupdates.id'), nullable=False, primary_key=True)
