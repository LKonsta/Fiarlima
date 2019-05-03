from flask import render_template
from application import app

from application.lists.models import Armylist, Unit_Armylist, Unit_Armylistupdate

from application.armydata.models import ArmyType, UnitType, Unit, UnitUpdates

from application.auth.models import User

@app.route("/")
def index():
	return render_template(
		"index.html",
		User=User.query.first())
