from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import CheckInForm, CheckOutForm, AdminForm
import logic.data_work as dw
from logic.database import view_database


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Home")


@app.route("/admin", methods=["GET", "POST"])
def admin():
    form = AdminForm()
    if form.validate_on_submit():
        data = view_database(form.admin_id.data)
        if data:
            return render_template("all_visitors.html", title="All Visitors", data=data)
        else:
            flash("Wrong admin ID")
            return redirect(url_for("index"))
    return render_template("admin.html", title="Admin", form=form)


@app.route("/check_in", methods=["GET", "POST"])
def check_in():
    form = CheckInForm()
    if form.validate_on_submit():
        v, h = dw.filter_data(form.data)
        timestamp = dw.create_visitor_obj(v, h)
        flash(
            "Visitor = {} for Host = {} Checked In".format(
                form.v_name.data, form.h_name.data
            )
        )
        flash("Check-In ID is = {}".format(timestamp))
        return redirect(url_for("index"))
    return render_template("check_in.html", title="Check In", form=form)


@app.route("/check_out", methods=["GET", "POST"])
def check_out():
    form = CheckOutForm()
    if form.validate_on_submit():
        t = form.timestamp.data
        status = dw.destroy_visitor_obj(t)
        if status:
            flash("Visitor ID = {} Checked Out".format(form.timestamp.data))
        else:
            flash("Visitor ID invalid. Please Try Again.")
        return redirect(url_for("index"))
    return render_template("check_out.html", title="Check Out", form=form)
