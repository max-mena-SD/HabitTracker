from flask import Flask, render_template, request

habits= ["test_habits"]

app= Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",habits=habits , title="Habit Tracker - Home")

@app.route("/add", methods=["GET", "POST"])
def add_habit():
    if request.form == "POST":
        pass

    return render_template("add_habit.html", title="Habit Tracker - Add Habit")