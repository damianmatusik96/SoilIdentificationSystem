from werkzeug.utils import secure_filename


def save_files(request):
    if request.method == 'POST':
        files = request.files.getlist('files[]')
        for file in files:
            file.save(secure_filename(file.filename))


def hello():
    return "hello"
