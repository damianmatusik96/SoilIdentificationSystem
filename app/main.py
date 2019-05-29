from app.IndentificationSystem import data_cluster, data_handler_3, data_cluster_3
from app.IndentificationSystem.data.ProfilePredictor import ProfilePredictor
import matplotlib.pyplot as plt


if __name__ == "__main__":
    data_cluster.choose_best_cluster(2, 8)
    profile_predictor = ProfilePredictor(data_handler_3.data, data_cluster)

    profile_predictor.get_best_profile()
    data_cluster_3.choose_best_cluster(2,8)
    plt.show()
    # data_cluster_3.choose_best_cluster(2, 8)
