# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 23:00:59 2019

@author: Dejwu
"""

import pandas as pd
from sklearn.cluster import KMeans as km
import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score as ss

data = pd.read_csv("sdm.csv", sep=";", header=None)
data.columns = ["a", "b", "c"]

data_pr = data[["b", "c"]]

plt.scatter(data_pr.b, data_pr.c)

kmeans = km(init='k-means++', n_clusters=3, random_state=0).fit(data_pr.as_matrix())
# data_pr['labels'] =pd.Series(kmeans.labels_)
# data_pr.plot.scatter(x='b',y='c',c='labels', colormap='viridis')
data_pr1 = data_pr.copy()
scores = []

for k in range(2, 10):
    kmeans = km(init='k-means++', n_clusters=k, random_state=0).fit(data_pr.as_matrix())
    data_pr1['labels'] = pd.Series(kmeans.labels_)
    print(len(kmeans.labels_))
    data_pr1.plot.scatter(x='b', y='c', c='labels', colormap='viridis')
    scores.append(ss(data_pr1[['b', 'c']], labels=data_pr1['labels']))

print(data_pr1)
n = [i for i in range(2, 10)]
plt.figure()
plt.plot(n, scores)
plt.show()

# zmiana txt do csv

# param1 = list()
# param2 = list()
# depth = list()
# all_data = list()
#
# filepath = "files\\sdmt3.txt"
# import pandas as pd
#
# with open(filepath, encoding="utf8", mode="r") as myfile:
#     for row in myfile:
#         d, p1, p2 = row.split()
#         depth.append(float(d.replace(',', '.')))
#         # depth.append(d)
#         param1.append(float(p1))
#         param2.append((float(p2)))
#
#     for x in range(0, len(depth)):
#         all_data.append(list([depth[x], param1[x], param2[x]]))
#
# datapd = pd.DataFrame(all_data)
#
# datapd.to_csv("sdmt3.csv", sep=';', encoding='utf-8', index=False, header=False)