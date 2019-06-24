from flask import render_template
from werkzeug.utils import secure_filename


def saveFiles(request):
    if request.method == 'POST':
        files = request.files.getlist('files[]')
        for file in files:
            file.save(secure_filename(file.filename))
        return render_template('index.html')
