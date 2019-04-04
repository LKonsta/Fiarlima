from application import db
from application.models import Base

class Armylist(Base):
        army_id = db.Column(db.Integer, db.ForeignKey('ArmyType.id'),nullable=False)
        name = db.Column(db.String(144), nullable=False)
        points = db.Column(db.Integer, nullable=False)
        done = db.Column(db.Boolean, nullable=False)

        account_id = db.Column(db.Integer, db.ForeignKey('account.id'),nullable=False)

        def __init__(self, name, points, army_id):
                self.army_id = army_id;
                self.name = name
                self.done = False
                self.points = points




