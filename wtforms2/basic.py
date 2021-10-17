from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, DateTimeField, RadioField, SelectField
from wtforms import validators
from wtforms.validators import DataRequired, NumberRange

app = Flask(__name__)

app.config['SECRET_KEY'] = 'key'

class InfoForm(FlaskForm):

    fname = StringField("First Name \t", validators=[DataRequired()])
    lname = StringField("Last Name \t", validators=[DataRequired()])
    age = StringField("Age \t", validators=[DataRequired()])
    sex = RadioField("Gender \t", validators=[DataRequired()], choices=[('1',"Male"), ('2',"Female")])
    dob = DateField("D.O.B \t", validators=[DataRequired()])
    hobbies = SelectField("Hobbies \t", validators=[DataRequired()], choices=[('game',"Gaming"), ('code',"Programming")])
    submit = SubmitField("Submit")

@app.route('/', methods=['GET','POST'])
def index():
    form = InfoForm()

    if form.validate_on_submit():
        session['fn'] = form.fname.data
        session['ln'] = form.lname.data
        session['age'] = form.age.data
        session['sex'] = form.sex.data
        session['dob'] = form.dob.data
        session['hobbies'] = form.hobbies.data

        return redirect(url_for('thankyou'))
    
    return render_template('index.html', form=form)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == "__main__":
    app.run(debug=True)