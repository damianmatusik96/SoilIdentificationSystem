from flask import *
from werkzeug.utils import secure_filename
from WebAppBackend.service import fileService
app = Flask(__name__)


@app.route("/upload")
def upload():
    return render_template('upload.html')


@app.route('/uploader', methods=['POST'])
def upload_file():
    return fileService.saveFiles(request)


if __name__ == '__main__':
    app.run(debug=True)
