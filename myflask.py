from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1> Hello Puppy!! </h1>"

@app.route("/user/<name>/")
def user(name):
    return f"<h3>Error or {name[1000]} </h3>"

@app.route("/puppy_latin/<name>")
def puppy_latin(name):
    if name.lower().endswith("y"):
        return f"latin name for puppy {name} is {name[:-1]}iful"
    else:
        return f"latin name for puppy {name} is {name}y"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)