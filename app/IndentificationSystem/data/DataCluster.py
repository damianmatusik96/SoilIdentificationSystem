import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import silhouette_score as ss
from sklearn_extensions.fuzzy_kmeans import FuzzyKMeans


class DataCluster:
    def __init__(self, data):
        self.data = data
        self.grouped_data = None

    def create_cluster(self):
        fuzzy = self.create_fuzzy(4, self.data)
        score = self.cluster_quality(self.data, fuzzy.labels_)
        self.grouped_data = self.group_data(self.data, fuzzy.labels_)
        self.plot(self.data, fuzzy, 4, score)

    def create_fuzzy(self, number_of_clusters, data):
        fuzzy_kmeans = FuzzyKMeans(k=number_of_clusters, m=4, max_iter=300)
        fuzzy_kmeans.fit(data)
        return fuzzy_kmeans

    def cluster_quality(self, data, labels):
        data['labels'] = pd.Series(labels)
        score = ss(data[['b', 'c']], labels=data['labels'])
        return score

    def group_data(self, data, labels):
        group_data = data.groupby(pd.Series(labels), group_keys=data['labels'].unique())
        return group_data

    def plot(self, data, fuzzy, number_of_clusters, score):
        plt.figure()
        for center in fuzzy.cluster_centers_:
            plt.plot(center[0], center[1], 'ro')

        data.plot.scatter(x=0, y=1, c='labels', colormap='viridis')
        plt.xlabel("Param 1")
        plt.ylabel("Param2")
        plt.title(f'K = {number_of_clusters}, Silhouette score = {score}')
        plt.show()

# for self.datapd['labels']

# print(datapd)
# print(group_data[1].get_group(1))K


#
# n = [i for i in range(2, 10)]
# plt.figure()
# # plt.plot(n, scores)
# plt.xlabel("K")
# plt.ylabel("Silhouette score")
