from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, BooleanField, IntegerField, validators

from application.armydata.models import ArmyType

class ListsForm(FlaskForm):

	army_id = SelectField("Army", choices=[])
	name = StringField("List name", [validators.length(min=2)])
	points = IntegerField("Points")
	done = BooleanField("Done")

	class Meta:
		csrf = False


class NewUnitForm(FlaskForm):
	extraamount = IntegerField("Extra Amount")

	class Meta:
		csrf = False
