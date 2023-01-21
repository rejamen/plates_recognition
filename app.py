import logging

from flask import Flask, request

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)


@app.route('/')
def index():
    return {'message': 'Hello Flask :D'}


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filename = file.filename
    file.save('./uploads/' + filename)
    logging.debug(f'File {filename} saved to uploads folder.')
    return {'message': 'File uploaded.'}


if __name__ == '__main__':
    app.run(debug=True)
