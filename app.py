import logging
from PIL import Image
from pytesseract import pytesseract

from flask import Flask, render_template, request

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.static_folder = 'static'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    try:
        file = request.files['file']
        # TODO Extends to PDFs. For now, file will be considered as an image.
        path = f'./uploads/{file.filename}'
        file.save(path)
        logging.debug(f'File saved to {path}.')
        text = extract_text_from_image(path)
        logging.debug('File processed.')
        return {
            'text': text,
            'message': 'File uploaded.',
        }
    except Exception as e:
        return {
            'internal_error': f'{e}',
        }


def extract_text_from_image(path):
    """Extract text from image in the given path.

    Args:
        path (str): path to the image to be processed.
    Returns:
        extracted text from the image
    """
    image = Image.open(path)
    text = pytesseract.image_to_string(image)
    return text


if __name__ == '__main__':
    app.run(debug=True)
