from werkzeug.utils import secure_filename
from flask import jsonify
from WebAppBackend.data.DataHandler import DataHandler
from WebAppBackend.data.DataCluster import DataCluster
from WebAppBackend.data.ProfilePredictor import ProfilePredictor
import os


def save_files(request, directory):
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file.save(os.path.join(directory, secure_filename(file.filename)))
            a = jsonify('Hello')
            return jsonify('Hello')


def create_cluster(*files):
    data_handler = DataHandler()
    data_handler.get_data(files)
    data_cluster = DataCluster(data_handler.sorted_data_pr)
    return data_cluster, data_handler


def create_profile(data_cluster, data_handler):
    data_cluster.choose_best_cluster(2, 8)
    profile_predictor = ProfilePredictor(data_handler.raw_data_pr, data_cluster)
    profile_predictor.get_best_profile()
    return profile_predictor.data


def main():
    train_data_cluster, train_data_handler = create_cluster('sdmt1.csv', 'sdmt2.csv')
    predict_data_cluster, predict_data_handler = create_cluster('sdmt3.csv')
    predictor_data = create_profile(predict_data_handler.raw_data_pr, train_data_cluster)
    return predictor_data
