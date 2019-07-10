from WebAppBackend.service import fileService
from WebAppBackend import app
from flask import render_template, request


# @app.route("/upload")
# def upload():
#     return render_template("upload.html")


@app.route('/uploader', methods=['POST'])
def upload_file():
    return fileService.saveFiles(request)
