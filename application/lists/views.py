from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.lists.models import Armylist, Unit_Armylist
from application.lists.forms import ListsForm, NewUnitForm

from application.armydata.models import ArmyType, UnitType, Unit
from application.armydata.forms import ArmyTypeForm, UnitTypeForm, UnitForm

from application.auth.models import User
from application.auth.views import LoginForm

@app.route("/lists", methods=["GET"])
def lists_index():
	return render_template("lists/list.html", lists = Armylist.query.all(), account = User.query.all(), armies = ArmyType.query.all())

@app.route("/lists/show/<list_id>", methods=["GET"])
def lists_show_list(list_id):
	list_id = list_id
	return render_template("lists/show.html", list = Armylist.query.filter_by(list_id=Armylist.id).first(), unitsinlist = Unit_Armylist.query.filter_by(list_id=Unit_Armylist.armylist_id).all(), unittype = UnitType.query.all())


@app.route("/lists/my", methods=["GET"])
@login_required
def lists_user_lists():
	return render_template("lists/userlists.html", lists = Armylist.query.filter_by(account_id=current_user.id).all(), armies = ArmyType.query.all())

@app.route("/lists/new/")
@login_required
def lists_form():
	form = ListsForm()
	form.army_id.choices = [(int(army.id), army.name) for army in ArmyType.query.all()]

	return render_template("lists/new.html", form = form, armies = ArmyType.query.all(), unittypes = UnitType.query.all(), units = Unit.query.all())

@app.route("/lists/new/", methods=["GET"])
@login_required
def lists_newUnit():
	formUnit = NewUnitForm()

	return render_template("lists/newUnit.html", formUnit = formUnit)

@app.route("/lists/<list_id>/", methods=["POST"])
@login_required
def lists_set_done(list_id):

	al = Armylist.query.get(list_id)
	al.done = True
	db.session().commit()

	return redirect(url_for("lists_index"))


@app.route("/lists/", methods=["POST"])
@login_required
def lists_create():
	form = ListsForm(request.form)

	form.army_id.choices = [(int(army.id), army.name) for army in ArmyType.query.all()]

#	if not form.validate():
#		return render_template("lists/new.html", form = form, armies = ArmyType.query.all())

	l = Armylist(form.name.data, form.points.data)

	l.army_id = int(form.army_id.data)
	l.done = form.done.data
	l.points = form.points.data
	l.account_id = current_user.id

	db.session().add(l)
	db.session().commit()

	return redirect(url_for("lists_index"))
