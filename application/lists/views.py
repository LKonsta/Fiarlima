from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.lists.models import Armylist
from application.lists.forms import ListsForm

@app.route("/lists", methods=["GET"])
def lists_index():
	return render_template("lists/list.html", lists = Armylist.query.all())

@app.route("/lists/new/")
@login_required
def lists_form():
	return render_template("lists/new.html", form = ListsForm())

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


	if not form.validate():
		return render_template("lists/new.html", form = form)

	l = Armylist(form.name.data)
	l.done = form.done.data
	l.account_id = current_user.id

	db.session().add(l)
	db.session().commit()

	return redirect(url_for("lists_index"))
