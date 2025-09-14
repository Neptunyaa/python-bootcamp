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
@app.route("/opinions/play")
def opinion(play):
    game = ["Soccer", "Basketball", "Tennis", "Cricket", "Baseball"]
    return render_template("opinion.html", play=play)

@app.route("/opinion/food")
def food_opinion():
    foods = ["Pizza", "Sushi", "Pasta", "Burgers", "Fries"]
    return render_template("food_opinion.html", foods=foods)

if __name__ == "__main__":
    app.run(debug=True)