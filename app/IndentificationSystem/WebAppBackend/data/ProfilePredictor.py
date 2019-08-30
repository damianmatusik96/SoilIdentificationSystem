import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import silhouette_score


class ProfilePredictor:
    def __init__(self, data, cluster):
        self.data = data.copy()
        self.cluster = cluster
        self.sorted_data = None

    def sort_data(self):
        data = self.data.copy()
        reset_index_data = data.reset_index()
        prepared_data = reset_index_data.sort_values('labels')
        final_data = prepared_data.reset_index()

        self.sorted_data = final_data[['param_1', 'param_2', 'labels']]

    def get_best_profile(self):
        score = self.get_profile(self.cluster.fuzzy, self.cluster.data, self.data, self.cluster.grouped_data)
        # self.show_result(self.data, 4, score)

    def get_profile(self, fuzzy, cluster_data, data, learning_data):
        min, max = self.get_bounds(cluster_data, learning_data)
        score = self.set_labels(data, min, max, fuzzy)
        return score

    @staticmethod
    def get_bounds(cluster_data, learning_data):
        max_values = []
        min_values = []
        for group_label in cluster_data['labels'].unique():
            max_param1 = np.max(learning_data['param_1'].get_group(group_label))
            max_param2 = np.max(learning_data['param_2'].get_group(group_label))
            min_param1 = np.min(learning_data['param_1'].get_group(group_label))
            min_param2 = np.min(learning_data['param_2'].get_group(group_label))
            tuple_max = (max_param1, max_param2)
            tuple_min = (min_param1, min_param2)
            max_values.append(tuple_max)
            min_values.append(tuple_min)
        return min_values, max_values

    @staticmethod
    def set_labels(data, min_values, max_values, fuzzy):

        data['labels'] = pd.Series(fuzzy.labels_)
        for i in range(0, len(data.values)):
            for j in range(len(max_values)):
                x, y, z = data.values[i]
                max1, max2 = max_values[j]
                min1, min2 = min_values[j]

                if min1 < x < max1 and min2 < y < max2:
                    data.at[i, 'labels'] = j
                if x > max1 and y > max2:
                    data.at[i, 'labels'] = np.max(data['labels'])
                # elif x < max1 and y < max2:
                #     data.at[i, 'labels'] = np.min(data['labels'])
        score = silhouette_score(data[['param_1', 'param_2']], labels=data['labels'])
        return score

    def show_result(self, data, number_of_clusters, score):
        data.plot.scatter(x='param_1', y='param_2', c='labels', colormap='viridis')
        plt.xlabel("Param 1")
        plt.ylabel("Param 2")
        plt.title(f'K = 3, Silhouette score = {score}')
        # plt.show()

# def get_best_profile(self):
#     scores = list()
#     for cluster in self.cluster_list:
#         data = self.data.copy()
#         scores.append(self.get_profile(cluster.fuzzy, cluster.data, data, cluster.grouped_data))
#     max_score = max(scores)
#     max_index = scores.index(max_score)
#     best_cluster = self.cluster_list[max_index]
#
#     self.get_profile(best_cluster.fuzzy, best_cluster.data, self.data, best_cluster.grouped_data)
#     self.show_result(self.data, 4, max_score)
