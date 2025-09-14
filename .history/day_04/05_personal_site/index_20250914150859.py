from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Home Page"


@app.route("/hobby")
@app.route("/hobbies")
def hobbies():
    return ("Hobbies Page")

@app.route("/opinion/<game>")
@app.route("/opinions/<game>")
def opinion(game):
    return f"Opinion about {game}"

@app.route("/opinion/<play>")
@app.route("/opinions/<play>")
def opinion(play):
    return f"Opinion about {play}"

@app.route("/food")
def food():
    foods = ["Pizza", "Sushi", "Pasta", "Burgers", "Fries"]
    return ("Food Opinion")



