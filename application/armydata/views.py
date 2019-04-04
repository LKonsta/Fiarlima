from flask import render_template, request, redirect, url_for
from sqlalchemy import desc

from application import app, db
from application.armydata.models import ArmyType, UnitType, Unit
from application.armydata.forms import ArmyTypeForm, UnitTypeForm, UnitForm

@app.route("/armydata", methods=["GET"])
def armydata_index():
	return render_template("armydata/army.html", armytypedata = ArmyType.query.order_by(ArmyType.name).all(), unittypedata = UnitType.query.order_by(UnitType.ArmyType_id).all(), unitdata = Unit.query.order_by(Unit.Army_id).all())

