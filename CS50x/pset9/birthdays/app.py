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
    if request.method == "POST":

        # Add the user's entry into the database
        name = request.form.get("name")
        if not name:
            return redirect("/")

        day = request.form.get("day")
        if not day:
            return redirect("/")
        try:
            day = int(day)
        except ValueError:
            return redirect("/")
        if day < 1 or day > 31:
            return redirect("/")


        month = request.form.get("month")
        if not month:
            return redirect("/")
        try:
            month = int(month)
        except ValueError:
            return redirect("/")
        if month < 1 or month > 12:
            return redirect("/")

        print(f"Name is {name}")
        print(f"Day is {day}")
        print(f"Month is {month}")

        db.execute("INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)", name, month, day)

        return redirect("/")

    else:

        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

        # Display the entries in the database on index.html
        rows = db.execute("SELECT * FROM birthdays")
        print(rows)

        return render_template("index.html", birthdays=rows, months=months)


