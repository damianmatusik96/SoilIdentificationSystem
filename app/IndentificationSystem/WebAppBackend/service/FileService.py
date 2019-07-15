from werkzeug.utils import secure_filename
import os


def save_files(request, directory):
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file.save(os.path.join(directory, secure_filename(file.filename)))
            return 'Hello'


def hello():
    return "hello"
