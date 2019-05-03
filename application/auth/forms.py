from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField

from application import db

class LoginForm(FlaskForm):
	username = StringField("Username")
	password = PasswordField("Password")

	class Meta:
		csrf = False

class NewUserForm(FlaskForm):
	name = StringField("Name")
	username = StringField("Username")
	password = PasswordField("Password")

	def validate(self):
		super_validate = super().validate()
		if not super_validate:
			return False
		bol = True
		insert = self.name.data
		sql_q = f"SELECT * FROM account " \
			f"WHERE name = '{ insert }';"
		ans = db.engine.execute(sql_q)
		for row in ans:
			if not row[0] == None:
				self.name.errors.append(f'Taken!')
				bol = False

		insert2 = self.username.data
		sql_q = f"SELECT * FROM account " \
			f"WHERE username = '{insert2}';"
		ans = db.engine.execute(sql_q)
		for row in ans:
			if not row[0] == None:
				self.username.errors.append(f'Taken!')
				bol = False

		return bol


	class Meta:
		csrf = False


class EditNameForm(FlaskForm):
	name = StringField("new name")

	def validate(self):
		super_validate = super().validate()
		if not super_validate:
			return False

		bol = True
		insert = self.name.data
		sql_q = f"SELECT * FROM account " \
			f"WHERE name = '{insert}';"
		ans = db.engine.execute(sql_q)
		for row in ans:
			if not row[0] == None:
				self.name.errors.append(f'Taken!')
				bol = False

		return bol

	class Meta:
		csrf = False