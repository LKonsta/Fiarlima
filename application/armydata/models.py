from application import db


class ArmyType(db.Model):
    __tablename__ = "armytype"

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
    __tablename__ = "unittype"

    id = db.Column(db.Integer, primary_key=True)

    ArmyType_id = db.Column(db.Integer, db.ForeignKey('armytype.id'), nullable=False)

    name = db.Column(db.String(144), nullable=False)
    MaxPoints = db.Column(db.Integer(), nullable=True)
    MinPoints = db.Column(db.Integer(), nullable=True)

    units = db.relationship('Unit', backref='unit_type', lazy=True)


class Unit(db.Model):
    __tablename__ = "unit"

    id = db.Column(db.Integer, primary_key=True)

    Army_id = db.Column(db.Integer, db.ForeignKey('armytype.id'), nullable=False)
    UnitType_id = db.Column(db.Integer, db.ForeignKey('unittype.id'), nullable=False)

    name = db.Column(db.String(144), nullable=False)
    start_cost = db.Column(db.Integer, nullable=False)
    cost_per = db.Column(db.Integer, nullable=True)
    start_number = db.Column(db.Integer, nullable=False)
    max_amount = db.Column(db.Integer, nullable=False)

    default_updates = db.Column(db.Boolean, nullable=False)

    updates = db.relationship('UnitUpdates', backref='unit', lazy=True)


class UnitUpdates(db.Model):
    __tablename__ = "unitupdates"

    id = db.Column(db.Integer, primary_key=True)

    unit_id = db.Column(db.Integer, db.ForeignKey('unit.id'), nullable=True)

    name = db.Column(db.String(144), nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    per = db.Column(db.Boolean, nullable=True)

    units = db.relationship("Unit_Armylistupdate", backref='update', lazy=True)