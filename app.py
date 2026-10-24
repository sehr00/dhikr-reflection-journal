from flask import Flask, render_template, request, redirect
import utils

app = Flask(__name__)

@app.route("/")
def home():
    dhikr = utils.get_random_dhikr()
    return render_template("index.html", dhikr=dhikr)

@app.route("/reflect", methods=["POST"])
def reflect():
    phrase = request.form["phrase"]
    reflection = request.form["reflection"]
    utils.save_reflection(phrase, reflection)
    return redirect("/reflections")

@app.route("/reflections")
def reflections():
    try:
        with open("reflections.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []
    return render_template("reflections.html", reflections=lines)

if __name__ == "__main__":
    app.run(debug=True)
@app.route("/reset", methods=["POST"])
def reset():
    utils.reset_reflections()
    return redirect("/reflections")
if __name__ == "__main__":
    app.run(debug=True)
