from flask import render_template, request, redirect, url_for
from sqlalchemy import desc

from application import app, db
from application.armydata.models import ArmyType, UnitType, Unit
from application.armydata.forms import ArmyTypeForm, UnitTypeForm, UnitForm

@app.route("/armydata", methods=["GET"])
def armydata_index():

	if ArmyType.is_army_type_empty() == 0:
		ArmyType.army_type_data_fill()

	if UnitType.is_unit_type_empty() == 0:
		UnitType.unit_type_data_fill()

	if Unit.is_unit_empty() == 0:
		Unit.unit_data_fill()

	return render_template("armydata/army.html", armytypedata = ArmyType.query.order_by(ArmyType.name).all(), unittypedata = UnitType.query.order_by(UnitType.ArmyType_id).all(), unitdata = Unit.query.order_by(Unit.Army_id).all())

