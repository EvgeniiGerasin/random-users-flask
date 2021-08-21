from config import DevConfig
from randomengine.random import RandomUserData

from flask import Flask


app = Flask(__name__)
app.config.from_object(DevConfig)


@app.route('/')
def index():
    data = RandomUserData().full_random()
    return f"{data[0]} {data[1]} {data[2]} {data[3]} | логин: {data[4]} |  пароль: {data[5]}"


if __name__ == "__main__":
    app.run()
