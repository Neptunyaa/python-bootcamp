from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/hobby")
@app.route("/hobbies")
def hobbies():
    hobby = ["Reading", "Traveling", "Gaming", "Cooking", "Hiking"]
    return render_template("hobbies.html", hobby=hobby)

@app.route("/opinion/play")
@app.route("/opinion/plays")
def opinion(play):
    game = ["Dota 2", "Apex", "Honkai", "Farlight", "Siege Six"]
    return render_template("game_opinion.html", game=game)

@app.route("/opinion/food")
def food_opinion():
    foods = ["Pizza", "Sushi", "Pasta", "Burgers", "Fries"]
    return render_template("food_opinion.html", foods=foods)

if __name__ == "__main__":
    app.run(debug=True)