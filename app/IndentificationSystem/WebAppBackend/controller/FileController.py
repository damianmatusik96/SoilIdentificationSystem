from flask import Blueprint, request

from WebAppBackend.service import FileService


home_blue = Blueprint('home_blue', __name__)


@home_blue.route("/")
def home():
    return "Hello, World!"


@home_blue.route('/save/train', methods=['POST'])
def upload_train_file():
    return FileService.save_files(request, "train_data")


@home_blue.route('/save/predict', methods=['POST'])
def upload_predict_file():
    return FileService.save_files(request, "predict_data")


# @home_blue.route('/predict', methods=['GET'])
# def get_profile():
#     return FileService.main()




