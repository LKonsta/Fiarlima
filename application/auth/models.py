from application import db
from application.models import Base

from sqlalchemy.sql import text

class User(Base):

	__tablename__ = "account"

	name = db.Column(db.String(144), nullable=False)
	username = db.Column(db.String(144), nullable=False)
	password = db.Column(db.String(144), nullable=False)

	lists = db.relationship("Armylist", backref='account', lazy=True)

	def get_total_user_count(self):
		sql_q = text("SELECT COUNT(id) FROM account")
		ans = db.engine.execute(sql_q)
		for row in ans:
			if row[0] == None:
				return f" no users"
			else:
				return f" {row[0]}"

	def get_most_army_count(self):
		sql_q = text("SELECT account.name, COUNT(1) AS count FROM Armylist JOIN account ON armylist.account_id = account.id GROUP BY account.id ORDER BY count DESC")

		ans = db.engine.execute(sql_q)
		for row in ans:
				txt = f" {row[0]} , with {row[1]} list(s)"
				return txt

	def get_total_army_list_count(self):
		sql_q = text("SELECT COUNT(Armylist.account_id) AS count FROM account JOIN Armylist ON account.id = armylist.account_id ORDER BY count")
		ans = db.engine.execute(sql_q)
		for row in ans:
			return row[0]

	def __init__(self, name, username, password):
		self.name = name
		self.username = username
		self.password = password

	def get_id(self):
		return self.id

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def is_authenticated(self):
		return True

