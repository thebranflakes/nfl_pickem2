from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime

# Create Flask Instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "69_secret_key_420"


# Create a Form Class
class NamerForm(FlaskForm):
    name = StringField("Whats Your Name", validators=[DataRequired()])
    submit = SubmitField("Submit")


# FILTERS:
# safe
# capitalize
# lower
# upper
# title
# trim
# striptags


# Create a route
@app.route('/')
def index():
    nfl_teams = ["ARI", "ATL", "BAL", "BUF", "CAR", "CHI", "CIN", "CLE", "DAL", "DEN", "DET", "GB", "HOU", "IND",
                 "JAX", "KC", "LAC", "LAR", "MIA", "MIN", "NE", "NO", "NYG", "NYJ", "LV", "PHI", "PIT", "SEA", "SF",
                 "TB", "TEN", "WAS"]
    return render_template('index.html', nfl_teams=nfl_teams)


# localhost:5000/user/John
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


# Create Custom Error Pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


# Create name page
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash('Form Submitted Successfully!')

    return render_template('name.html', name=name, form=form)
