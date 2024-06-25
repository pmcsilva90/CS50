import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    rows = db.execute("SELECT * FROM birthdays")

    if request.method == "POST":

        # Add the user's entry into the database
        name = request.form.get("name")
        if not name:
            return render_template("index.html", birthdays=rows, months=monthserror_message="Error adding birthday: must include name")
            #return redirect("/")

        day = request.form.get("day")
        if not day:
            return render_template("index.html", error_message="Error adding birthday: must include day")
            #return redirect("/")
        try:
            day = int(day)
        except ValueError:
            return render_template("index.html", error_message="Error adding birthday: invalid day format")
            #return redirect("/")
        if day < 1 or day > 31:
            return render_template("index.html", error_message="Error adding birthday: invalid day value")
            #return redirect("/")


        month = request.form.get("month")
        if not month:
            return render_template("index.html", error_message="Error adding birthday: must include month")
            # return redirect("/")
        try:
            month = int(month)
        except ValueError:
            return render_template("index.html", error_message="Error adding birthday: invalid month format")
            # return redirect("/")
        if month < 1 or month > 12:
            return render_template("index.html", error_message="Error adding birthday: invalid month value")
            #return redirect("/")

        print(f"Name is {name}")
        print(f"Day is {day}")
        print(f"Month is {month}")

        db.execute("INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)", name, month, day)

        return redirect("/")

    else:



        # Display the entries in the database on index.html

        print(rows)

        return render_template("index.html", birthdays=rows, months=months)


