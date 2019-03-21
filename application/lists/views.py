from application import app, db
from flask import render_template, request, redirect, url_for
from application.lists.models import Armylist


@app.route("/lists", methods=["GET"])
def lists_index():
	return render_template("lists/list.html", lists = Armylist.query.all())

@app.route("/lists/new/")
def lists_form():
	return render_template("lists/new.html")

@app.route("/lists/<list_id>/", methods=["POST"])
def lists_set_done(list_id):
	
	al = Armylist.query.get(list_id)
	al.done = True
	db.session().commit()

	return redirect(url_for("lists_index"))


@app.route("/lists/", methods=["POST"])
def lists_create():
	l = Armylist(request.form.get("name"))

	db.session().add(l)
	db.session().commit()

	return redirect(url_for("lists_index"))
