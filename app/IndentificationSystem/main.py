from flask import Blueprint

from app.IndentificationSystem import data_cluster, data_handler_3, data_cluster_3
from WebAppBackend.data.ProfilePredictor import ProfilePredictor
import matplotlib.pyplot as plt


def main():
    data_cluster.choose_best_cluster(2, 8)
    profile_predictor = ProfilePredictor(data_handler_3.raw_data_pr, data_cluster)
    profile_predictor.get_best_profile()
    json_data = profile_predictor.data.to_json()
    data_cluster_3.choose_best_cluster(2, 8)
    plt.show()
    return json_data
    # data_cluster_3.choose_best_cluster(2, 8)
