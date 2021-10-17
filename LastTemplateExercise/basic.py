from flask import Flask,request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/sign_up")
def sign_up():
    return render_template("signup.html")

@app.route("/thank_you")
def thank_you():
    first_name = request.args.get("first")
    last_name  =request.args.get("last")

    return render_template("thankyou.html", fn=first_name, ln=last_name)


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)