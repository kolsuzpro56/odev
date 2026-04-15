from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    name = ""
    skill = ""

    if request.method == "POST":
        name = request.form.get("name")
        skill = request.form.get("skill")

    return render_template("index.html", name=name, skill=skill)

if __name__ == "__main__":
    app.run(debug=True)