from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, BooleanField, IntegerField, validators

from application.armydata.models import Unit

class ListsForm(FlaskForm):
	choices = [('1','null')]
	army_type_id = SelectField("Army", choices=choices)
	name = StringField("List name", [validators.length(min=2)])
	points = IntegerField("Points")

	class Meta:
		csrf = False


class New_UnitForm(FlaskForm):
	unit = SelectField("Unit",choices=[])
	amount = IntegerField("Amount", [validators.Required()])
	final = BooleanField('Final')

	def validate(self):
		super_validate = super().validate()
		if not super_validate:
			return False

		unit = Unit.query.filter_by(id=self.unit.data).first()
		max = unit.max_amount
		min = unit.start_number
		if self.amount.data > max or self.amount.data < min:
			self.amount.errors.append(f'Not within the valid range from {min} to max {max} !')
			return False

		return True

	class Meta:
		csrf = False



class EditListForm(FlaskForm):
	name = StringField("List name", [validators.length(min=2)])
	points = IntegerField("Points")

	class Meta:
		csrf = False