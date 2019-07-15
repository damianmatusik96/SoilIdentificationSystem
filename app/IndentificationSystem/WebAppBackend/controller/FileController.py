from flask import Blueprint, request
from flask_restful import Resource
from WebAppBackend.service import FileService


home_blue = Blueprint('home_blue', __name__)
# class UploadImage(Resource):
#     def post(self):
#         file = request.files['file']


@home_blue.route("/")
def home():
    return "Hello, World!"


@home_blue.route('/uploader', methods=['POST', 'GET'])
def upload_file():
    elo = request.files
    return FileService.save_files(request)


