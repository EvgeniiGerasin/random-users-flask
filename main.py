from config import DevConfig

from flask import Flask


app = Flask(__name__)
app.config.from_object(DevConfig)


@app.route('/')
def index():
    return 'All Ok'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
