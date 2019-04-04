from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, BooleanField, IntegerField, validators

from application.armydata.models import ArmyType

class ListsForm(FlaskForm):
	list = []
#	for army in ArmyType.query.all():
#		list.append(army.id)

	army_id = IntegerField()
	name = StringField("List name", [validators.length(min=2)])
	points = IntegerField("Points")
	done = BooleanField("Done")

	class Meta:
		csrf = False
