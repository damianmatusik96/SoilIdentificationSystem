

from flask import Blueprint
import DataService

main_blue = Blueprint('main_blue', __name__)


@main_blue.route('/predict', methods=['GET'])
def get_profile():
    return DataService.get_profile()
