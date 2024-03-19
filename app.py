import logging
import os
from io import BytesIO

from PIL import Image
from flask import Flask, render_template, request, send_file, abort
from rembg import remove
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Configure logger
LOG_FILE = 'app.log'
logging.basicConfig(filename=LOG_FILE, level=logging.INFO)
logger = logging.getLogger(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    try:
        if request.method == 'POST':
            if 'file' not in request.files:
                return 'No file part', 400
            file = request.files['file']
            if file.filename == '':
                return 'No selected file', 400
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                # Ensure the upload folder exists
                os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                input_image = Image.open(filepath)
                output_image = remove(input_image, post_process_mask=True)
                img_io = BytesIO()
                output_image.save(img_io, 'PNG')
                img_io.seek(0)
                return send_file(img_io, mimetype='image/png', as_attachment=True,
                                 download_name=filename[:-4] + '_rmbg.png')
            else:
                return 'Invalid file format. Allowed formats: png, jpg, jpeg, gif', 400
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        abort(500)

    return render_template('index.html')


@app.errorhandler(500)
def internal_server_error(error):
    return "Internal Server Error", 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100, debug=False)
