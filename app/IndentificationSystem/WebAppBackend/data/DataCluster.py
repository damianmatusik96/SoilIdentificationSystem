from sklearn.metrics import silhouette_score as ss
import matplotlib.pyplot as plt
import pandas as pd
from sklearn_extensions.fuzzy_kmeans import FuzzyKMeans
from sklearn import metrics

class DataCluster:
    def __init__(self, data):
        self.data = data.copy()
        self.grouped_data = None
        self.fuzzy = None
        self.sorted_data = None

    @staticmethod
    def order_data(data, order_by):
        sorted_data = data.sort([order_by])
        return sorted_data[['param_1', 'param_2']]

    def choose_best_cluster(self, min_clusters, max_clusters):
        scores = list()

        for k in range(min_clusters, max_clusters):
            data = self.data.copy()
            score, fuzzy = self.create_cluster(data, k)
            scores.append(score)

        max_score = max(scores)
        k = scores.index(max_score) + min_clusters
        score, fuzzy = self.create_cluster(self.data, k)

        self.fuzzy = fuzzy
        self.grouped_data = self.group_data(self.data, fuzzy.labels_)
        self.plot(self.data, fuzzy, k, score)

    def create_cluster(self, data, number_of_clusters):
        fuzzy = self.create_fuzzy(number_of_clusters, data)
        score = self.cluster_quality(data, fuzzy.labels_)
        return score, fuzzy

    @staticmethod
    def create_fuzzy(number_of_clusters, data):
        fuzzy_kmeans = FuzzyKMeans(k=number_of_clusters, m=2, max_iter=100)
        fuzzy_kmeans.fit(data)
        return fuzzy_kmeans

    @staticmethod
    def cluster_quality(data, labels):
        data['labels'] = pd.Series(labels)
        score = ss(data[['param_1', 'param_2']], labels=data['labels'])
        return score

    def group_data(self, data, labels):
        group_data = data.groupby(pd.Series(labels), group_keys=data['labels'].unique())
        return group_data

    def plot(self, data, fuzzy, number_of_clusters, score):
        plt.figure()
        for center in fuzzy.cluster_centers_:
            plt.plot(center[0], center[1], 'ro')

        data.plot.scatter(x='param_1', y='param_2', c='labels', colormap='viridis')
        plt.xlabel("Param 1")
        plt.ylabel("Param 2")
        plt.title(f'K = {number_of_clusters}, Silhouette score = {score}')
        # plt.show()

    def sort_data(self):
        data = self.data.copy()
        reset_index_data = data.reset_index()
        prepared_data = reset_index_data.sort_values('labels')
        final_data = prepared_data.reset_index()

        self.sorted_data = final_data[['param_1', 'param_2', 'labels']]

# for self.datapd['labels']

# print(datapd)
# print(group_data[1].get_group(1))K


#
# n = [i for i in range(2, 10)]
# plt.figure()
# # plt.plot(n, scores)
# plt.xlabel("K")
# plt.ylabel("Silhouette score")
