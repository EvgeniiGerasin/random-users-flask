from config import DevConfig
from randomengine.random import RandomUserData

from flask import Flask, render_template


app = Flask(__name__)
app.config.from_object(DevConfig)


@app.route('/')
def index():
    random_data = RandomUserData().full_random()
    return render_template(
        'index.html', random_data=random_data
    )


if __name__ == "__main__":
    app.run()
