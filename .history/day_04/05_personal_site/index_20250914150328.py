from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hobby")
@app.route("/hobbies")
def hobbies():
    return render_template("hobbies.html")