from app.IndentificationSystem import data_cluster, data_handler_3, data_cluster_3
from WebAppBackend.data.ProfilePredictor import ProfilePredictor
import matplotlib.pyplot as plt


def get_profile():
    data_cluster.choose_best_cluster(2, 8)
    profile_predictor = ProfilePredictor(data_handler_3.raw_data_pr, data_cluster)
    profile_predictor.get_best_profile()
    profile_predictor.sort_data()
    siema = profile_predictor.sorted_data.copy()
    siema['depth'] = data_handler_3.raw_data['depth']
    profile_predictor.sorted_data = siema
    json_data = profile_predictor.sorted_data.to_json()
    return json_data



