from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)
session = {"todo" : []}

@app.route("/")
def index():
    now = datetime.now()
    return render_template('main.html', hour=now.hour)

@app.route("/hobby")
@app.route("/hobbies")
def hobbies():
    hobby = ["Reading", "Traveling", "Gaming", "Cooking", "Hiking"]
    return render_template("hobbies.html", hobby=hobby)

@app.route("/opinion/game")
@app.route("/opinion/games")
def opinion():
    game = ["Dota 2", "Apex", "Honkai", "Farlight", "Siege Six"]
    return render_template("opinion.html", game=game)

@app.route("/opinion/food")
def food_opinion():
    foods = ["Pizza", "Sushi", "Pasta", "Burgers", "Fries"]
    return render_template("food_opinion.html", foods=foods)

@app.route("/skills")
def skills():
    skills = {
        "Photoshop": "Intermediate",
        "Illustrator": "Beginner",
        "After Effects": "Intermediate",
        "Figma": "Intermediate",
        "Premiere Pro": "Intermediate",
        "Blender" : "Beginner",
    }
    return render_template("skills.html", skills=skills)

@app.get("/todo/")
def show_todo():
    return render_template("todo.html", todos=session["todo"])

@app.post("/todo/")
def add_todo():
    if request.form.get("todo"):
        session["todos"].append(request.form["todo"])
    return redirect("todo.html")

if __name__ == "__main__":
    app.run(debug=True)