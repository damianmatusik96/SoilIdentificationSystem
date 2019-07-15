from werkzeug.utils import secure_filename


def save_files(request):
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file.save(secure_filename(file.filename))
            return 'Hello'


def hello():
    return "hello"
