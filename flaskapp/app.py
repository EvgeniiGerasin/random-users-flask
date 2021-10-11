from flask import Flask, request
from flask.templating import render_template

import os

from flaskapp.engine.random import RandomUserData

app = Flask(__name__)


@app.route('/')
def index():
    context = RandomUserData().full_random_user()
    return render_template('index.html', user=context)

@app.route('/settings', methods=('GET', 'POST'))
def settings():

    r = RandomUserData()

    if request.method == 'POST':

        try:
            os.remove('flaskapp/engine/csv/data_users.csv')
        except:
            pass

        date_from = request.form['date_from']
        date_to = request.form['date_to']
        gender = request.form['gender']
        number = int(request.form['number'])
        # csv = bool(request.form['type'])
        r.start_date = date_from
        r.stop_date = date_to
        r.gender = gender
        user = r.castom_random_user()
        context = {
            'user': user,
            'date_from': date_from,
            'date_to': date_to,
            'gender': gender,
        }
        return render_template('settings.html', data=context)

    context = r.full_random_user()
    return render_template('settings.html', user=context)