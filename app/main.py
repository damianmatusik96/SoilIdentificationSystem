from app.IndentificationSystem import data_cluster_1, data_cluster_3, data_cluster_2, data_handler_3
from app.IndentificationSystem.data.ProfilePredictor import ProfilePredictor

if __name__ == "__main__":
    data_cluster_1.choose_best_cluster(2, 8)
    data_cluster_2.choose_best_cluster(2, 8)
    print(data_cluster_1.grouped_data)

    cluster_list = list()
    cluster_list.append(data_cluster_1)
    cluster_list.append(data_cluster_2)
    profile_predictor = ProfilePredictor(data_handler_3.data, cluster_list)
    profile_predictor.get_best_profile()
    data_cluster_3.choose_best_cluster(2, 8)
