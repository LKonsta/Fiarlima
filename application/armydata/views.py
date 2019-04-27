from flask import render_template

from application import app, db
from application.armydata.models import ArmyType, UnitType, Unit

@app.route("/armydata", methods=["GET"])
def armydata_index():

	return render_template(
		"armydata/army.html", 
		armytypedata = ArmyType.query.order_by(ArmyType.name).all(), 
		unittypedata = UnitType.query.order_by(UnitType.ArmyType_id).all(), 
		unitdata = Unit.query.order_by(Unit.Army_id).all()
	)

