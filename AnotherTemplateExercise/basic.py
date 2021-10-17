import re
from flask import Flask, request, render_template

app = Flask(__name__)
reqs = ["Must have uppercase somewhere", "Must have lowercase somewhere", "Should end with a number" ]


@app.route("/")
def index():
    return render_template('index.html', reqs=reqs)

@app.route("/nameCheck")
def nameCheck():
    uName = request.args.get("uname")
    lower=upper=num= False

    lower = any(c.islower() for c in uName)
    upper = any(c.isupper() for c in uName)
    num = not uName[-1].isalpha()
    
    freqs = []
    if not lower:
        freqs.append(reqs[1])
    if not upper:
        freqs.append(reqs[0])
    if not num:
        freqs.append(reqs[2])

    return render_template("report.html", uName=uName, reqs=freqs)

@app.errorhandler(404)
def notFound(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=False)