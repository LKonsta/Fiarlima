from application import db
from application.models import Base

from sqlalchemy.sql import text

class Armylist(Base):
    __tablename__ = "Armylist"

    army_type_id = db.Column(db.Integer, db.ForeignKey('ArmyType.id'), nullable=False)
    name = db.Column(db.String(144), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    done = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    unitsinlist = db.relationship(
        'Unit_Armylist',
        backref='Armylist',
        lazy=True,
        cascade="all, delete-orphan"
    )

    def total_cost(self):
        al_id = self.id
        sql_q = text(f"SELECT sum(Unit_Armylist.final_cost) FROM UnitType "
            f"JOIN Unit ON UnitType.id = Unit.UnitType_id "
            f"JOIN Unit_Armylist ON Unit.id = Unit_Armylist.Unit_id "
            f"JOIN Armylist ON Unit_Armylist.Armylist_id = Armylist.id "
            f"WHERE Unit_Armylist.Armylist_id = {al_id};")
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
        sql_q = text(f"SELECT sum(Unit_Armylist.final_cost) FROM UnitType "
            f"JOIN Unit ON UnitType.id = Unit.UnitType_id "
            f"JOIN Unit_Armylist ON Unit.id = Unit_Armylist.Unit_id "
            f"JOIN Armylist ON Unit_Armylist.Armylist_id = Armylist.id "
            f"WHERE UnitType.id = {unittype_id} AND "
            f"Unit_Armylist.Armylist_id = {al_id};")
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
    __tablename__ = "Unit_Armylist"

    id = db.Column(db.Integer, primary_key=True)
    Armylist_id = db.Column(db.Integer, db.ForeignKey('Armylist.id'), nullable=False)
    Unit_id = db.Column(db.Integer, db.ForeignKey('Unit.id'), nullable=False)
    unit = db.relationship("Unit")
    amount = db.Column(db.Integer, nullable=False)
    final_cost = db.Column(db.Integer, nullable=True)
    updates = db.relationship(
        "Unit_ArmylistUpdate",
        backref='unit_in_army_list',
        lazy=True,
        cascade="all, delete-orphan"
    )

    def __init__(self, Unit_id, amount):
        self.Unit_id = Unit_id
        self.amount = amount

    def cost(self):
        return self.final_cost


class Unit_ArmylistUpdate(db.Model):
    __tablename__ = "Unit_ArmylistUpdate"

    unit_army_list_id = db.Column(db.Integer, db.ForeignKey('Unit_Armylist.id'), nullable=False, primary_key=True)
    update_id = db.Column(db.Integer, db.ForeignKey('UnitUpdates.id'), nullable=False, primary_key=True)
