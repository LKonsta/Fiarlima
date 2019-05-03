from flask import render_template, request, redirect, url_for, abort
from flask_login import login_user, logout_user, login_required

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, NewUserForm, EditNameForm


@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
	if request.method == "GET":
		return render_template("auth/loginform.html", form = LoginForm())

	form = LoginForm(request.form)

	user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
	if not user:
		return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")


	login_user(user)
	return redirect(url_for("index"))


@app.route("/auth/logout")
def auth_logout():
	logout_user()
	return redirect(url_for("index"))


@app.route("/auth/new")
def user_form():
	return render_template("auth/newuser.html", form = NewUserForm())


@app.route("/auth/new", methods=["POST"])
def user_create():
	form = NewUserForm(request.form)

	if form.validate() and request.method == 'POST':
		a = User(form.name.data, form.username.data, form.password.data)

		db.session().add(a)
		db.session().commit()

		return redirect(url_for("auth_login"))

	return render_template("auth/newuser.html", form=form)


@app.route("/auth/edit/<user_id>", methods=["GET", "POST"])
@login_required
def user_name_edit(user_id):
	form = EditNameForm(request.form)
	user = User.query.get(user_id)

	if request.method == 'POST' and form.validate():
		user.name = form.name.data

		db.session().commit()

		return redirect(url_for("lists_index"))

	form.name.data=user.name

	return render_template(
		"auth/edit_user.html",
		form=form
	)

