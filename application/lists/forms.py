from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, BooleanField, IntegerField, validators

class ListsForm(FlaskForm):
	choices = [('1','null')]
	army_type_id = SelectField("Army", choices=choices)
	name = StringField("List name", [validators.length(min=2)])
	points = IntegerField("Points")

	class Meta:
		csrf = False


class New_UnitForm(FlaskForm):
	unit = SelectField("Unit",choices=[])
	amount = IntegerField("Amount", [validators.NumberRange(min=1, max=60)])

	class Meta:
		csrf = False
