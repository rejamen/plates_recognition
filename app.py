from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return {'message': 'Hello Flask :D'}


if __name__ == '__main__':
    app.run(debug=True)
