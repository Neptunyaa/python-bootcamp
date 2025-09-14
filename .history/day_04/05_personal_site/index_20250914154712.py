from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main.html")


@app.route("/hobby")
@app.route("/hobbies")
def hobby():

    return render_template("hobbies.html")


@app.route("/opinion/<play>")
@app.route("/opinions/<play>")
def opinion(play):
    return render_template("opinion.html", play=play)

@app.route("/opinion/food")
def food_opinion():
    foods = ["Pizza", "Sushi", "Pasta", "Burgers", "Fries"]
    return render_template("food_opinion.html", foods=foods)

app.run()

