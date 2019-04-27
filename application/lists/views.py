from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.sql import text

from application import app, db
from application.lists.models import Armylist, Unit_Armylist
from application.lists.forms import ListsForm, New_UnitForm

from application.armydata.models import ArmyType, UnitType, Unit
from application.armydata.forms import ArmyTypeForm, UnitTypeForm, UnitForm

from application.auth.models import User
from application.auth.views import LoginForm


@app.route("/lists", methods=["GET"])
def lists_index():
    return render_template(
        "lists/list.html",
        lists=Armylist.query.all(),
        account=User.query.all(),
        armies=ArmyType.query.all()
    )


@app.route("/lists/show/<list_id>", methods=["GET"])
def lists_show_list(list_id):
    list_id = list_id
    army_id = Armylist.query.filter_by(id=list_id).first().army_type_id
    return render_template(
        "lists/show.html",
        list=Armylist.query.filter_by(id=list_id).first(),
        unitsinlist=Unit_Armylist.query.filter_by(Armylist_id=list_id).all(),
        unittype=UnitType.query.filter_by(ArmyType_id=army_id).all(),
    )


@app.route("/lists/delete/<list_id>", methods=["POST"])
@login_required
def list_remove(list_id):
    list_id = list_id
    list = Armylist.query.get(list_id)
    db.session().delete(list)
    db.session().commit()

    return redirect(url_for("lists_index"))


@app.route("/lists/my", methods=["GET"])
@login_required
def lists_user_lists():
    return render_template(
        "lists/userlists.html",
        lists=Armylist.query.filter_by(account_id=current_user.id).all(),
        armies=ArmyType.query.all()
    )


@app.route("/lists/new/")
@login_required
def lists_form():
    form = ListsForm()
    form.army_type_id.choices = [(str(army.id), army.name) for army in ArmyType.query.all()]

    return render_template(
        "lists/new.html",
        form=form,
        armies=ArmyType.query.all(),
        unittypes=UnitType.query.all(),
        units=Unit.query.all()
    )


@app.route("/lists/edit/<list_id>/<uil_id>", methods=["POST"])
@login_required
def list_remove_unit(list_id, uil_id):
    ual = Unit_Armylist.query.get(uil_id)
    db.session().delete(ual)
    db.session().commit()

    return redirect(url_for("lists_edit", list_id=list_id))


@app.route("/lists/", methods=["POST"])
@login_required
def lists_create():
    form = ListsForm(request.form)
    form.army_type_id.choices = [(str(a.id), a.name) for a in ArmyType.query.all()]

    if not form.validate():
        return render_template("lists/new.html",
                               form=form,
                               armies=ArmyType.query.all()
                               )

    l = Armylist(form.name.data, form.points.data)

    l.army_type_id = form.army_type_id.data
    l.points = form.points.data
    l.account_id = current_user.id

    db.session().add(l)
    db.session().commit()

    return redirect(url_for("lists_edit", list_id=l.id))


@app.route("/lists/edit/<list_id>", methods=["GET"])
@login_required
def lists_edit(list_id):
    list_id = list_id
    army_id = Armylist.query.filter_by(id=list_id).first().army_type_id
    return render_template(
        "lists/edit.html",
        list=Armylist.query.filter_by(id=list_id).first(),
        unitsinlist=Unit_Armylist.query.filter_by(Armylist_id=list_id).all(),
        unittype=UnitType.query.filter_by(ArmyType_id=army_id).all()
    )


@app.route("/lists/edit/<list_id>/add/<unittype_id>", methods=["POST", "GET"])
@login_required
def list_add_unit(list_id, unittype_id):
    form = New_UnitForm(request.form)
    list_id = list_id
    unittype_id = unittype_id
    unit_choices = Unit.query.filter_by(UnitType_id=unittype_id).all()
    form.unit.choices = [
        (
            str(unit.id),
            f"{unit.name} | {unit.start_cost} pts "
            f"{'+' + str(unit.cost_per) + ' pts/per extra' if unit.cost_per else ''} | "
            f"{'single model' if unit.max_amount == 1 else 'amount: ' + str(unit.start_number) + '-' + str(unit.max_amount)}"
        ) for unit in unit_choices
    ]
    form.amount.data = form.amount.data

    if request.method == 'POST' and form.validate():
        nu = Unit_Armylist(form.unit.data, form.amount.data)
        nu.Armylist_id = list_id

        db.session().add(nu)
        db.session().commit()

        return redirect(url_for('lists_edit', list_id=nu.Armylist_id))

    return render_template(
        "lists/new_unit.html",
        form=form,
        list_id=list_id,
        unittype_id=unittype_id
    )
