from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class ListsForm(FlaskForm):
	name = StringField("List name", [validators.length(min=2)])
	done = BooleanField("Done")

	class Meta:
		csrf = False
