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
    category = request.form["category"]
    reflection = request.form["reflection"]

    utils.save_reflection(
        phrase,
        category,
        reflection
    )

    return redirect("/reflections")

@app.route("/reflections")
def reflections():
    query = request.args.get("q", "")

    try:
        with open("reflections.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []

    if query:
        lines = [
            line for line in lines
            if query.lower() in line.lower()
        ]

    return render_template(
    "reflections.html",
    reflections=lines,
    total=len(lines)
)

@app.route("/reset", methods=["POST"])
def reset():
    utils.reset_reflections()
    return redirect("/reflections")

# ✅ Only one run block at the very end
if __name__ == "__main__":
    app.run(debug=True)
