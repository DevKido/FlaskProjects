from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    owner="Kido"

    fruits = ["Apple", "Orange", "Banana"]

    return render_template("basic.html",owner=owner, fruits=fruits)

if __name__ == "__main__":
    app.run(debug=True)
