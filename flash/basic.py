from flask import Flask,flash,render_template,session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField

app = Flask(__name__)

app.config["SECRET_KEY"] = 'asd'

class SForm(FlaskForm):
    submit = SubmitField("Click me")

@app.route('/', methods=["POST","GET"])
def index():

    form = SForm()
    if form.validate_on_submit():
        flash("You just clicked the button!!!")
        redirect(url_for('index'))
    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)