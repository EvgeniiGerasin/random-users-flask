from flask import Flask, request, send_from_directory
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
        csv = request.form['csv']
        r.start_date = date_from
        r.stop_date = date_to
        r.gender = gender
        if csv == 'true':
            r.generate_csv_users(number=number)
            path = 'data_users.csv'
            dir = 'engine/csv'
            return send_from_directory(
                dir,
                path,
                as_attachment=True
            )
        user = r.castom_random_user()
        context = {
            'user': user,
            'date_from': date_from,
            'date_to': date_to,
            'gender': gender,
            'number': number,
        }
        return render_template('settings.html', data=context)
    context = {
        'user': r.full_random_user(),
        'date_from': '1970-01-01',
        'date_to': '2021-01-01',
        'gender': 'random',
        'number': 1,
    }
    return render_template('settings.html', data=context)
