from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Home Page"


@app.route("/hobby")
@app.route("/hobbies")
def hobbies():
    return ("Hobbies Page")


@app.route("/opinion/<play>")
@app.route("/opinions/<play>")
def opinion(play):
    return f"Opinion about {play}"

@app.route("/opinion/food")
def food_opinion():
    foods = ["Pizza", "Sushi", "Pasta", "Burgers", "Fries"]
    return f"Food Opinion: {', '.join(foods)}"

app.run()

