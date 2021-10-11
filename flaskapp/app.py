from flask import Flask
from flask.templating import render_template

from flaskapp.engine.random import RandomUserData

app = Flask(__name__)


@app.route('/')
def index():
    user = RandomUserData().full_random_user()
    return render_template('index.html', user=user)