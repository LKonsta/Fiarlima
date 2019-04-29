from flask import render_template

from application import app, db
from application.armydata.models import ArmyType, UnitType, Unit, UnitUpdates

@app.route("/armydata", methods=["GET"])
def armydata_index():

	return render_template(
		"armydata/army.html", 
		armytypedata = ArmyType.query.all(),
		unittypedata = UnitType.query.all(),
		unitdata = Unit.query.all(),
		updatedata = UnitUpdates.query.all()
	)

