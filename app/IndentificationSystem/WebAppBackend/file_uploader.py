from flask import *
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route("/upload")
def upload():
    return render_template('upload.html')


@app.route('/uploader', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        files = request.files.getlist('files[]')
        for file in files:
            file.save(secure_filename(file.filename))
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
