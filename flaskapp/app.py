import re
from flask import Flask, request, send_from_directory, jsonify
from flask.templating import render_template

import os
import time

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


@app.route('/api_description')
def api_description():
    return render_template('api_description.html')


@app.route('/api/random')
def api_random():

    r = RandomUserData()
    # if not one parameters return full random user
    if len(request.args) == 0:
        resp = {
            'status': True,
            'users': [
                r.full_random_user()
            ]
        }
        return jsonify(resp)

    date_from = request.args.get('date_from')
    date_to = request.args.get('date_to')
    gender = request.args.get('gender')
    number = request.args.get('number')

    if date_from and date_to:

        # check format date
        date_from_cond = re.match(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', date_from)
        date_to_cond = re.match(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', date_to)
        if not date_from_cond or not date_to_cond:
            resp = {
                'status': False,
                'test error': 'The date format must be YYYY-mm-dd. For example try /api/random?date_from=1990-01-01&date_to=2010-02-02'
            }
            return jsonify(resp)
        # check difference date
        try:
            d_f = time.mktime(time.strptime(date_from, '%Y-%m-%d'))
            d_t = time.mktime(time.strptime(date_to, '%Y-%m-%d'))
        except ValueError:
            resp = {
                'status': False,
                'test error': 'The date format must be YYYY-mm-dd. For example try /api/random?date_from=1990-01-01&date_to=2010-02-02'
            }
            return jsonify(resp)
        if d_f > d_t:
            resp = {
                'status': False,
                'test error': 'Date from must be earlier than date to'
            }
            return jsonify(resp)
        # application of dates
        r.start_date = date_from
        r.stop_date = date_to
    # if dates not get
    elif date_to and not date_from or date_from and not date_to:
        resp = {
            'status': False,
            'test error': 'Date from and date to should be transferred together'
        }
        return jsonify(resp)
    # check gender
    if gender == 'male' or gender == 'female' or gender == 'random':
        r.gender = gender
    else:
        resp = resp = {
            'status': False,
            'test error': 'Gender users is wrong. Gender should be male or female. For example try /api/random?gender=male or /api/random?gender=female or /api/random?gender=random'
        }
        return jsonify(resp)
    # check number users generation
    if number or number == '':
        users = []
        try:
            amount = int(number)
        except ValueError:
            resp = {
                'status': False,
                'test error': 'Number users is wrong. For example try /api/random?number=33'
            }
            return jsonify(resp)
        # check if number == 0
        if amount < 1:
            resp = {
                'status': False,
                'test error': 'Number users is wrong. Should be > 0'
            }
            return jsonify(resp)
        # * main function
        for _ in range(0, amount):
            users.append(r.castom_random_user())
            resp = {
                'status': True,
                'users': users,
            }
        return jsonify(resp)
