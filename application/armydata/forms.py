from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, FieldList, BooleanField


class ArmyTypeForm(FlaskForm):
	name = StringField("Army name")
	tag = StringField("Army tag")

	class Meta:
		csrf = False


class UnitTypeForm(FlaskForm):
	name = StringField("UnitType name")
	MaxPoints = IntegerField("Max points")
	MinPoints = IntegerField("Min points")

	class Meta:
		csrf = False


class UnitForm(FlaskForm):
	name = StringField("Unit name")
	start_cost = IntegerField("Unit start cost")
	cost_per = IntegerField("Unit cost per")
	start_number = IntegerField("Unit start number")
	max_amount = IntegerField("Unit max amount")

	class Meta:
		csrf = False


class UpdateForm(FlaskForm):

	update = FieldList(BooleanField('Updates', []))