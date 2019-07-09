from flask import Blueprint

from WebAppBackend.service import FileService


home_blue = Blueprint('home_blue', __name__)


@home_blue.route("/")
def home():
    return "Hello, World!"


@home_blue.route('/uploader', methods=['POST'])
def upload_file(request):
    return FileService.save_files(request)
